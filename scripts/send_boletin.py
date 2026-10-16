#!/usr/bin/env python3
"""Envía ediciones de Visión MML LATAM por correo a los suscriptores (Brevo).

Reutiliza los mismos secrets del digest diario (BREVO_API_KEY, BREVO_LIST_ID,
SMTP_PASSWORD). Se ejecuta desde .github/workflows/send-boletin.yml.

Variables:
  EDITION    "10" (una edición) o "resumen" (un solo correo con 02-10)
  MODE       "prueba" -> solo a EMAIL_TEST (default info@miopialatam.org)
             "suscriptores" -> a toda la lista de Brevo
  FORCE_SEND "1" para reenviar una edición ya enviada a suscriptores
"""
import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
from boletin_content import EDITIONS  # noqa: E402
from daily_digest import (  # noqa: E402
    BREVO_LIST_ID, fetch_brevo_contacts, send_via_brevo, send_via_smtp,
)

SITE = "https://miopialatam.org"
STATE = ROOT / "state" / "boletin_sent.json"
EMAIL_TEST = os.environ.get("EMAIL_TEST", "info@miopialatam.org")
COURSE = os.environ.get("INCLUDE_COURSE", "1") == "1"
HOTMART = "https://pay.hotmart.com/Y108020169L?off=fga3eto3"

STRIPES = ('<table role="presentation" width="100%" cellpadding="0" cellspacing="0"><tr>'
           '<td height="5" style="background:#F5C518"></td><td height="5" style="background:#2EAA4A"></td>'
           '<td height="5" style="background:#0077C8"></td><td height="5" style="background:#D42B2B"></td></tr></table>')


def strip(s):
    import re
    return re.sub(r"<[^>]+>", "", s).replace("<br>", " ")


def header():
    return f"""<tr><td>{STRIPES}</td></tr>
<tr><td style="background:#0A2540;padding:28px 32px;color:#fff;font-family:Georgia,serif">
  <div style="font-family:Arial,sans-serif;font-size:11px;letter-spacing:4px;text-transform:uppercase;color:#C9D6E2">Newsletter</div>
  <div style="font-size:32px;font-weight:bold;font-style:italic;line-height:1.1">Visión <span style="color:#F5C518">M</span><span style="color:#2EAA4A">M</span><span style="color:#7AB6E0">L</span> <span style="font-family:Arial,sans-serif;font-style:normal;font-size:12px;letter-spacing:4px;background:#9C2A35;padding:3px 10px;border-radius:99px;vertical-align:middle">LATAM</span></div>
</td></tr>"""


def btn(href, text, bg="#0077C8", fg="#ffffff"):
    return (f'<a href="{href}" style="display:inline-block;background:{bg};color:{fg};text-decoration:none;'
            f'font-family:Arial,sans-serif;font-weight:bold;font-size:14px;padding:12px 22px;border-radius:999px;margin:4px 6px 4px 0">{text}</a>')


def course_block():
    if not COURSE:
        return ""
    return f"""<tr><td style="padding:0 32px 28px">
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="background:#FFF6D8;border-left:4px solid #F5C518;border-radius:0 12px 12px 0"><tr><td style="padding:18px 20px;font-family:Arial,sans-serif;color:#3C2E00">
<div style="font-size:11px;letter-spacing:3px;text-transform:uppercase;font-weight:bold;color:#5C4400">Curso en vivo · inicia 3 nov 2026</div>
<div style="font-size:20px;font-weight:bold;color:#0A2540;margin:6px 0">Miopía de cerca</div>
<div style="font-size:14px;line-height:1.55">5 clases en vivo con 10 especialistas de 9 países, embajadores del Grupo Manejo Miopía LATAM. Martes y jueves 7:00 p.m. hora Bogotá. Preventa USD 97 hasta el 27 de octubre.</div>
<div style="margin-top:10px">{btn(SITE + '/curso-miopia-de-cerca.html', 'Ver programa', '#0A2540')}{btn(HOTMART, 'Inscribirme', '#F5C518', '#0A2540')}</div>
</td></tr></table></td></tr>"""


def footer():
    return f"""<tr><td style="background:#F5F8FB;padding:22px 32px;font-family:Arial,sans-serif;font-size:12px;color:#5A7184;line-height:1.6">
Grupo Manejo Miopía LATAM · <a href="{SITE}" style="color:#0077C8">miopialatam.org</a> · <a href="mailto:info@miopialatam.org" style="color:#0077C8">info@miopialatam.org</a><br>
Recibe este correo porque se suscribió al newsletter Visión MML LATAM. Para darse de baja, responda a este correo con la palabra BAJA.<br>
Contenido educativo; no reemplaza una valoración visual individual.
</td></tr>"""


def wrap(rows):
    return f"""<!DOCTYPE html><html lang="es"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1"></head>
<body style="margin:0;background:#EEF2F6">
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="background:#EEF2F6"><tr><td align="center" style="padding:24px 10px">
<table role="presentation" width="600" cellpadding="0" cellspacing="0" style="max-width:600px;width:100%;background:#ffffff;border-radius:16px;overflow:hidden">
{rows}
</table></td></tr></table></body></html>"""


def edition_email(e):
    url = f"{SITE}/{e['slug']}"
    secs = "".join(
        f'<tr><td style="padding:0 32px 16px;font-family:Arial,sans-serif">'
        f'<div style="font-size:11px;letter-spacing:3px;text-transform:uppercase;font-weight:bold;color:{c}">{i+1:02d} · {s["kicker"]}</div>'
        f'<div style="font-family:Georgia,serif;font-size:19px;font-weight:bold;color:#0A2540;margin:4px 0">{strip(s["title"])}</div>'
        f'<div style="font-size:14px;color:#5A7184;line-height:1.55">{strip(s["deck"])}</div></td></tr>'
        for i, (s, c) in enumerate(zip(e["sections"], ["#0077C8", "#2EAA4A", "#D42B2B"])))
    rows = header() + f"""
<tr><td style="padding:28px 32px 8px;font-family:Arial,sans-serif">
  <div style="display:inline-block;font-size:11px;letter-spacing:3px;text-transform:uppercase;font-weight:bold;color:#92690A;background:#FFF6D8;padding:5px 12px;border-radius:99px">Edición {e['num']} · {e['month']}</div>
  <h1 style="font-family:Georgia,serif;font-style:italic;font-size:30px;line-height:1.15;color:#0A2540;margin:14px 0 10px">{strip(e['cover_title'])}</h1>
  <p style="font-size:16px;color:#1A3347;line-height:1.6;margin:0 0 14px">{e['deck']}</p>
  <p style="font-size:15px;color:#1A3347;line-height:1.7;margin:0 0 18px;border-left:3px solid #0077C8;padding-left:14px">{e['editorial'][0]}</p>
  <div style="margin-bottom:22px">{btn(url, 'Leer la edición completa', '#0A2540')}{btn(e['substack'], 'Escuchar en Substack')}</div>
  <div style="font-size:11px;letter-spacing:3px;text-transform:uppercase;font-weight:bold;color:#8B9DAA;margin-bottom:12px">En esta edición</div>
</td></tr>
{secs}
<tr><td style="padding:6px 32px 26px">{btn(url, 'Ir a la edición', '#0077C8')}</td></tr>
{course_block()}
{footer()}"""
    subject = f"Visión MML LATAM · Ed. {e['num']}: {strip(e['card_title'])}"
    return subject, wrap(rows)


def summary_email(eds):
    items = "".join(
        f'<tr><td style="padding:0 32px 14px;font-family:Arial,sans-serif">'
        f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="border:1px solid #E5EAEF;border-radius:12px"><tr><td style="padding:14px 16px">'
        f'<div style="font-size:11px;letter-spacing:2px;text-transform:uppercase;font-weight:bold;color:#0077C8">Edición {e["num"]} · {e["date_short"]}</div>'
        f'<div style="font-family:Georgia,serif;font-size:18px;font-weight:bold;color:#0A2540;margin:4px 0">{strip(e["card_title"])}</div>'
        f'<div style="font-size:13px;color:#5A7184;line-height:1.5;margin-bottom:8px">{e["card_desc"]}</div>'
        f'<a href="{SITE}/{e["slug"]}" style="font-size:13px;font-weight:bold;color:#0077C8;text-decoration:none">Leer edición &rarr;</a> &nbsp; '
        f'<a href="{e["substack"]}" style="font-size:13px;color:#5A7184">Escuchar</a>'
        f'</td></tr></table></td></tr>' for e in eds)
    rows = header() + f"""
<tr><td style="padding:28px 32px 14px;font-family:Arial,sans-serif">
  <h1 style="font-family:Georgia,serif;font-style:italic;font-size:28px;line-height:1.15;color:#0A2540;margin:0 0 10px">{len(eds)} nuevas ediciones de Visión MML LATAM</h1>
  <p style="font-size:15px;color:#1A3347;line-height:1.65;margin:0">Durante octubre publicamos una edición por cada artículo de la red: lentes de contacto en ARVO 2026, atropina, gafas de control, ortoqueratología, calculadoras e inteligencia artificial, economía de la salud y premiopía. Cada una tiene versión web, PDF descargable y narración en audio.</p>
</td></tr>
{items}
<tr><td style="padding:6px 32px 26px">{btn(SITE + '/boletin.html', 'Ver el repositorio completo', '#0A2540')}</td></tr>
{course_block()}
{footer()}"""
    return f"Visión MML LATAM · {len(eds)} nuevas ediciones de octubre", wrap(rows)


def main():
    edition = os.environ.get("EDITION", "").strip().lower()
    mode = os.environ.get("MODE", "prueba").strip().lower()
    force = os.environ.get("FORCE_SEND", "").strip().lower() in ("1", "true", "yes")
    if edition in ("resumen", "todas", "all"):
        key, eds = "resumen-oct-2026", EDITIONS
        subject, html_body = summary_email(eds)
    else:
        edition = edition.zfill(2)
        match = [e for e in EDITIONS if e["num"] == edition]
        if not match:
            sys.exit(f"error: edición '{edition}' no existe. Opciones: {[e['num'] for e in EDITIONS]} o 'resumen'")
        key = f"ed{edition}"
        subject, html_body = edition_email(match[0])

    (ROOT / "data").mkdir(exist_ok=True)
    (ROOT / "data" / f"email-{key}.html").write_text(html_body, encoding="utf-8")
    print(f"asunto: {subject}")

    state = json.loads(STATE.read_text()) if STATE.exists() else {"sent": {}}
    brevo_key = os.environ.get("BREVO_API_KEY")

    if mode != "suscriptores":
        test = [{"email": EMAIL_TEST, "name": "Prueba MML"}]
        if brevo_key:
            send_via_brevo(html_body, "[PRUEBA] " + subject, brevo_key, test)
        else:
            send_via_smtp(html_body, "[PRUEBA] " + subject, os.environ["SMTP_PASSWORD"])
        print(f"prueba enviada a {EMAIL_TEST}")
        return

    if key in state["sent"] and not force:
        print(f"'{key}' ya se envió el {state['sent'][key]['at']} a {state['sent'][key]['count']} suscriptores. Use FORCE_SEND para reenviar.")
        return
    if not brevo_key:
        sys.exit("error: BREVO_API_KEY es necesario para enviar a suscriptores")
    contacts = fetch_brevo_contacts(brevo_key, BREVO_LIST_ID)
    print(f"{len(contacts)} suscriptores en la lista {BREVO_LIST_ID}")
    n = send_via_brevo(html_body, subject, brevo_key, contacts)
    state["sent"][key] = {"at": datetime.now(timezone.utc).isoformat(timespec="seconds"), "count": n}
    STATE.write_text(json.dumps(state, indent=2, ensure_ascii=False))
    print(f"enviado a {n} suscriptores")


if __name__ == "__main__":
    main()
