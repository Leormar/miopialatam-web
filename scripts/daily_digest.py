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
from datetime import datetime, timedelta, timezone
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
INDEX_FILE = ROOT / "index.html"

# Marcadores dentro de #digestGrid en index.html. El script SOLO reescribe el
# contenido entre estos dos comentarios: nunca toca clases, IDs ni rutas.
DIGEST_START = "<!-- DIGEST:START -->"
DIGEST_END = "<!-- DIGEST:END -->"

ROMM_FEED = "https://reviewofmm.com/feed/"
MP_CATEGORIES = [
    ("Clinical", "https://www.myopiaprofile.com/articles/category/clinical"),
    ("Science", "https://www.myopiaprofile.com/articles/category/science"),
]
MP_BASE = "https://www.myopiaprofile.com"

# Tope de artículos a parsear por Myopia Profile (ambas categorías combinadas).
# Antes era 15 fijo y dejaba afuera novedades reales que quedaban más abajo en
# la página → digests "sin novedades" con contenido fresco disponible.
MP_MAX_ITEMS = int(os.environ.get("MP_MAX_ITEMS", "40"))
# Máximo de novedades a incluir en UN email (honra el "3-5 destacadas").
# Las que excedan se marcan como vistas igual para no repetirlas mañana.
MAX_DIGEST_ITEMS = int(os.environ.get("MAX_DIGEST_ITEMS", "6"))

SMTP_HOST = "mail.privateemail.com"
SMTP_PORT = 587
SMTP_USER = os.environ.get("SMTP_USER", "info@miopialatam.org")
EMAIL_FROM = os.environ.get("EMAIL_FROM", "info@miopialatam.org")
EMAIL_TO = os.environ.get("EMAIL_TO", "info@miopialatam.org")
SENDER_NAME = os.environ.get("SENDER_NAME", "Comité Editorial MML")

BREVO_API_BASE = "https://api.brevo.com/v3"
BREVO_LIST_ID = int(os.environ.get("BREVO_LIST_ID", "6"))

CLAUDE_MODEL = os.environ.get("CLAUDE_MODEL", "claude-haiku-4-5-20251001")

COLOMBIA_TZ = timezone(timedelta(hours=-5))

UA = "Mozilla/5.0 (compatible; MML-Digest/1.0; +https://miopialatam.org)"

CATEGORY_MAP = {
    "CLINICAL": {"color": "#2EAA4A", "label": "Control clínico", "bg_light": "#E6F7EB"},
    "PRACTICE": {"color": "#0077C8", "label": "Gestión de consultorio", "bg_light": "#EAF4FB"},
    "INDUSTRY": {"color": "#D42B2B", "label": "Industria", "bg_light": "#FDECEA"},
    "WEB": {"color": "#F5C518", "label": "Nuevos recursos", "bg_light": "#FFF8E5"},
}


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
    return items[:MP_MAX_ITEMS]


def _apply_category(art: dict, cat: str) -> None:
    cat = cat if cat in CATEGORY_MAP else "CLINICAL"
    meta = CATEGORY_MAP[cat]
    art["category"] = cat
    art["category_color"] = meta["color"]
    art["category_label"] = meta["label"]
    art["category_bg_light"] = meta["bg_light"]


def summarize(articles: list[dict], client: Anthropic) -> None:
    for art in articles:
        if art.get("summary_es"):
            continue
        prompt = (
            "Sos editor del digest diario del Comité Editorial MML LATAM "
            "(Grupo Manejo Miopía Latinoamérica).\n\n"
            "Clasificá el artículo en UNA categoría (usá EXACTAMENTE el código):\n"
            "- CLINICAL → control clínico de la miopía: atropina, ortho-k, "
            "lentes blandos, lentes oftálmicas, evidencia clínica, axial length, "
            "protocolos terapéuticos, casos clínicos, screening pediátrico\n"
            "- PRACTICE → gestión del consultorio: pricing, marketing, "
            "estrategia de práctica privada, organización, programas pagos, "
            "modelos de negocio, equipamiento\n"
            "- INDUSTRY → noticias de la industria: lanzamientos de productos "
            "de fabricantes (ZEISS, Essilor, CooperVision, HOYA), anuncios "
            "corporativos, congresos institucionales (BHVI, IMI, AAO, BCLA), "
            "regulaciones, premios, becas\n"
            "- WEB → recursos digitales nuevos: calculadoras online, sitios "
            "web, herramientas digitales, plataformas, apps\n\n"
            "Resumí en 2 líneas en español neutro LATAM (máximo 280 caracteres, "
            "tono editorial profesional, sin markdown, sin viñetas, sin saludos).\n\n"
            "Devolveme EXACTAMENTE en este formato:\n"
            "CATEGORIA: [código]\n"
            "RESUMEN: [tu resumen]\n\n"
            f"Título: {art['title']}\n"
            f"Fuente: {art['source']}\n"
            f"Texto original: {art.get('summary', '')[:600] or '(solo título disponible)'}"
        )
        try:
            response = client.messages.create(
                model=CLAUDE_MODEL,
                max_tokens=300,
                messages=[{"role": "user", "content": prompt}],
            )
            text = response.content[0].text.strip()
            cat = "CLINICAL"
            summary = text
            up = text.upper()
            cat_idx = up.find("CATEGORIA:")
            res_idx = up.find("RESUMEN:")
            if cat_idx >= 0:
                end = text.find("\n", cat_idx)
                if end < 0:
                    end = len(text)
                cat_raw = text[cat_idx + len("CATEGORIA:"):end].strip().upper()
                cat_raw = cat_raw.split()[0] if cat_raw else "CLINICAL"
                if cat_raw in CATEGORY_MAP:
                    cat = cat_raw
            if res_idx >= 0:
                summary = text[res_idx + len("RESUMEN:"):].strip()
            _apply_category(art, cat)
            art["summary_es"] = summary
        except Exception as exc:
            _apply_category(art, "CLINICAL")
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
                "category": it.get("category", "CLINICAL"),
                "category_color": it.get("category_color", "#2EAA4A"),
                "category_label": it.get("category_label", "Control clínico"),
            }
            for it in top_items[:4]
        ],
    }
    SNAPSHOT_FILE.write_text(
        json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )


def _digest_cards_html(items: list[dict]) -> str:
    """Renderiza las tarjetas del digest como HTML real, con EXACTAMENTE el
    mismo markup y clases que produce el JS del home (hb-digest-card + dg-*),
    para que el contenido quede indexable y index.html cambie a diario sin
    romper estilos. El JS sigue refrescando en vivo (mismas 3 tarjetas)."""
    import html as _html

    def _cat_class(it: dict) -> str:
        c = str(it.get("category", "")).upper()
        return {
            "PRACTICE": "dg-practice",
            "INDUSTRY": "dg-industry",
            "WEB": "dg-web",
        }.get(c, "dg-clinical")

    cards = []
    for it in items[:3]:
        cls = _cat_class(it)
        label = _html.escape(str(it.get("category_label") or "Control clínico"))
        src = _html.escape(str(it.get("source_short") or it.get("source") or ""))
        title = _html.escape(str(it.get("title") or ""))
        summary = _html.escape(str(it.get("summary_es") or ""))
        url = _html.escape(str(it.get("url") or "#"), quote=True)
        cards.append(
            f'<a class="hb-digest-card {cls}" href="{url}" target="_blank" rel="noopener">'
            f'<span class="hb-digest-card-label">{label}</span>'
            f'<div class="hb-digest-card-src">{src}</div>'
            f'<div class="hb-digest-card-title">{title}</div>'
            f'<div class="hb-digest-card-summary">{summary}</div>'
            f'<span class="hb-digest-card-cta">Leer artículo</span>'
            f'</a>'
        )
    return "\n      ".join(cards)


def inject_digest_into_index(items: list[dict]) -> None:
    """Incrusta las tarjetas del digest dentro de #digestGrid en index.html,
    SOLO entre los marcadores DIGEST:START/END. No toca nada más del archivo."""
    import re

    if not INDEX_FILE.exists():
        print("warn: index.html no encontrado; se omite la inyección")
        return
    doc = INDEX_FILE.read_text(encoding="utf-8")
    if DIGEST_START not in doc or DIGEST_END not in doc:
        print("warn: marcadores DIGEST no encontrados en index.html; se omite")
        return
    cards = _digest_cards_html(items)
    block = f"{DIGEST_START}\n      {cards}\n      {DIGEST_END}"
    new_doc = re.sub(
        re.escape(DIGEST_START) + r".*?" + re.escape(DIGEST_END),
        lambda _m: block,
        doc,
        flags=re.S,
    )
    if new_doc != doc:
        INDEX_FILE.write_text(new_doc, encoding="utf-8")
        print(f"index.html: digest incrustado en HTML real ({len(items[:4])} tarjetas)")
    else:
        print("index.html: digest sin cambios")


def render_html(articles: list[dict], bootstrap: bool, fallback: bool = False) -> str:
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
            "<p>Hoy no encontramos publicaciones nuevas. Volveremos mañana "
            "a las 7:00 AM con el próximo resumen del manejo de la miopía.</p>"
        )
        items_html = ""
    else:
        if fallback:
            intro = (
                "<p style='color:#5A7184;margin:0 0 1.4em'>Lo más reciente "
                "del manejo de la miopía a esta hora.</p>"
            )
        else:
            word = "novedad destacada" if len(articles) == 1 else "novedades destacadas"
            intro = f"<p style='color:#5A7184;margin:0 0 1.4em'>{len(articles)} {word} para hoy.</p>"
        items_html = ""
        for i, art in enumerate(articles, 1):
            cat_color = art.get('category_color', '#F5C518')
            cat_bg = art.get('category_bg_light', '#FFF8E5')
            cat_label = art.get('category_label', 'Control clínico')
            items_html += f"""
<div style="margin-bottom:1.3em;padding:1.1em 1.2em;background:{cat_bg};border-left:4px solid {cat_color};border-radius:6px">
  <div style="font-size:11px;color:{cat_color};text-transform:uppercase;letter-spacing:0.08em;font-weight:800">{cat_label} · <span style="color:#5A7184;font-weight:600">{art['source']}</span></div>
  <div style="margin:0.45em 0 0.5em;font-size:16px;font-weight:700;color:#0A2540;line-height:1.3">{i}. {art['title']}</div>
  <div style="color:#333;line-height:1.55;font-size:14px">{art.get('summary_es', '')}</div>
  <a href="{art['url']}" style="display:inline-block;margin-top:0.7em;color:{cat_color};font-size:13px;font-weight:700;text-decoration:none">Leer artículo completo →</a>
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
        <h1 style="margin:6px 0 8px;font-size:24px;color:#0A2540;line-height:1.2;font-weight:700">Visión MML LATAM · {today}</h1>
        <div style="font-size:11px;color:#5A7184;letter-spacing:0.04em;line-height:1.5;margin-bottom:4px">
          <span style="display:inline-block;width:10px;height:10px;background:#2EAA4A;border-radius:2px;vertical-align:middle;margin-right:5px"></span>Control clínico &nbsp;
          <span style="display:inline-block;width:10px;height:10px;background:#0077C8;border-radius:2px;vertical-align:middle;margin-right:5px"></span>Gestión consultorio &nbsp;
          <span style="display:inline-block;width:10px;height:10px;background:#D42B2B;border-radius:2px;vertical-align:middle;margin-right:5px"></span>Industria &nbsp;
          <span style="display:inline-block;width:10px;height:10px;background:#F5C518;border-radius:2px;vertical-align:middle;margin-right:5px"></span>Nuevos recursos
        </div>
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
    from email.utils import formataddr
    from email.header import Header
    msg = MIMEMultipart("alternative")
    msg["Subject"] = Header(subject, "utf-8")
    msg["From"] = formataddr((str(Header(SENDER_NAME, "utf-8")), EMAIL_FROM))
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


def pick_one_per_category(items: list[dict], max_count: int = 4) -> list[dict]:
    """Selecciona 1 item por cada categoría disponible, en el orden:
    Verde clínico → Azul gestión → Rojo industria → Amarillo recursos.
    Rellena con cualquier item adicional hasta max_count si quedan slots.
    """
    order = ["CLINICAL", "PRACTICE", "INDUSTRY", "WEB"]
    picked_urls: set[str] = set()
    result: list[dict] = []
    for cat in order:
        for it in items:
            if it.get("category") == cat and it["url"] not in picked_urls:
                result.append(it)
                picked_urls.add(it["url"])
                break
        if len(result) >= max_count:
            break
    if len(result) < max_count:
        for it in items:
            if len(result) >= max_count:
                break
            if it["url"] not in picked_urls:
                result.append(it)
                picked_urls.add(it["url"])
    return result[:max_count]


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

    # Candado de idempotencia: un solo email por día (hora Colombia).
    # Aunque el cron de respaldo y el disparador externo coincidan, no se
    # duplica. FORCE_SEND=1 fuerza el envío (útil para pruebas manuales).
    today_co = datetime.now(COLOMBIA_TZ).strftime("%Y-%m-%d")
    force_send = os.environ.get("FORCE_SEND", "").strip().lower() in ("1", "true", "yes")
    already_sent_today = state.get("last_sent_date") == today_co
    if already_sent_today and not force_send:
        print(f"idempotency guard: ya se envió hoy ({today_co}); se actualiza el "
              "snapshot pero se omite el email. Usá FORCE_SEND=1 para forzar.")

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
    if new_items:
        print(f"summarizing {len(new_items)} new items...")
        summarize(new_items, client)
    pool_for_widget = all_items[:12]
    print(f"summarizing top-{len(pool_for_widget)} pool for widget categorization...")
    summarize(pool_for_widget, client)
    top_for_widget = pick_one_per_category(pool_for_widget, max_count=4)
    print(f"widget selection: {len(top_for_widget)} items ({', '.join(it.get('category', '?') for it in top_for_widget)})")

    write_snapshot(top_for_widget)
    print(f"snapshot written: {SNAPSHOT_FILE}")

    inject_digest_into_index(top_for_widget)

    if bootstrap:
        print("bootstrap run: sending welcome only")
        html = render_html([], bootstrap=True)
        subject = "📚 Digest MML activado · primer envío"
        email_articles = []
    else:
        # Honra el "3-5 destacadas": si hay un backlog grande, se envían las
        # primeras MAX_DIGEST_ITEMS (las más recientes); el resto se marca
        # como visto igual (más abajo) para no repetirlas.
        email_articles = new_items[:MAX_DIGEST_ITEMS]
        if len(new_items) > MAX_DIGEST_ITEMS:
            print(f"backlog: {len(new_items)} nuevos; se envían {len(email_articles)} "
                  f"(MAX_DIGEST_ITEMS={MAX_DIGEST_ITEMS}), el resto se marca como visto")
        # Si no hay novedades nuevas, igual enviamos lo más reciente de las
        # fuentes (las mismas tarjetas del home) para que el correo SIEMPRE
        # traiga info actualizada, aunque se repita respecto a días previos.
        fallback_mode = not email_articles
        if fallback_mode:
            email_articles = top_for_widget
            print(f"sin novedades nuevas; fallback a lo más reciente: "
                  f"{len(email_articles)} items")
        html = render_html(email_articles, bootstrap=False, fallback=fallback_mode)
        today_short = datetime.now(timezone.utc).strftime("%d %b")
        if fallback_mode:
            subject = f"📚 Digest MML · Lo más reciente · {today_short}"
        else:
            subject = f"📚 Digest MML · {len(email_articles)} novedades · {today_short}"

    sent_via = "none"
    sent_count = 0
    if already_sent_today and not force_send:
        sent_via = "skipped-already-sent"
    elif brevo_key:
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
            print("warn: no Brevo subscribers and no SMTP_PASSWORD; skipping email")
        else:
            print(f"sending via SMTP to {EMAIL_TO}...")
            try:
                send_via_smtp(html, subject, smtp_password)
                sent_via = "smtp"
                sent_count = 1
            except Exception as exc:
                print(f"warn: SMTP send failed: {exc}", file=sys.stderr)
                sent_via = "smtp-failed"

    # Marcar el día como enviado solo si realmente salió el email.
    if sent_via in ("brevo", "smtp"):
        state["last_sent_date"] = today_co

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
