#!/usr/bin/env python3
"""Genera curso-miopia-de-cerca.html (curso en vivo con embajadores MML)
usando la plantilla visual de boletin-ed01.html."""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TPL = (ROOT / "boletin-ed01.html").read_text(encoding="utf-8")
HEAD = TPL.split('<section class="cover">', 1)[0]
FOOTER = TPL[TPL.index("<footer>"):]

HOTMART = "https://pay.hotmart.com/Y108020169L?off=fga3eto3"
WHATSAPP = "https://wa.me/573183753210"
TITLE = "Curso en vivo Miopía de cerca · 3 nov 2026 · MML"
DESC = "Curso en vivo de control y manejo de la miopía con los embajadores del Grupo Manejo Miopía LATAM: 5 clases, 10 especialistas de 9 países, inicia el 3 de noviembre de 2026."

head = HEAD
head = re.sub(r"<title>.*?</title>", f"<title>{TITLE}</title>", head, count=1)
head = re.sub(r'(<meta name="description" content=")[^"]*', r"\g<1>" + DESC, head, count=1)
head = head.replace("https://miopialatam.org/boletin-ed01.html", "https://miopialatam.org/curso-miopia-de-cerca.html")
head = re.sub(r'(<meta property="og:title" content=")[^"]*', r"\g<1>" + TITLE, head, count=1)
head = re.sub(r'(<meta property="og:description" content=")[^"]*', r"\g<1>" + DESC, head, count=1)
head = head.replace("https://miopialatam.org/logo-mml.png\">\n<meta property=\"og:site_name\"",
                    "https://miopialatam.org/img/curso/miopia-de-cerca-flyer.jpg\">\n<meta property=\"og:site_name\"")
head = head.replace('<a href="eventos.html">Eventos</a>', '<a href="eventos.html" class="active">Eventos</a>')
head = head.replace('<a href="boletin.html" class="active">Boletin</a>', '<a href="boletin.html">Boletin</a>')
head = head.replace('<a href="boletin.html" class="btn-primary">Repositorio</a>', f'<a href="{HOTMART}" target="_blank" rel="noopener" class="btn-primary">Inscribirme</a>')
head = head.replace("Visión MML LATAM · Edición 01 · Mayo 2026", "Curso Miopía de cerca · MML")

CSS = """
/* CURSO */
.c-hero{background:linear-gradient(135deg,#0A2540 0%,#102E50 55%,#0077C8 100%);color:#fff;padding:4rem 2rem 4.5rem;position:relative;overflow:hidden}
.c-hero-inner{max-width:1100px;margin:0 auto;display:grid;grid-template-columns:1.15fr 1fr;gap:3rem;align-items:center;position:relative;z-index:2}
.c-hero::before{content:'';position:absolute;inset:0;background-image:radial-gradient(circle at 1px 1px,rgba(255,255,255,0.06) 1px,transparent 0);background-size:28px 28px}
.c-logos{display:flex;align-items:center;gap:1.4rem;margin-bottom:1.4rem;flex-wrap:wrap}
.c-logos img{height:46px;width:auto}
.c-logos small{font-family:'Barlow Condensed',sans-serif;font-weight:700;letter-spacing:0.16em;text-transform:uppercase;font-size:0.72rem;color:#F5C518}
.c-eyebrow{font-family:'Barlow Condensed',sans-serif;font-weight:800;letter-spacing:0.24em;text-transform:uppercase;font-size:0.85rem;color:#F5C518;margin-bottom:0.6rem}
.c-title{font-family:'Barlow Condensed',sans-serif;font-weight:900;font-size:clamp(2.8rem,6vw,4.6rem);line-height:0.95;text-transform:uppercase;letter-spacing:-0.01em}
.c-title span{display:inline-block;background:#F5C518;color:#0A2540;padding:0 0.35em;border-radius:999px;margin-top:0.15em}
.c-tag{font-family:'Playfair Display',serif;font-style:italic;font-size:1.35rem;margin:1rem 0 1.2rem;color:rgba(255,255,255,0.9)}
.c-tag em{color:#F5C518}
.c-facts{display:flex;flex-wrap:wrap;gap:0.5rem;margin-bottom:1.6rem}
.c-fact{background:rgba(255,255,255,0.1);border:1px solid rgba(255,255,255,0.2);border-radius:999px;padding:0.45rem 0.9rem;font-size:0.84rem;font-weight:600}
.c-flyer{width:100%;max-width:440px;border-radius:22px;box-shadow:0 20px 60px rgba(0,0,0,0.35);justify-self:center;display:block}
.c-cta{display:flex;gap:0.7rem;flex-wrap:wrap}
@media(max-width:900px){.c-hero-inner{grid-template-columns:1fr}.c-flyer{max-width:360px}}
.price{background:linear-gradient(135deg,#FFF6D8 0%,#FFFCEB 100%);border:1px solid #F5C518;border-radius:20px;padding:1.6rem 1.4rem;text-align:center;margin:0 0 3.5rem}
.price-main{font-family:'Barlow Condensed',sans-serif;font-weight:800;font-size:1.5rem;text-transform:uppercase;color:#0A2540}
.price-main strong{color:#D42B2B;font-size:2.1rem}
.price-sub{font-size:0.9rem;color:#5C4400;margin:0.3rem 0 1rem}
.prog{width:100%;border-collapse:collapse;font-size:0.9rem;margin:1rem 0}
.prog th{background:#0A2540;color:#fff;text-align:left;padding:0.7rem;font-family:'Barlow Condensed',sans-serif;letter-spacing:0.08em;text-transform:uppercase;font-size:0.8rem}
.prog td{border-bottom:1px solid var(--bd);padding:0.8rem 0.7rem;vertical-align:top;line-height:1.5}
.prog td:first-child{font-family:'Barlow Condensed',sans-serif;font-weight:800;font-size:1.3rem;color:#0077C8}
.prog tr:nth-child(even) td{background:#FAFBFC}
@media(max-width:640px){.prog,.prog tbody,.prog tr,.prog td{display:block;width:100%}.prog thead{display:none}.prog tr{border:1px solid var(--bd);border-radius:12px;margin-bottom:0.8rem;overflow:hidden}.prog td{border:none;padding:0.4rem 0.9rem}}
.fmt{display:grid;grid-template-columns:repeat(3,1fr);gap:1rem;margin:1rem 0}
.fmt div{background:#F5F8FB;border-radius:14px;padding:1.1rem;text-align:center}
.fmt strong{display:block;font-family:'Barlow Condensed',sans-serif;font-weight:800;font-size:1.7rem;color:#0077C8}
.fmt span{font-size:0.84rem;color:var(--mu)}
@media(max-width:640px){.fmt{grid-template-columns:1fr}}
.docs{display:grid;grid-template-columns:1fr 1fr;gap:1rem;margin-top:1.2rem}
.doc{display:flex;gap:0.9rem;background:#fff;border:1px solid var(--bd);border-radius:16px;padding:1rem}
.doc img{width:72px;height:72px;border-radius:50%;object-fit:cover;flex-shrink:0}
.doc-name{font-family:'Barlow Condensed',sans-serif;font-weight:800;font-size:1.02rem;text-transform:uppercase;color:var(--ink);line-height:1.1}
.doc-meta{font-size:0.74rem;font-weight:700;color:#D42B2B;text-transform:uppercase;letter-spacing:0.04em;margin:0.2rem 0 0.35rem}
.doc-bio{font-size:0.83rem;color:var(--mu);line-height:1.5}
@media(max-width:720px){.docs{grid-template-columns:1fr}}
.faq dt{font-weight:700;color:var(--ink);margin-top:1rem}
.faq dd{color:var(--txt);line-height:1.65}
.final{background:linear-gradient(135deg,#0A2540,#0077C8);border-radius:24px;color:#fff;text-align:center;padding:2.4rem 1.5rem;margin:3rem 0 1rem}
.final h3{font-family:'Barlow Condensed',sans-serif;font-weight:900;font-size:2.2rem;text-transform:uppercase}
.final p{color:rgba(255,255,255,0.85);margin:0.4rem 0 1.3rem}
.final a.ghost-w{color:#fff;font-weight:600}
"""
head = head.replace("</style>", CSS + "</style>", 1)

DOCENTES = [
 ("edgar-davila", "Dr. Edgar Dávila-García, OD, FIACLE, FSLS, NCLE-AC", "Clase 1 · Puerto Rico", "Director científico de TheEye-Herd. Doctor en Optometría (U. Interamericana de Puerto Rico). Conferencista en 26 países, autor de un libro de lentes de contacto especializados. Miembro fundador del Grupo Manejo de la Miopía LATAM y Embajador IMI para Latinoamérica."),
 ("angel-macedo", "Optom. Ángel Macedo Mariano", "Clase 1 · Perú", "Embajador IMI para Perú, presidente del Gremio de Optómetras y Ópticas del Perú (GOOP) y vocal para Suramérica de ALDOO. CEO de la Clínica de Oftalmología Pediátrica Visage Kids."),
 ("francisco-perez", "Mtro. Francisco Pérez Robles", "Clase 2 · México", "Maestro en Diagnóstico y Terapéutica Visual. Práctica con énfasis pediátrico y línea de trabajo en neuro-optometría. Miembro de COMOF, NEURAR, CODEC y CLIO."),
 ("suelen-abril", "Lic. Suelen Abril Cruz, SCSIODERV", "Clase 2 · Perú · Invitada especial", "MBA y Máster en Visión y Deporte (U. Complutense de Madrid). Directora clínica del Centro Internacional Estereopik (Lima) y docente de posgrado en Perú y Brasil."),
 ("ariolfo-vazquez", "Dr. Ariolfo G. Vázquez, OD, FIACLE, FSLS", "Clase 3 · Ecuador", "Cofundador del Grupo Manejo de la Miopía LATAM. Jefe de Contactología y Optometría de la Clínica Oftalmolaser y director del Centro Visual Optocentro (Cuenca)."),
 ("hector-paez", "Héctor Hugo Páez Villa, Opt. Esp.", "Clase 3 · Colombia", "Especialista en Segmento Anterior y Lentes de Contacto. Embajador para Colombia del Grupo MML, vicepresidente de CLIO y docente de Clínica de Refracción en la Universidad CES."),
 ("roberto-villanueva", "Lic. Roberto Villanueva Carvajal", "Clase 4 · Chile", "Contactólogo especialista en ortoqueratología, control de miopía y queratocono, acreditado por el BHVI. Representante para Chile del Grupo MML."),
 ("julio-martinez", "Dr. Julio Roberto Martínez Amador", "Clase 4 · Honduras", "Médico y cirujano, licenciado y magíster en Optometría Clínica y Terapia Visual (U. Galileo). Integra la práctica médica y optométrica con la ultrasonografía ocular."),
 ("jairo-soberanis", "M.Sc. Jairo David Soberanis Hernández", "Clase 5 · Guatemala", "Experto internacional en control de miopía, orto-K y lentes esclerales. Coordinador de Optometría en la U. Galileo (Huehuetenango) y embajador en Guatemala del Grupo MML."),
 ("cinthya-armijo", "Lic. Cinthya Armijo de López", "Clase 5 · El Salvador", "Presidenta de la Asociación Salvadoreña de Optometristas (ASOP) y embajadora para El Salvador del Grupo MML. Conferencista para el Ministerio de Salud de El Salvador."),
]
docs = "\n".join(f'      <div class="doc"><img src="img/curso/{s}.jpg" alt="{n}" loading="lazy"><div><div class="doc-name">{n}</div><div class="doc-meta">{m}</div><div class="doc-bio">{b}</div></div></div>' for s, n, m, b in DOCENTES)

BODY = f"""<section class="c-hero">
  <div class="c-hero-inner">
    <div>
      <div class="c-logos"><img src="img/curso/theeyeherd-logo.png" alt="TheEye-Herd"><small>Con el respaldo de</small><img src="img/curso/boston-logo.png" alt="Boston Materials"></div>
      <div class="c-eyebrow">Curso en vivo · Control y manejo de la miopía</div>
      <h1 class="c-title">Miopía<br><span>de cerca</span></h1>
      <p class="c-tag">Más allá de la corrección, <em>el futuro es el control.</em></p>
      <div class="c-facts">
        <div class="c-fact">5 clases en vivo</div>
        <div class="c-fact">10 especialistas de 9 países</div>
        <div class="c-fact">Inicia martes 3 nov 2026</div>
        <div class="c-fact">Mar y jue · 7:00 p.m. Bogotá</div>
      </div>
      <div class="c-cta">
        <a class="cover-btn primary" href="{HOTMART}" target="_blank" rel="noopener">Inscribirme · USD 97</a>
        <a class="cover-btn ghost" href="{WHATSAPP}" target="_blank" rel="noopener">Escribir por WhatsApp</a>
      </div>
    </div>
    <img class="c-flyer" src="img/curso/miopia-de-cerca-flyer.jpg" alt="Curso Miopía de cerca, inicia el 3 de noviembre de 2026">
  </div>
</section>

<article class="article">

  <div class="price">
    <div class="price-main">Preventa: <strong>USD 97</strong> hasta el 27 de octubre</div>
    <div class="price-sub">Precio regular desde el 28 de octubre: USD 127 · Ahorra USD 30 inscribiéndote antes · Pago único</div>
    <a class="cover-btn primary" href="{HOTMART}" target="_blank" rel="noopener">Inscríbete aquí</a>
  </div>

  <section class="section" style="--c:#0077C8;--cb:rgba(0,119,200,0.08)">
    <div class="sec-kicker">El curso</div>
    <h2 class="sec-title">La miopía ya no se corrige: <em>se controla</em></h2>
    <div class="sec-body">
      <p>Durante décadas, el éxito con el paciente miope se medía en una sola cifra: 20/20. Hoy esa respuesta se queda corta. Cada dioptría que avanza en un niño es riesgo acumulado para toda su vida, y la familia ya no pregunta solo “¿qué graduación tiene?”, sino “¿se puede frenar?”.</p>
      <p>Se estima que para 2050 cerca de la mitad de la población mundial —unos 4.758 millones de personas— será miope, y alrededor de 938 millones tendrán miopía alta (Holden et al., <em>Ophthalmology</em>, 2016).</p>
      <p>Este curso, construido con los <strong>embajadores y fundadores del Grupo Manejo Miopía LATAM</strong>, va de las definiciones al protocolo, y del protocolo a cada intervención con evidencia: ortoqueratología, lentes de contacto blandos, lentes oftálmicos, atropina y opciones emergentes.</p>
      <h3 style="font-family:'Barlow Condensed',sans-serif;text-transform:uppercase;color:var(--ink);margin:1.4rem 0 0.6rem">Qué vas a dominar</h3>
      <ul>
        <li><strong>Las bases y definiciones</strong> actuales del control y manejo de la miopía, con un lenguaje clínico común.</li>
        <li><strong>Un protocolo de examinación básica</strong> para el paciente con miopía en progresión, aplicable desde tu próxima consulta.</li>
        <li><strong>El papel de la visión binocular</strong> en la evaluación y el seguimiento del paciente miope.</li>
        <li><strong>Ortoqueratología y lentes de contacto blandos</strong> como estrategias de control: cuándo, a quién y cómo.</li>
        <li><strong>Lentes oftálmicos de control y atropina</strong>: indicaciones, combinación y manejo de expectativas con la familia.</li>
        <li><strong>Las intervenciones emergentes</strong> que están llegando a la consulta y cómo evaluarlas con criterio.</li>
      </ul>
    </div>
  </section>

  <section class="section" style="--c:#2EAA4A;--cb:rgba(46,170,74,0.08)">
    <div class="sec-kicker">Formato y programa</div>
    <h2 class="sec-title">110 minutos <em>que rinden</em></h2>
    <div class="fmt">
      <div><strong>40 + 40 min</strong><span>Dos conferencias por clase, cada una con un especialista distinto.</span></div>
      <div><strong>30 min</strong><span>Panel clínico con 3 instructores: los 2 conferencistas + un embajador MML.</span></div>
      <div><strong>110 min</strong><span>Duración total de cada sesión.</span></div>
    </div>
    <p style="font-size:0.85rem;color:var(--mu);margin-top:1rem"><strong>Martes y jueves · 7:00 p.m. hora Bogotá · en vivo</strong> (6:00 p.m. Ciudad de México y Guatemala · 7:00 p.m. Lima · 9:00 p.m. Santiago y Buenos Aires)</p>
    <table class="prog">
      <thead><tr><th>#</th><th>Clase</th><th>Fecha</th><th>Docentes</th></tr></thead>
      <tbody>
        <tr><td>1</td><td>Bases y definiciones del control y manejo de la miopía</td><td>Mar 3 nov</td><td>Dr. Edgar Dávila-García, OD<br>Optom. Ángel Macedo Mariano</td></tr>
        <tr><td>2</td><td>Protocolo de examinación básica en el control de la miopía / Importancia de la visión binocular</td><td>Jue 5 nov</td><td>Mtro. Francisco Pérez Robles<br>Lic. Suelen Abril Cruz (invitada especial)</td></tr>
        <tr><td>3</td><td>Intervenciones I: Ortoqueratología y lentes de contacto blandos para el control de la miopía</td><td>Mar 10 nov</td><td>Dr. Ariolfo G. Vázquez, OD<br>Héctor Hugo Páez Villa, Esp.</td></tr>
        <tr><td>4</td><td>Intervenciones II: Lentes oftálmicos para el control de la miopía y atropina</td><td>Jue 12 nov</td><td>Lic. Roberto Villanueva Carvajal<br>Dr. Julio Roberto Martínez Amador</td></tr>
        <tr><td>5</td><td>Intervenciones emergentes para el control y manejo de la miopía + panel final</td><td>Mar 17 nov</td><td>M.Sc. Jairo David Soberanis Hernández<br>Lic. Cinthya Armijo de López<br>+ Embajadores MML</td></tr>
      </tbody>
    </table>
  </section>

  <section class="section" style="--c:#D42B2B;--cb:rgba(212,43,43,0.07)">
    <div class="sec-kicker">Tus docentes</div>
    <h2 class="sec-title">10 especialistas, <em>9 países</em></h2>
    <p class="sec-deck">Todos los conferencistas y panelistas son embajadores o fundadores del Grupo Manejo Miopía LATAM, salvo invitados especiales.</p>
    <div class="docs">
{docs}
    </div>
  </section>

  <section class="section" style="--c:#0077C8;--cb:rgba(0,119,200,0.08)">
    <div class="sec-kicker">Inscripción</div>
    <h2 class="sec-title">Qué incluye <em>y para quién es</em></h2>
    <div class="sec-body">
      <ul>
        <li><strong>5 clases en vivo</strong> con 2 especialistas por sesión y panel clínico de 30 minutos.</li>
        <li><strong>Grabaciones de todas las sesiones</strong> para repasar a tu ritmo.</li>
        <li><strong>Preguntas en tiempo real</strong> a los embajadores MML durante cada panel.</li>
        <li><strong>Examen de evaluación y certificado</strong> emitido por TheEye-Herd, con dirección científica del Dr. Edgar Dávila.</li>
        <li><strong>Acceso a la comunidad de especialistas</strong> por WhatsApp.</li>
      </ul>
      <div class="callout"><div class="callout-title">¿Para quién es?</div><div class="callout-text">Optometristas y contactólogos que ya corrigen miopía y quieren ofrecer control con protocolo y evidencia; especialistas en optometría pediátrica; oftalmólogos y equipos de salud visual; profesionales de LATAM que buscan formación de alto nivel, en español y en vivo.</div></div>
      <h3 style="font-family:'Barlow Condensed',sans-serif;text-transform:uppercase;color:var(--ink);margin:1.4rem 0 0.2rem">Preguntas frecuentes</h3>
      <dl class="faq">
        <dt>¿Y si no puedo conectarme en vivo?</dt><dd>Todas las clases quedan grabadas y disponibles para verlas cuando quieras.</dd>
        <dt>¿Cuánto cuesta?</dt><dd>USD 97 en preventa hasta el 27 de octubre. Desde el 28 de octubre, el precio regular es USD 127. Pago único.</dd>
        <dt>¿Recibo certificado?</dt><dd>Sí. Al aprobar el examen recibes el certificado de TheEye-Herd con dirección científica del Dr. Edgar Dávila.</dd>
        <dt>¿Cómo accedo al curso?</dt><dd>El curso se hospeda en Hotmart. Al inscribirte recibes el acceso y la invitación a la comunidad de WhatsApp.</dd>
      </dl>
    </div>
  </section>

  <div class="final">
    <h3>Miopía de cerca</h3>
    <p>Preventa USD 97 hasta el 27 de octubre · después USD 127 · inicia el 3 de noviembre</p>
    <a class="cover-btn primary" href="{HOTMART}" target="_blank" rel="noopener">Inscríbete aquí</a>
    <p style="margin-top:1rem;font-size:0.9rem">o escríbenos por <a class="ghost-w" href="{WHATSAPP}" target="_blank" rel="noopener">WhatsApp</a></p>
  </div>
  <p style="font-size:0.78rem;color:#8B9DAA;text-align:center">Organiza TheEye-Herd (theeyeherd.com) con el respaldo de Boston Materials, junto a los embajadores del Grupo Manejo Miopía LATAM.</p>

</article>

"""

(ROOT / "curso-miopia-de-cerca.html").write_text(head + BODY + FOOTER, encoding="utf-8")
print("ok curso-miopia-de-cerca.html")
