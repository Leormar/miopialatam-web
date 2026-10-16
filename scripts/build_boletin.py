#!/usr/bin/env python3
"""Genera boletin-edNN.html a partir de scripts/boletin_content.py usando
boletin-ed01.html como plantilla visual, y actualiza el repositorio en
boletin.html (entre los marcadores ISSUES:START / ISSUES:END).

Uso:  python3 scripts/build_boletin.py
"""
import html
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
from boletin_content import EDITIONS  # noqa: E402

TPL = (ROOT / "boletin-ed01.html").read_text(encoding="utf-8")
HEAD, rest = TPL.split('<section class="cover">', 1)
_, TAIL = rest.split('<section class="next-issue">', 1)
TAIL = '<section class="next-issue">' + TAIL
FOOTER = TAIL[TAIL.index("<footer>"):]

COLORS = [("#0077C8", "rgba(0,119,200,0.08)"), ("#2EAA4A", "rgba(46,170,74,0.08)"), ("#D42B2B", "rgba(212,43,43,0.07)")]
TIP_COLORS = ["#0077C8", "#2EAA4A", "#D42B2B"]

EXTRA_CSS = """
/* SUBSTACK / AUDIO BOX (ed. 02+) */
.substack-box{display:flex;align-items:center;justify-content:space-between;gap:1rem;flex-wrap:wrap;background:linear-gradient(135deg,#EAF4FB 0%,#F6FAFD 100%);border:1px solid #CFE3F2;border-radius:18px;padding:1.3rem 1.5rem;margin:0 0 3.5rem}
.substack-box-text{font-size:0.92rem;color:var(--txt);line-height:1.55;max-width:470px}
.substack-box-text strong{color:var(--ink)}
.substack-box-k{font-family:'Barlow Condensed',sans-serif;font-weight:800;font-size:0.74rem;letter-spacing:0.2em;text-transform:uppercase;color:#0077C8;margin-bottom:0.3rem;display:flex;align-items:center;gap:8px}
.substack-box-k svg{width:16px;height:16px}
.substack-btn{display:inline-flex;align-items:center;gap:8px;padding:0.8rem 1.4rem;border-radius:999px;background:linear-gradient(135deg,#0A2540,#0077C8);color:#fff;text-decoration:none;font-weight:700;font-size:0.88rem}
.ed-nav{display:flex;justify-content:space-between;gap:1rem;flex-wrap:wrap;margin:2rem 0 0}
.ed-nav a{font-size:0.86rem;font-weight:600;color:var(--az);text-decoration:none}
@media print{.substack-box,.ed-nav{display:none !important}}
"""

HEADPHONES = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 18v-6a9 9 0 0 1 18 0v6"/><path d="M21 19a2 2 0 0 1-2 2h-1a2 2 0 0 1-2-2v-3a2 2 0 0 1 2-2h3zM3 19a2 2 0 0 0 2 2h1a2 2 0 0 0 2-2v-3a2 2 0 0 0-2-2H3z"/></svg>'


def strip_tags(s):
    return re.sub(r"<[^>]+>", "", s)


def build_head(e):
    title = f"Visión MML LATAM · Edición {e['num']} — {strip_tags(e['card_title'])}"
    h = HEAD
    h = re.sub(r"<title>.*?</title>", f"<title>{html.escape(title)}</title>", h, count=1)
    h = re.sub(r'(<meta name="description" content=")[^"]*', r"\g<1>" + html.escape(e["deck"]), h, count=1)
    h = h.replace("https://miopialatam.org/boletin-ed01.html", f"https://miopialatam.org/{e['slug']}")
    h = re.sub(r'(<meta property="og:title" content=")[^"]*', r"\g<1>" + html.escape(title), h, count=1)
    h = re.sub(r'(<meta property="og:description" content=")[^"]*', r"\g<1>" + html.escape(e["deck"]), h, count=1)
    h = h.replace("Visión MML LATAM · Edición 01 · Mayo 2026", f"Visión MML LATAM · Edición {e['num']} · {e['month']}")
    h = h.replace("</style>", EXTRA_CSS + "</style>", 1)
    return h


def section_html(i, s):
    c, cb = COLORS[i]
    out = [f'  <section class="section" id="seccion-{i+1}" style="--c:{c};--cb:{cb}">',
           f'    <div class="sec-kicker">{i+1:02d} · {s["kicker"]}</div>',
           f'    <h2 class="sec-title">{s["title"]}</h2>',
           f'    <p class="sec-deck">{s["deck"]}</p>']
    if s.get("tips"):
        out.append('    <div class="tip-grid">')
        for j, (t, x) in enumerate(s["tips"]):
            out.append(f'      <div class="tip-card" style="--c:{TIP_COLORS[j]}"><div class="tip-num">{j+1:02d}</div>'
                       f'<div class="tip-title">{t}</div><div class="tip-text">{x}</div></div>')
        out.append('    </div>')
    style = ' style="margin-top:1.4rem"' if s.get("tips") else ""
    out.append(f'    <div class="sec-body"{style}>')
    out.append(s.get("body", "").strip())
    if s.get("callout"):
        ct, cx = s["callout"]
        out.append(f'      <div class="callout"><div class="callout-title">{ct}</div><div class="callout-text">{cx}</div></div>')
    if s.get("refs"):
        out.append('      <div class="references"><h4>Referencias</h4><ol>')
        out += [f"        <li>{r}</li>" for r in s["refs"]]
        out.append('      </ol></div>')
    out.append('    </div>\n  </section>\n')
    return "\n".join(out)


def build_page(idx, e):
    prev_e = EDITIONS[idx - 1] if idx > 0 else {"slug": "boletin-ed01.html", "num": "01"}
    next_e = EDITIONS[idx + 1] if idx + 1 < len(EDITIONS) else None
    toc_kickers = [s["kicker"] for s in e["sections"]]
    toc = "\n".join(
        f'      <a class="toc-item" href="#seccion-{i+1}"><div class="toc-num">{i+1:02d}</div>'
        f'<div class="toc-info"><div class="toc-kicker">{toc_kickers[i]}</div><div class="toc-name">{n}</div></div></a>'
        for i, n in enumerate(e["toc"]))
    editorial = "\n".join(f"    <p>{p}</p>" for p in e["editorial"])
    sections = "\n".join(section_html(i, s) for i, s in enumerate(e["sections"]))
    ed_inline = TPL[TPL.index("  <!-- COMITÉ EDITORIAL INLINE -->"):TPL.index('  <div class="actions-bar">')]
    actions = TPL[TPL.index('  <div class="actions-bar">'):TPL.index("</article>")]
    nav_links = f'<a href="{prev_e["slug"]}">&larr; Edición {prev_e["num"]}</a>'
    nav_links += f'<a href="{next_e["slug"]}">Edición {next_e["num"]} &rarr;</a>' if next_e else '<a href="boletin.html">Ver todas las ediciones &rarr;</a>'

    body = f"""<section class="cover">
  <div class="cover-stripe">
    <div style="background:#F5C518"></div>
    <div style="background:#2EAA4A"></div>
    <div style="background:#0077C8"></div>
    <div style="background:#D42B2B"></div>
  </div>
  <div class="cover-inner">
    <div>
      <div class="vmml-logo">
        <div class="vmml-eyebrow">Newsletter</div>
        <div class="vmml-title">
          <span class="vmml-vision">Visión</span>
          <span class="vmml-letters"><span class="m1">M</span><span class="m2">M</span><span class="l">L</span></span>
        </div>
        <div class="vmml-locale">LATAM</div>
      </div>
      <div class="issue-tag">Edición {e['num']} · {e['month']}</div>
      <h1 class="cover-title">{e['cover_title']}</h1>
      <p class="cover-deck">{e['deck']}</p>
      <div class="cover-meta">
        <span>Publicado <strong>{e['date']}</strong></span>
        <span>Lectura <strong>{e['read']}</strong></span>
        <span>Idioma <strong>Español</strong></span>
      </div>
      <div class="cover-actions">
        <button class="cover-btn primary" onclick="window.print()">Descargar PDF</button>
        <a class="cover-btn ghost" href="boletin.html">Ver repositorio</a>
      </div>
    </div>
    <aside class="cover-toc">
      <div class="cover-toc-title">En esta edición</div>
      <a class="toc-item" href="#editorial"><div class="toc-num">00</div><div class="toc-info"><div class="toc-kicker">Carta editorial</div><div class="toc-name">Comité Editorial MML</div></div></a>
{toc}
    </aside>
  </div>
</section>

<article class="article">

  <section class="editorial-letter" id="editorial">
    <h2>{e['editorial_h']}</h2>
{editorial}
    <div class="editorial-signature">— Comité Editorial Visión MML LATAM<br><small>Edgar Davila García · David P. Piñero · Elise G. Kramer · Ricardo Pintor L. · Ariolfo Vazquez · Leonardo Orjuela M.</small></div>
  </section>

  <div class="substack-box">
    <div class="substack-box-text"><div class="substack-box-k">{HEADPHONES} Versión completa y narrada</div>Esta edición resume el artículo publicado en <strong>VISION MML</strong>, nuestro boletín en Substack, donde puede leerlo completo con figuras y escucharlo narrado.</div>
    <a class="substack-btn" href="{e['substack']}" target="_blank" rel="noopener">Leer y escuchar en Substack</a>
  </div>

{sections}
{ed_inline}{actions}  <p style="font-size:0.8rem;color:#8B9DAA;line-height:1.5">Este contenido es educativo y no reemplaza una valoración visual individual.</p>
  <div class="ed-nav">{nav_links}</div>

</article>

<section class="next-issue">
  <h3>Reciba cada edición en su correo</h3>
  <p>Suscríbase para recibir <strong>Visión MML LATAM</strong> directamente en su bandeja de entrada.</p>
  <div class="next-actions">
    <a href="boletin.html#suscribirme" class="next-btn primary">Suscribirme al newsletter</a>
    <a href="boletin.html" class="next-btn ghost">Ver repositorio</a>
  </div>
</section>

"""
    return build_head(e) + body + FOOTER


def issue_card(e):
    return f"""    <a href="{e['slug']}" class="issue">
      <div class="issue-cover">
        <div class="issue-num">Edición {e['num']} · {e['month']}</div>
        <div class="issue-cover-title">{e['card_title']}</div>
      </div>
      <div class="issue-content">
        <div class="issue-date">Publicado {e['date_short']}</div>
        <div class="issue-title">{e['issue_title']}</div>
        <div class="issue-desc">{e['card_desc']}</div>
        <div class="issue-cta">Leer edición</div>
      </div>
    </a>
"""


ED01_CARD = """    <a href="boletin-ed01.html" class="issue">
      <div class="issue-cover">
        <div class="issue-num">Edición 01 · Mayo 2026</div>
        <div class="issue-cover-title">El primer paso para una red regional</div>
      </div>
      <div class="issue-content">
        <div class="issue-date">Publicado 22 mayo 2026</div>
        <div class="issue-title">Hacia un consenso LATAM en control de miopía</div>
        <div class="issue-desc">Editorial de los fundadores · prevalencia regional · selección de tratamiento por perfil de paciente · futuro de la red MML.</div>
        <div class="issue-cta">Leer edición</div>
      </div>
    </a>
"""


def update_repo_page():
    p = ROOT / "boletin.html"
    s = p.read_text(encoding="utf-8")
    cards = "".join(issue_card(e) for e in reversed(EDITIONS)) + ED01_CARD
    block = "<!-- ISSUES:START -->\n" + cards + "    <!-- ISSUES:END -->"
    if "<!-- ISSUES:START -->" in s:
        s = re.sub(r"<!-- ISSUES:START -->.*?<!-- ISSUES:END -->", lambda m: block, s, flags=re.S)
    else:
        start = s.index('  <div class="issues">') + len('  <div class="issues">')
        end = s.index("  </div>\n</div>\n\n<section class=\"editorial-sec\">")
        s = s[:start] + "\n    " + block + "\n\n" + s[end:]
    p.write_text(s, encoding="utf-8")


if __name__ == "__main__":
    for i, e in enumerate(EDITIONS):
        (ROOT / e["slug"]).write_text(build_page(i, e), encoding="utf-8")
        print("ok", e["slug"])
    update_repo_page()
    print("ok boletin.html")
