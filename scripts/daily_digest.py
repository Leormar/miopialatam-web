#!/usr/bin/env python3
"""Digest editorial diario MML LATAM.

Fuentes:
- Review of Myopia Management (RSS)
- Myopia Profile (scraping clinical + science)

Resume cada artículo nuevo con Claude y envía un correo a info@miopialatam.org.
Pensado para correr en GitHub Actions todos los días a las 7:00 AM Colombia (12:00 UTC).
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
                "title": title,
                "url": href,
                "summary": "",
                "published": "",
            })
    return items[:15]


def summarize(articles: list[dict], client: Anthropic) -> None:
    for art in articles:
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
        intro = f"<p style='color:#5A7184;margin:0 0 1.4em'>{len(articles)} novedades para el skim diario.</p>"
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
      <tr><td style="height:6px;background:#F5C518"></td></tr>
      <tr><td style="padding:2em 2em 1.2em">
        <div style="font-size:11px;letter-spacing:0.2em;text-transform:uppercase;color:#0077C8;font-weight:700">Comité Editorial · MML LATAM</div>
        <h1 style="margin:0.3em 0 0.15em;font-size:24px;color:#0A2540">Digest diario · {today}</h1>
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


def send_email(html_body: str, subject: str, password: str) -> None:
    msg = MIMEMultipart("alternative")
    msg["Subject"] = subject
    msg["From"] = f"Comité Editorial MML <{EMAIL_FROM}>"
    msg["To"] = EMAIL_TO
    msg.attach(MIMEText(html_body, "html", "utf-8"))

    with smtplib.SMTP(SMTP_HOST, SMTP_PORT) as smtp:
        smtp.starttls()
        smtp.login(SMTP_USER, password)
        smtp.send_message(msg)


def main() -> int:
    print(f"[{datetime.now(timezone.utc).isoformat()}] starting digest")

    smtp_password = os.environ.get("SMTP_PASSWORD")
    anthropic_key = os.environ.get("ANTHROPIC_API_KEY")
    if not smtp_password:
        print("error: SMTP_PASSWORD env var missing", file=sys.stderr)
        return 1
    if not anthropic_key:
        print("error: ANTHROPIC_API_KEY env var missing", file=sys.stderr)
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

    if bootstrap:
        print("bootstrap run: marking all as seen, sending welcome email")
        html = render_html([], bootstrap=True)
        subject = "📚 Digest MML activado · primer envío"
    else:
        if new_items:
            print("summarizing with Claude...")
            client = Anthropic(api_key=anthropic_key)
            summarize(new_items, client)
        html = render_html(new_items, bootstrap=False)
        today_short = datetime.now(timezone.utc).strftime("%d %b")
        subject = f"📚 Digest MML · {len(new_items)} novedades · {today_short}"

    print(f"sending email to {EMAIL_TO}...")
    send_email(html, subject, smtp_password)

    new_seen = seen | {it["url"] for it in all_items}
    state["seen_urls"] = list(new_seen)[-500:]
    state["last_run"] = datetime.now(timezone.utc).isoformat()
    state["first_run"] = False
    save_state(state)

    sent_count = 0 if bootstrap else len(new_items)
    print(f"done. sent {sent_count} new items.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
