#!/usr/bin/env python3
"""Digest editorial diario MML LATAM.

Fuentes:
- Review of Myopia Management (RSS)
- Myopia Profile (scraping clinical + science)

Resume cada artículo nuevo con Claude, guarda un snapshot público
en data/digest-latest.json (consumido por el home) y envía un email:
- Si BREVO_API_KEY está seteada → envía vía Brevo a todos los contactos
  de la lista BREVO_LIST_ID (default 6).
- Si no → fallback SMTP single recipient a EMAIL_TO.
"""

import json
import os
import smtplib
import sys
from datetime import datetime, timezone
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from pathlib import Path

import feedparser
import requests
from anthropic import Anthropic
from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parent.parent
STATE_FILE = ROOT / "state" / "last_seen.json"
SNAPSHOT_FILE = ROOT / "data" / "digest-latest.json"

ROMM_FEED = "https://reviewofmm.com/feed/"
MP_CATEGORIES = [
    ("Clinical", "https://www.myopiaprofile.com/articles/category/clinical"),
    ("Science", "https://www.myopiaprofile.com/articles/category/science"),
]
MP_BASE = "https://www.myopiaprofile.com"

SMTP_HOST = "mail.privateemail.com"
SMTP_PORT = 587
SMTP_USER = os.environ.get("SMTP_USER", "info@miopialatam.org")
EMAIL_FROM = os.environ.get("EMAIL_FROM", "info@miopialatam.org")
EMAIL_TO = os.environ.get("EMAIL_TO", "info@miopialatam.org")
SENDER_NAME = os.environ.get("SENDER_NAME", "Comité Editorial MML")

BREVO_API_BASE = "https://api.brevo.com/v3"
BREVO_LIST_ID = int(os.environ.get("BREVO_LIST_ID", "6"))

CLAUDE_MODEL = os.environ.get("CLAUDE_MODEL", "claude-haiku-4-5-20251001")

UA = "Mozilla/5.0 (compatible; MML-Digest/1.0; +https://miopialatam.org)"


def load_state() -> dict:
    if STATE_FILE.exists():
        return json.loads(STATE_FILE.read_text(encoding="utf-8"))
    return {"seen_urls": [], "first_run": True}


def save_state(state: dict) -> None:
    STATE_FILE.parent.mkdir(parents=True, exist_ok=True)
    STATE_FILE.write_text(
        json.dumps(state, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )


def fetch_romm() -> list[dict]:
    feed = feedparser.parse(ROMM_FEED)
    items = []
    for entry in feed.entries[:15]:
        summary = entry.get("summary", entry.get("description", "")) or ""
        soup = BeautifulSoup(summary, "html.parser")
        items.append({
            "source": "Review of Myopia Management",
            "source_short": "RoMM",
            "title": entry.title.strip(),
            "url": entry.link,
            "summary": soup.get_text(" ", strip=True)[:600],
            "published": entry.get("published", ""),
        })
    return items


def fetch_myopia_profile() -> list[dict]:
    items = []
    seen_urls = set()
    for label, url in MP_CATEGORIES:
        try:
            r = requests.get(url, timeout=20, headers={"User-Agent": UA})
            r.raise_for_status()
        except Exception as exc:
            print(f"warn: Myopia Profile {label} failed: {exc}", file=sys.stderr)
            continue
        soup = BeautifulSoup(r.text, "html.parser")
        for link in soup.select("a[href*='/articles/']"):
            href = link.get("href", "").strip()
            title = link.get_text(" ", strip=True)
            if not title or len(title) < 12:
                continue
            if href.startswith("/"):
                href = MP_BASE + href
            if "/articles/category/" in href or href.rstrip("/").endswith("/articles"):
                continue
            if href in seen_urls:
                continue
            seen_urls.add(href)
            items.append({
                "source": f"Myopia Profile · {label}",
                "source_short": "Myopia Profile",
                "title": title,
                "url": href,
                "summary": "",
                "published": "",
            })
    return items[:15]


def summarize(articles: list[dict], client: Anthropic) -> None:
    for art in articles:
        if art.get("summary_es"):
            continue
        prompt = (
            "Resumí en 2 líneas en español neutro LATAM el siguiente artículo "
            "para el digest diario del Comité Editorial MML LATAM (manejo de "
            "miopía). Sin saludos, sin markdown, sin viñetas. Solo 2 líneas, "
            "máximo 280 caracteres, tono editorial profesional.\n\n"
            f"Título: {art['title']}\n"
            f"Fuente: {art['source']}\n"
            f"Texto original: {art.get('summary', '')[:600] or '(solo título disponible)'}"
        )
        try:
            response = client.messages.create(
                model=CLAUDE_MODEL,
                max_tokens=180,
                messages=[{"role": "user", "content": prompt}],
            )
            art["summary_es"] = response.content[0].text.strip()
        except Exception as exc:
            art["summary_es"] = f"(Resumen no disponible: {exc})"


def write_snapshot(top_items: list[dict]) -> None:
    """Persistir las top 3 lecturas para que el home las muestre."""
    SNAPSHOT_FILE.parent.mkdir(parents=True, exist_ok=True)
    payload = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "date_display": datetime.now(timezone.utc).strftime("%d %b %Y"),
        "items": [
            {
                "source": it["source"],
                "source_short": it.get("source_short", it["source"]),
                "title": it["title"],
                "url": it["url"],
                "summary_es": it.get("summary_es", ""),
            }
            for it in top_items[:3]
        ],
    }
    SNAPSHOT_FILE.write_text(
        json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )


def render_html(articles: list[dict], bootstrap: bool) -> str:
    today = datetime.now(timezone.utc).strftime("%d %b %Y")
    if bootstrap:
        intro = (
            "<p>Bienvenido al digest editorial automatizado del Comité MML LATAM. "
            "Acabás de activar el sistema: a partir de mañana a las 7:00 AM "
            "vas a recibir solo las novedades nuevas de cada día. Hoy guardamos "
            "como referencia los artículos ya existentes en ambas fuentes para "
            "no enviártelos.</p>"
        )
        items_html = ""
    elif not articles:
        intro = (
            "<p>Sin novedades hoy en RoMM ni Myopia Profile. Volveremos mañana "
            "a las 7:00 AM con el siguiente digest.</p>"
        )
        items_html = ""
    else:
        word = "novedad destacada" if len(articles) == 1 else "novedades destacadas"
        intro = f"<p style='color:#5A7184;margin:0 0 1.4em'>{len(articles)} {word} para hoy.</p>"
        items_html = ""
        for i, art in enumerate(articles, 1):
            items_html += f"""
<div style="margin-bottom:1.3em;padding:1.1em 1.2em;background:#F7F9FC;border-left:4px solid #F5C518;border-radius:6px">
  <div style="font-size:11px;color:#0077C8;text-transform:uppercase;letter-spacing:0.08em;font-weight:700">{art['source']}</div>
  <div style="margin:0.45em 0 0.5em;font-size:16px;font-weight:700;color:#0A2540;line-height:1.3">{i}. {art['title']}</div>
  <div style="color:#333;line-height:1.55;font-size:14px">{art.get('summary_es', '')}</div>
  <a href="{art['url']}" style="display:inline-block;margin-top:0.7em;color:#0077C8;font-size:13px;font-weight:700;text-decoration:none">Leer artículo completo →</a>
</div>"""

    return f"""<!DOCTYPE html>
<html lang="es"><body style="margin:0;padding:0;background:#EEF2F6;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Inter,Arial,sans-serif;color:#0A2540">
<table role="presentation" cellpadding="0" cellspacing="0" width="100%" style="background:#EEF2F6;padding:24px 12px">
  <tr><td align="center">
    <table role="presentation" cellpadding="0" cellspacing="0" width="640" style="max-width:640px;background:#fff;border-radius:14px;overflow:hidden;box-shadow:0 4px 18px rgba(10,37,64,0.08)">
      <tr><td>
        <table cellpadding="0" cellspacing="0" border="0" width="100%"><tr>
          <td style="height:6px;background:#F5C518;line-height:6px;font-size:0;width:25%">&nbsp;</td>
          <td style="height:6px;background:#2EAA4A;line-height:6px;font-size:0;width:25%">&nbsp;</td>
          <td style="height:6px;background:#0077C8;line-height:6px;font-size:0;width:25%">&nbsp;</td>
          <td style="height:6px;background:#D42B2B;line-height:6px;font-size:0;width:25%">&nbsp;</td>
        </tr></table>
      </td></tr>
      <tr><td style="padding:30px 32px 6px">
        <table cellpadding="0" cellspacing="0" border="0" style="margin-bottom:18px"><tr>
          <td style="padding-right:16px;vertical-align:middle"><img src="https://miopialatam.org/logo-preview-circulo.png" alt="MML LATAM · Grupo Manejo Miopía Latinoamérica" width="74" height="74" style="display:block;border:0;border-radius:50%"></td>
          <td style="vertical-align:middle;border-left:1px solid #E5EAEF;padding-left:16px"><div style="font-family:Arial,Helvetica,sans-serif;font-weight:900;font-size:13px;color:#0A2540;letter-spacing:0.18em;text-transform:uppercase;line-height:1.4">Grupo<br>Manejo Miopía<br>LATAM</div></td>
        </tr></table>
        <div style="font-size:11px;letter-spacing:0.22em;text-transform:uppercase;color:#0077C8;font-weight:700">🔎 Búsqueda indexada · Comité Editorial</div>
        <h1 style="margin:6px 0 10px;font-size:24px;color:#0A2540;line-height:1.2;font-weight:700">Visión MML LATAM · {today}</h1>
        {intro}
        {items_html}
      </td></tr>
      <tr><td style="padding:1em 2em 2em;border-top:1px solid #E5EAF0">
        <p style="font-size:12px;color:#5A7184;line-height:1.6;margin:0">
          Generado automáticamente cada mañana a las 7:00 AM (Colombia).<br>
          <strong>Fuentes:</strong> Review of Myopia Management · Myopia Profile (Clinical + Science)<br>
          🌐 <a href="https://miopialatam.org" style="color:#0077C8">miopialatam.org</a> · ✉️ <a href="mailto:info@miopialatam.org" style="color:#0077C8">info@miopialatam.org</a>
        </p>
      </td></tr>
    </table>
  </td></tr>
</table>
</body></html>"""


def send_via_smtp(html_body: str, subject: str, password: str) -> None:
    msg = MIMEMultipart("alternative")
    msg["Subject"] = subject
    msg["From"] = f"{SENDER_NAME} <{EMAIL_FROM}>"
    msg["To"] = EMAIL_TO
    msg.attach(MIMEText(html_body, "html", "utf-8"))

    with smtplib.SMTP(SMTP_HOST, SMTP_PORT) as smtp:
        smtp.starttls()
        smtp.login(SMTP_USER, password)
        smtp.send_message(msg)


def fetch_brevo_contacts(api_key: str, list_id: int) -> list[dict]:
    contacts = []
    offset = 0
    limit = 100
    while True:
        r = requests.get(
            f"{BREVO_API_BASE}/contacts/lists/{list_id}/contacts",
            params={"limit": limit, "offset": offset},
            headers={"api-key": api_key, "accept": "application/json"},
            timeout=30,
        )
        r.raise_for_status()
        data = r.json()
        batch = data.get("contacts", [])
        for c in batch:
            attrs = c.get("attributes", {}) or {}
            contacts.append({
                "email": c["email"],
                "name": attrs.get("FIRSTNAME") or attrs.get("NOMBRE") or c["email"].split("@")[0],
            })
        if len(batch) < limit:
            break
        offset += limit
    return contacts


def send_via_brevo(html_body: str, subject: str, api_key: str, contacts: list[dict]) -> int:
    if not contacts:
        return 0
    sent = 0
    batch_size = 50
    for i in range(0, len(contacts), batch_size):
        chunk = contacts[i:i + batch_size]
        payload = {
            "sender": {"name": SENDER_NAME, "email": EMAIL_FROM},
            "subject": subject,
            "htmlContent": html_body,
            "messageVersions": [
                {"to": [{"email": c["email"], "name": c["name"]}]}
                for c in chunk
            ],
        }
        r = requests.post(
            f"{BREVO_API_BASE}/smtp/email",
            json=payload,
            headers={
                "api-key": api_key,
                "accept": "application/json",
                "content-type": "application/json",
            },
            timeout=45,
        )
        if r.status_code >= 400:
            print(f"error: Brevo send failed ({r.status_code}): {r.text[:400]}", file=sys.stderr)
            r.raise_for_status()
        sent += len(chunk)
    return sent


def main() -> int:
    print(f"[{datetime.now(timezone.utc).isoformat()}] starting digest")

    anthropic_key = os.environ.get("ANTHROPIC_API_KEY")
    brevo_key = os.environ.get("BREVO_API_KEY")
    smtp_password = os.environ.get("SMTP_PASSWORD")

    if not anthropic_key:
        print("error: ANTHROPIC_API_KEY env var missing", file=sys.stderr)
        return 1
    if not brevo_key and not smtp_password:
        print("error: need BREVO_API_KEY or SMTP_PASSWORD", file=sys.stderr)
        return 1

    state = load_state()
    bootstrap = state.get("first_run", True)
    seen = set(state.get("seen_urls", []))

    print("fetching RoMM RSS...")
    romm = fetch_romm()
    print(f"  → {len(romm)} items")

    print("fetching Myopia Profile...")
    mp = fetch_myopia_profile()
    print(f"  → {len(mp)} items")

    all_items = romm + mp
    new_items = [it for it in all_items if it["url"] not in seen]
    print(f"new items vs state: {len(new_items)} / {len(all_items)}")

    client = Anthropic(api_key=anthropic_key)
    top_for_widget = all_items[:3]
    if new_items:
        print("summarizing new items...")
        summarize(new_items, client)
    print("summarizing top-3 for home widget if needed...")
    summarize(top_for_widget, client)

    write_snapshot(top_for_widget)
    print(f"snapshot written: {SNAPSHOT_FILE}")

    if bootstrap:
        print("bootstrap run: sending welcome only")
        html = render_html([], bootstrap=True)
        subject = "📚 Digest MML activado · primer envío"
        email_articles = []
    else:
        email_articles = new_items
        html = render_html(email_articles, bootstrap=False)
        today_short = datetime.now(timezone.utc).strftime("%d %b")
        subject = f"📚 Digest MML · {len(email_articles)} novedades · {today_short}"

    sent_via = "none"
    sent_count = 0
    if brevo_key:
        print(f"fetching subscribers from Brevo list {BREVO_LIST_ID}...")
        contacts = fetch_brevo_contacts(brevo_key, BREVO_LIST_ID)
        print(f"  → {len(contacts)} subscribers")
        if contacts:
            print(f"sending via Brevo to {len(contacts)} subscribers...")
            sent_count = send_via_brevo(html, subject, brevo_key, contacts)
            sent_via = "brevo"
        else:
            print("no Brevo subscribers yet; falling back to SMTP")

    if sent_via == "none":
        if not smtp_password:
            print("error: no Brevo subscribers and no SMTP_PASSWORD", file=sys.stderr)
            return 1
        print(f"sending via SMTP to {EMAIL_TO}...")
        send_via_smtp(html, subject, smtp_password)
        sent_via = "smtp"
        sent_count = 1

    new_seen = seen | {it["url"] for it in all_items}
    state["seen_urls"] = list(new_seen)[-500:]
    state["last_run"] = datetime.now(timezone.utc).isoformat()
    state["first_run"] = False
    state["last_sent_via"] = sent_via
    state["last_recipients"] = sent_count
    save_state(state)

    n_email = 0 if bootstrap else len(email_articles)
    print(f"done. {n_email} items in email; delivered via {sent_via} to {sent_count} recipient(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
