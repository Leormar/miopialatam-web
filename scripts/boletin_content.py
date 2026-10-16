# -*- coding: utf-8 -*-
"""Contenido editorial de las ediciones 02-10 de Visión MML LATAM.
Cada edición se construye a partir de un post de VISION MML (Substack).
Generado con scripts/build_boletin.py
"""

EDITIONS = [
# ---------------------------------------------------------------- ED 02
{
"num": "02", "date": "2 de octubre de 2026", "date_short": "2 oct 2026", "month": "Octubre 2026",
"slug": "boletin-ed02.html", "read": "~ 7 min",
"substack": "https://grupomiopialatam.substack.com/p/arvo-2026-lo-que-dicen-los-nuevos",
"cover_title": "ARVO 2026:<br>lentes de contacto que frenan",
"card_title": "ARVO 2026: lentes de contacto que frenan",
"issue_title": "Lo nuevo en lentes de contacto para control de miopía",
"deck": "Cuatro estudios, cuatro estrategias —desechable diario, EDOF, curva catenaria y ortoqueratología— y lo que significan para la consulta en Latinoamérica.",
"card_desc": "Abiliti 1-Day a 24 meses · EDOF a 5 años · PROTECT con NaturalVue · orto-K en 14.000 niños de Tianjin.",
"toc": ["Cuatro estudios de ARVO 2026", "Lo que nos llevamos a la consulta", "Leer con criterio"],
"editorial_h": "Del congreso a la consulta",
"editorial": [
"Cada mayo, la reunión anual de ARVO concentra lo más reciente de la investigación en visión. La edición 2026 se celebró en Denver y dejó un mensaje claro para quienes trabajamos con lentes de contacto: <strong>el control de la miopía ya tiene datos a tres y cinco años</strong>, y dejó de ser una promesa de corto plazo.",
"En esta edición revisamos cuatro trabajos presentados en el congreso, a partir del resumen publicado por Myopia Profile, y les sumamos nuestra lectura clínica: qué cambia en la consulta y qué conviene leer con prudencia.",
],
"sections": [
{"kicker": "Evidencia", "title": "Cuatro estudios, <em>cuatro estrategias</em>",
 "deck": "Lentes diarias, diseños EDOF esféricos y tóricos, curva catenaria y ortoqueratología en la práctica real.",
 "body": """
<p><strong>1. Abiliti 1-Day a 24 meses en niños chinos.</strong> Estudio prospectivo de un solo brazo: 60 niños de 7 a 12 años con lentes diarias frente a 42 controles “del mundo real” con gafas monofocales. Elongación axial de 0,23 mm frente a 0,50 mm y progresión de −0,56 D frente a −1,16 D, sin eventos adversos reportados.</p>
<p><strong>2. Lentes EDOF de mark’ennovy.</strong> El grupo español de Díaz-Gómez, De Gracia y Carballo presentó datos en niños caucásicos. Con lentes esféricas a 5 años (47 niños frente a 51 con gafas), la reducción acumulada fue de 0,91 D y 0,61 mm. Con tóricas a 3 años (8 frente a 8 niños astigmáticos), de 0,85 D y 0,49 mm.</p>
<p><strong>3. PROTECT: curva catenaria (NaturalVue) a 2 años.</strong> Ensayo multicéntrico, doble ciego y controlado en EE. UU., Canadá, Hong Kong y Singapur con 145 niños de 8 a 12 años. Diferencia de 0,59 D y 0,22 mm frente a la lente monofocal. Además, identificó como factores de riesgo la edad, el inicio antes de los 8 años, la longitud axial basal, los antecedentes familiares, el país y el tiempo al aire libre.</p>
<p><strong>4. Ortoqueratología en 14.752 niños de Tianjin.</strong> Análisis retrospectivo con 9 diseños distintos. La elongación disminuye con la edad y se estabiliza después de los 15 años; los diseños personalizados mostraron la menor elongación anual, y los niños que pasaron de gafas de control a orto-K bajaron de 0,311 a 0,171 mm/año.</p>
""",
 "callout": ("Lectura MML", "El seguimiento a 5 años con EDOF es de lo más valioso de esta edición: confirma que el efecto se sostiene en el tiempo. El dato tórico es muy relevante para nuestra región, donde el astigmatismo asociado es frecuente, aunque con 16 niños debe tomarse como señal preliminar."),
 "refs": ["Peng B. ARVO 2026 Recap #1: What’s new in myopia control with contact lenses. Myopia Profile, 1 de junio de 2026. myopiaprofile.com/articles/recap-1-ARVO-2026"]},
{"kicker": "Práctica clínica", "title": "Lo que nos llevamos <em>a la consulta</em>",
 "deck": "Cinco ideas prácticas para el especialista en lentes de contacto.",
 "tips": [("El efecto se sostiene", "Con datos a 3 y 5 años, el control con lentes de contacto deja de ser una promesa de corto plazo."),
          ("El niño astigmático cuenta", "Ya existen opciones tóricas con datos. No hay que dejarlo fuera del control."),
          ("Medir en milímetros", "Todos los estudios reportan longitud axial. La refracción sola se queda corta para seguir al paciente.")],
 "body": """
<p>A esas tres ideas sumamos dos más. <strong>Estratificar el riesgo desde la primera consulta</strong>: edad de inicio, antecedentes familiares y tiempo al aire libre deben quedar registrados, como sugiere el análisis de PROTECT. Y <strong>elegir bien el diseño</strong>: en ortoqueratología, la personalización mostró menor elongación anual en la cohorte de Tianjin.</p>
""",
 "callout": None, "refs": []},
{"kicker": "Futuro LATAM", "title": "Leer <em>con criterio</em>",
 "deck": "Datos de congreso útiles, pero no equivalentes entre sí.",
 "body": """
<p>Varios de estos trabajos son patrocinados por la industria, no aleatorizados o con muestras pequeñas. La cohorte de Tianjin es enorme, pero retrospectiva y con posible sesgo de selección, así que las comparaciones entre marcas deben leerse con prudencia. Los datos de congreso, además, pueden cambiar en su publicación final.</p>
<p>Para la red queda una pregunta abierta: <strong>¿qué opciones de lentes de contacto para control de miopía están disponibles hoy en cada país, y cuál es la barrera principal: costo, acceso o adherencia?</strong> Conocer ese mapa es el primer paso para recomendaciones regionales realistas.</p>
""",
 "callout": ("Llamado a la red", "Cuéntenos qué lentes de control tiene disponibles en su país y qué frena su uso. Escríbanos a <strong>info@miopialatam.org</strong>."),
 "refs": []},
]},
# ---------------------------------------------------------------- ED 03
{
"num": "03", "date": "3 de octubre de 2026", "date_short": "3 oct 2026", "month": "Octubre 2026",
"slug": "boletin-ed03.html", "read": "~ 7 min",
"substack": "https://grupomiopialatam.substack.com/p/su-hijo-no-solo-necesita-gafas-necesita",
"cover_title": "No solo gafas:<br>un plan",
"card_title": "No solo gafas: un plan",
"issue_title": "Cómo hablar de miopía con los padres",
"deck": "Por qué tantas familias dicen “por ahora solo las gafas” frente a la miopía, y cómo podemos explicarla mejor.",
"card_desc": "La miopía que no se siente · cada dioptría cuenta · de explicar a acompañar en la consulta.",
"toc": ["Por qué la miopía no se siente", "De explicar a acompañar", "Lo que pueden hacer los padres"],
"editorial_h": "La conversación también es tratamiento",
"editorial": [
"Es una escena que se repite: un niño de 7 años con −1,50 D, padres miopes, buenas preguntas… y al final, con una sonrisa amable, “por ahora solo las gafas”. El Dr. Michael Dittman la describió en Review of Myopia Management, y muchos colegas de la red nos sentimos identificados.",
"En esta edición proponemos mirar esa escena de otra forma. La evidencia no basta si no logramos que la familia entienda <strong>qué significa el diagnóstico</strong>. Las gafas corrigen la visión de hoy; el manejo de la miopía protege la de los próximos 50 años.",
],
"sections": [
{"kicker": "Evidencia", "title": "La miopía <em>no se siente</em> como una enfermedad",
 "deck": "El niño se pone las gafas y ve bien. Lo que no se ve es que el ojo sigue creciendo.",
 "body": """
<p>En la miopía infantil el ojo crece de más: aumenta la <strong>longitud axial</strong>, el largo del ojo de adelante hacia atrás. Las gafas convencionales corrigen el desenfoque, pero no frenan ese crecimiento. Con los años, un ojo más largo aumenta el riesgo de desprendimiento de retina, maculopatía miópica, glaucoma y catarata temprana.</p>
<ul>
<li><strong>El problema crece:</strong> para 2050 cerca de la mitad de la población mundial será miope, unos 4.758 millones de personas, y cerca de 1.000 millones tendrán miopía alta [1].</li>
<li><strong>Empezar temprano pesa:</strong> en Singapur, cuanto más temprano apareció la miopía, mayor fue el riesgo de llegar a miopía alta [2].</li>
<li><strong>Cada dioptría cuenta:</strong> frenar la miopía en una sola dioptría reduce en torno a un 40 % el riesgo de maculopatía miópica [3].</li>
<li><strong>Hay herramientas que funcionan:</strong> en un ensayo de dos años, las gafas DIMS redujeron la progresión en torno al 52 % y el alargamiento del ojo en torno al 62 % [4]. La ortoqueratología, los lentes de contacto de control y la atropina en baja dosis también tienen respaldo.</li>
</ul>
<p>Hoy existen además curvas de crecimiento de la longitud axial por edad, parecidas a las tablas de peso y talla del pediatra, que permiten ubicar a cada niño frente a sus pares [5].</p>
""",
 "callout": ("Un mensaje que confunde", "Si un especialista formula gafas sin decir nada y otro habla de tratamiento, controles y costos, la familia entiende que el control es un “extra”. La coherencia del mensaje entre profesionales también es parte del manejo."),
 "refs": ["Holden BA, et al. Global prevalence of myopia and high myopia and temporal trends from 2000 through 2050. Ophthalmology. 2016;123(5):1036-42.",
          "Chua SY, et al. Age of onset of myopia predicts risk of high myopia in later childhood in myopic Singapore children. Ophthalmic Physiol Opt. 2016;36(4):388-94.",
          "Bullimore MA, Brennan NA. Myopia control: why each diopter matters. Optom Vis Sci. 2019;96(6):463-5.",
          "Lam CSY, et al. DIMS spectacle lenses slow myopia progression: a 2-year randomised clinical trial. Br J Ophthalmol. 2020;104(3):363-8.",
          "Tideman JWL, et al. Axial length growth and the risk of developing myopia in European children. Acta Ophthalmol. 2018;96(3):301-9.",
          "Dittman M. How to communicate with parents who “just want glasses”. Review of Myopia Management, 28 de septiembre de 2026."]},
{"kicker": "Práctica clínica", "title": "De explicar <em>a acompañar</em>",
 "deck": "Saber la ciencia es indispensable, pero no basta. Lo que más ayuda es cambiar la forma de hablar con los padres.",
 "tips": [("Preguntar antes de explicar", "“¿Qué ha notado en la visión de su hijo?” Mete a la familia en la conversación desde el inicio."),
          ("Mostrar datos, no discursos", "Ver en una gráfica dónde está su hijo frente a niños de su edad vuelve concreto el futuro."),
          ("Respetar los tiempos", "No todos deciden ese día. Un resumen escrito y seguimiento valen más que una decisión presionada.")],
 "body": """
<p>Validar lo que los padres observaron (“tenía razón, hoy lo confirmamos”) los convierte en parte del equipo. Y mostrar qué cambia con el tratamiento es el momento en que muchas familias dejan de ver la miopía como una incomodidad y empiezan a verla como algo que se puede prevenir.</p>
""",
 "callout": ("Para colegas", "La medición de la longitud axial es la herramienta de comunicación más poderosa que tenemos. Un número que se grafica y se compara en cada control convence más que cualquier explicación."),
 "refs": []},
{"kicker": "Para familias", "title": "Lo que pueden hacer <em>los padres</em>",
 "deck": "Cinco recomendaciones para compartir en consulta.",
 "body": """
<ul>
<li><strong>Preguntar por la longitud axial</strong>, no solo por la fórmula de las gafas.</li>
<li><strong>Tomar en serio la miopía temprana</strong>, sobre todo si aparece antes de los 8 años o si los padres son miopes.</li>
<li><strong>Sacar a los niños al aire libre todos los días.</strong> Es una de las medidas de prevención con mejor respaldo.</li>
<li><strong>Pedir que les expliquen las opciones de control</strong>, con su evidencia, ventajas y límites, y decidir con información.</li>
<li><strong>Cumplir los controles.</strong> Un tratamiento de miopía se evalúa con mediciones en el tiempo.</li>
</ul>
""",
 "callout": None, "refs": []},
]},
# ---------------------------------------------------------------- ED 04
{
"num": "04", "date": "5 de octubre de 2026", "date_short": "5 oct 2026", "month": "Octubre 2026",
"slug": "boletin-ed04.html", "read": "~ 8 min",
"substack": "https://grupomiopialatam.substack.com/p/donde-actua-la-atropina-lo-que-dicen",
"cover_title": "¿Dónde actúa<br>la atropina?",
"card_title": "¿Dónde actúa la atropina?",
"issue_title": "Lo que dicen 30 años de datos",
"deck": "Siete estudios, del laboratorio a los ensayos clínicos con niños, para responder una pregunta que llega a la consulta casi todas las semanas.",
"card_desc": "La hipótesis acomodativa que se cayó · retina, coroides y esclera · dosis y respuesta en LAMP y CHAMP.",
"toc": ["Retina, coroides y esclera", "Dosis y respuesta", "Para los padres"],
"editorial_h": "Un tratamiento que funciona por razones que aún estudiamos",
"editorial": [
"“Doctor, si las gotas dilatan la pupila, ¿no le van a dañar la vista a mi hijo?” La atropina lleva más de un siglo en oftalmología como medicamento para dilatar, y muchas familias la conocen así. Por eso la primera duda no suele ser si funciona, sino qué le hace al ojo.",
"En esta edición organizamos la evidencia por niveles —animales, retina y coroides de niños, ensayos clínicos— y llegamos a una conclusión doble: el mecanismo sigue abierto, pero <strong>la atropina funciona, depende de la dosis y hay que medir la respuesta en cada niño</strong>.",
],
"sections": [
{"kicker": "Evidencia", "title": "Retina, coroides y esclera: <em>dónde actúa</em>",
 "deck": "La explicación clásica decía que la atropina frena la miopía porque paraliza la acomodación. Los datos la desmontaron.",
 "body": """
<p><strong>La hipótesis que se cayó.</strong> En 1993, en pollitos —cuyo músculo de enfoque no responde a la atropina— el medicamento igual redujo el crecimiento del ojo [1]. Si funciona sin tocar el enfoque, el efecto viene de otro lado.</p>
<p><strong>La retina.</strong> En cobayas con miopía inducida, la atropina al 0,01 % y al 1 % redujo la miopía según la dosis. La respuesta de los fotorreceptores no cambió, pero la onda b fotópica del electrorretinograma aumentó a partir de la sexta semana [2]. En 61 niños de 7 a 10 años, la actividad retiniana basal se relacionó de forma opuesta con el crecimiento del ojo en tratados y no tratados [3]: la retina de cada niño podría influir en si la gota le sirve.</p>
<p><strong>La coroides.</strong> En el seguimiento a dos años de LAMP, la coroides se engrosó unas 21 micras con 0,05 %, unas 3 con 0,025 % y prácticamente nada con 0,01 %. Más engrosamiento se asoció con menos progresión, pero explicó solo cerca del 15 % del efecto [4].</p>
<p><strong>La esclera.</strong> Revisiones recientes proponen que la atropina mejora la circulación coroidea, reduce la hipoxia escleral y frena la remodelación del tejido [7]. Es una hipótesis bien fundamentada, aún no demostrada en niños.</p>
""",
 "callout": ("Lectura MML", "La coroides participa, pero no lo explica todo. El efecto de la atropina parece repartirse entre varias capas del ojo, y aparece con el tiempo, no de inmediato."),
 "refs": ["McBrien NA, et al. Atropine reduces experimental myopia and eye enlargement via a nonaccommodative mechanism. Invest Ophthalmol Vis Sci. 1993;34(1):205-15.",
          "Wang Y, et al. Electroretinogram response changes in a guinea pig myopia model treated with different concentrations of atropine. Biochem Biophys Res Commun. 2026.",
          "Chan HHL, et al. Efficacy of 0.01% atropine for myopia control depends on baseline electroretinal response. Sci Rep. 2022;12:11588.",
          "Yam JC, et al. The association of choroidal thickening by atropine with treatment effects for myopia: two-year LAMP study. Am J Ophthalmol. 2022;237:130-8.",
          "Yam JC, et al. Low-Concentration Atropine for Myopia Progression (LAMP) Study. Ophthalmology. 2019;126(1):113-24.",
          "Zadnik K, et al. Efficacy and safety of 0.01% and 0.02% atropine over 3 years (CHAMP). JAMA Ophthalmol. 2023;141(10):990-9.",
          "Huang L, et al. The role of atropine in myopia control: insights into choroidal and scleral mechanisms. Front Pharmacol. 2025;16:1509196."]},
{"kicker": "Práctica clínica", "title": "Dosis y respuesta: <em>lo que importa</em>",
 "deck": "Los ensayos clínicos son los que guían las decisiones, y aquí los datos son consistentes.",
 "body": """
<p>En <strong>LAMP</strong>, al primer año, la miopía avanzó 0,27 D con 0,05 %, 0,46 D con 0,025 %, 0,59 D con 0,01 % y 0,81 D con placebo. La longitud axial creció 0,20 mm con la dosis más alta frente a 0,41 mm con placebo [5]. En <strong>CHAMP</strong>, a tres años, respondió bien el 28,5 % de los niños con 0,01 %, frente al 17,5 % con placebo [6].</p>
<p>El patrón es coherente: las dosis más altas mueven más la coroides, la retina y la longitud axial; las más bajas hacen menos y su efecto varía más entre niños.</p>
""",
 "tips": [("La concentración se elige", "Según edad, velocidad de progresión y longitud axial, ajustando por tolerancia (fotofobia, visión cercana)."),
          ("Control con biometría", "La fórmula por sí sola no dice si el ojo sigue creciendo. Se mide el largo del ojo en cada control."),
          ("Sin respuesta, otra estrategia", "Subir la concentración o combinar con gafas de desenfoque, orto-K o lentes multifocales.")],
 "callout": ("Buenas prácticas MML", "El electrorretinograma y la tomografía de coroides son herramientas de investigación prometedoras, pero hoy no son exámenes de rutina para decidir la atropina."),
 "refs": []},
{"kicker": "Para familias", "title": "Cinco claves <em>para los padres</em>",
 "deck": "Lo que conviene saber antes y durante el tratamiento con atropina.",
 "body": """
<ul>
<li><strong>Pregunten qué concentración</strong> usa su hijo y por qué.</li>
<li><strong>Pidan que se mida la longitud axial</strong> al inicio y cada 6 meses.</li>
<li><strong>Apliquen la gota todas las noches:</strong> la constancia pesa tanto como la dosis.</li>
<li><strong>No suspendan por su cuenta;</strong> el retiro se planea con el especialista.</li>
<li><strong>Mantengan al menos dos horas al aire libre</strong> al día, que también protegen.</li>
</ul>
""",
 "callout": None, "refs": []},
]},
# ---------------------------------------------------------------- ED 05
{
"num": "05", "date": "7 de octubre de 2026", "date_short": "7 oct 2026", "month": "Octubre 2026",
"slug": "boletin-ed05.html", "read": "~ 9 min",
"substack": "https://grupomiopialatam.substack.com/p/gafas-que-frenan-la-miopia-que-dice",
"cover_title": "Gafas que<br>frenan la miopía",
"card_title": "Gafas que frenan la miopía",
"issue_title": "Qué dice la evidencia y quién las aprobó",
"deck": "Microlentes, desenfoque y puntos difusores: ensayos clínicos, aprobaciones en EE. UU., Europa, Canadá y China, y recomendaciones para colegas y padres.",
"card_desc": "DIMS, HAL y DOT · ensayos y metaanálisis · autorización FDA de 2025 · perlas de adaptación.",
"toc": ["Tres ideas ópticas, cuatro ensayos", "El mapa regulatorio", "Perlas para colegas y padres"],
"editorial_h": "De promesa a tratamiento",
"editorial": [
"Hace cinco años, cuando una familia preguntaba si existían gafas que frenaran la miopía, la respuesta tenía muchos matices. Hoy es más clara: existen, funcionan y ya tienen respaldo regulatorio, aunque no todas son iguales ni tienen la misma evidencia.",
"En septiembre de 2025 la FDA autorizó por primera vez unas gafas para frenar la miopía infantil. En esta edición ordenamos lo que sabemos: <strong>cómo funcionan, cuánto frenan, quién las aprobó y qué hace falta para que funcionen en la vida real</strong>.",
],
"sections": [
{"kicker": "Evidencia", "title": "Tres ideas ópticas, <em>cuatro ensayos</em>",
 "deck": "Todas comparten una zona central limpia y una periferia de tratamiento. Lo que cambia es la señal que envían a la retina.",
 "body": """
<ul>
<li><strong>DIMS (MiyoSmart):</strong> segmentos de +3,50 D en panal que crean desenfoque miópico periférico. Lam 2020, 160 niños de 8–13 años, 2 años: 52 % menos progresión refractiva y 62 % menos elongación axial [1].</li>
<li><strong>HAL (Stellest):</strong> anillos de microlentes asféricas. Bao 2022, 157 niños, 2 años: 55 % y 50 %, que suben a 67 % y 60 % con 12 horas o más de uso diario [2].</li>
<li><strong>DOT (SightGlass):</strong> puntos que difunden la luz y reducen el contraste periférico. CYPRESS, 256 niños de 6–10 años, 1 año: 74 % y 50 % [3]; CATHAY a 2 años: 67 % y 62 %.</li>
</ul>
<p>El seguimiento a seis años de DIMS mostró una progresión media de 0,15 D por año con uso continuo, sin pérdida de efecto ni rebote al suspender [4]. En los metaanálisis, HAL (0,23 mm/año) y DIMS (0,21 mm/año) aparecen entre las intervenciones efectivas, junto con la ortoqueratología y la atropina [5].</p>
""",
 "callout": ("Leer con cuidado", "Los porcentajes no son intercambiables: cada ensayo tuvo poblaciones, edades y duraciones distintas. Y más del 70 % de los estudios se hicieron en población asiática. Latinoamérica necesita datos propios."),
 "refs": ["Lam CSY, et al. DIMS spectacle lenses slow myopia progression: a 2-year randomised clinical trial. Br J Ophthalmol. 2020;104(3):363-8.",
          "Bao J, et al. Spectacle lenses with aspherical lenslets for myopia control: a randomized clinical trial. JAMA Ophthalmol. 2022;140(5):472-8.",
          "Rappon J, et al. Control of myopia using diffusion optics spectacle lenses: 12-month results (CYPRESS). Br J Ophthalmol. 2023;107(11):1709-15.",
          "Lam CSY, et al. Long-term myopia control effect and safety in children wearing DIMS spectacle lenses for 6 years. Sci Rep. 2023;13:5475.",
          "Schmidt DC, et al. Efficacy of interventions for myopia control in children: network meta-analyses. Acta Ophthalmol. 2025;103(8):939-65."]},
{"kicker": "Regulación", "title": "Quién las aprobó: <em>el mapa regulatorio</em>",
 "deck": "Situación a octubre de 2026.",
 "body": """
<ul>
<li><strong>Estados Unidos (FDA):</strong> HAL autorizada el 25 de septiembre de 2025 por la vía De Novo, para niños de 6 a 12 años al iniciar, con miopía entre −0,75 y −4,50 D y astigmatismo de hasta 1,50 D [6]. DOT tiene designación de dispositivo innovador desde 2024, sin autorización de comercialización. DIMS no tiene autorización FDA.</li>
<li><strong>Unión Europea:</strong> se comercializan con marcado CE; DOT lo obtuvo en 2020.</li>
<li><strong>Canadá:</strong> DIMS y DOT disponibles desde hace varios años.</li>
<li><strong>China:</strong> uso masivo y más de 20 diseños locales, muchos con poca o ninguna evidencia publicada.</li>
</ul>
<p>Un detalle sensato de la autorización FDA: exige vigilancia posterior para detectar rebote al suspender, y advierte que la eficacia no se ha probado con otros recubrimientos ni tintes.</p>
""",
 "callout": None,
 "refs": ["U.S. Food and Drug Administration. FDA authorizes marketing of first eyeglass lenses to slow progression of pediatric myopia. 25 de septiembre de 2025."]},
{"kicker": "Práctica clínica", "title": "Perlas para <em>colegas y padres</em>",
 "deck": "Su éxito depende de tres cosas que no vienen en la caja: buena adaptación, uso diario prolongado y control con longitud axial.",
 "tips": [("Centrado crítico", "La zona central limpia mide alrededor de 9 mm. DIP monocular y altura pupilar con el armazón ya ajustado."),
          ("12 horas o más", "El beneficio depende de las horas de uso. Unas gafas guardadas en el morral no tratan nada."),
          ("Desconfiar de copias", "Que un lente tenga “puntos” o “anillos” no lo convierte en tratamiento. Original y bien centrado.")],
 "body": """
<p>Conviene advertir a la familia que en las primeras semanas puede haber halos o borrosidad periférica; la mayoría se adapta, pero si no se avisa, se abandona el tratamiento. Si a los 6–12 meses el ojo sigue creciendo rápido, se puede combinar con atropina en baja dosis o cambiar a ortoqueratología o lentes de contacto de desenfoque. Y las gafas no reemplazan los hábitos: dos horas al aire libre al día y pausas en el trabajo de cerca.</p>
""",
 "callout": ("Buenas prácticas MML", "Medir la longitud axial al inicio y cada 6 meses es la única forma de saber si el tratamiento funciona."),
 "refs": []},
]},
# ---------------------------------------------------------------- ED 06
{
"num": "06", "date": "7 de octubre de 2026", "date_short": "7 oct 2026", "month": "Octubre 2026",
"slug": "boletin-ed06.html", "read": "~ 8 min",
"substack": "https://grupomiopialatam.substack.com/p/lentes-de-noche-para-frenar-la-miopia",
"cover_title": "Lentes de noche:<br>la orto-K",
"card_title": "Lentes de noche: la orto-K",
"issue_title": "Lo que hay que saber de la ortoqueratología",
"deck": "Cómo funciona, cuánto frena el crecimiento del ojo, qué riesgos tiene y cómo hacerla bien, para padres y colegas.",
"card_desc": "ROMIO y metaanálisis · efecto a 5 años · queratitis microbiana en proporción · perlas clínicas y reglas para padres.",
"toc": ["Cómo funciona y cuánto frena", "La seguridad no se negocia", "Perlas y reglas de oro"],
"editorial_h": "Un tratamiento médico, no un accesorio",
"editorial": [
"“¿Entonces mi hija duerme con los lentes y en el día no necesita gafas?” Es la pregunta que más escuchamos al explicar la ortoqueratología. Pero lo más importante no es la comodidad de no usar gafas durante el día: <strong>bien indicada, la orto-K frena el crecimiento del ojo miope</strong>.",
"Llevamos más de una década con buena evidencia. En esta edición la ordenamos: qué hace, cuánto funciona, qué riesgos tiene y qué hace falta para que salga bien.",
],
"sections": [
{"kicker": "Evidencia", "title": "Cómo funciona y <em>cuánto frena</em>",
 "deck": "Un lente rígido de geometría inversa que moldea el epitelio corneal mientras el niño duerme.",
 "body": """
<p>Durante la noche, el lente adelgaza el epitelio en el centro y lo engrosa en la periferia media. En el centro la córnea queda más plana y corrige la miopía; en la periferia, el anillo más curvo crea <strong>desenfoque miópico periférico</strong>, la señal que frena el crecimiento del ojo. El efecto es reversible en días o semanas.</p>
<ul>
<li><strong>ROMIO</strong> (Hong Kong, 102 niños de 6–10 años, 2 años): los ojos con orto-K crecieron un 43 % menos, 0,36 mm frente a 0,63 mm [1].</li>
<li><strong>Metaanálisis 2015:</strong> unos 0,27 mm menos en dos años, alrededor de un 45 % menos que las gafas monofocales [2]. El metaanálisis en red de 2025, con 74 ensayos, la ubica entre las intervenciones efectivas [3].</li>
<li><strong>A largo plazo</strong> (Japón, 5 años): 0,99 mm frente a 1,41 mm con gafas, con mayor beneficio en los primeros años y en los más pequeños [4].</li>
<li><strong>Al suspender</strong> (DOEE): el ojo puede crecer más rápido durante un tiempo [5]. No se suspende de golpe en plena edad de progresión.</li>
</ul>
""",
 "callout": None,
 "refs": ["Cho P, Cheung SW. Retardation of myopia in orthokeratology (ROMIO) study: a 2-year randomized clinical trial. Invest Ophthalmol Vis Sci. 2012;53(11):7077-85.",
          "Sun Y, et al. Orthokeratology to control myopia progression: a meta-analysis. PLoS One. 2015;10(4):e0124535.",
          "Schmidt DC, et al. Efficacy of interventions for myopia control in children: network meta-analyses. Acta Ophthalmol. 2025;103(8):939-65.",
          "Hiraoka T, et al. Long-term effect of overnight orthokeratology on axial length elongation: a 5-year follow-up. Invest Ophthalmol Vis Sci. 2012;53(7):3913-9.",
          "Cho P, Cheung SW. Discontinuation of orthokeratology on eyeball elongation (DOEE). Cont Lens Anterior Eye. 2017;40(2):82-7."]},
{"kicker": "Seguridad", "title": "La seguridad: <em>el punto que no se negocia</em>",
 "deck": "Un lente que se duerme puesto tiene un riesgo real: la queratitis microbiana.",
 "body": """
<p>Hay que hablarlo con la misma claridad que la eficacia. Un estudio en EE. UU. con 86 consultorios y 677 niños estimó unos <strong>14 casos por cada 10.000 años de uso</strong>, con intervalo de confianza amplio [6]. Un estudio grande en Rusia encontró entre 4,9 y 5,3 casos por cada 10.000 años-paciente en niños [7].</p>
<p>Es un riesgo comparable al de otros lentes de uso nocturno, y casi siempre asociado a fallas de higiene, especialmente el contacto del lente o el estuche con agua de la llave, donde vive la <em>Acanthamoeba</em>. El consenso BCLA CLEAR concluye que la orto-K es efectiva y segura cuando se adapta bien y se sigue con disciplina [8].</p>
""",
 "callout": ("Regla de oro para familias", "Nunca agua de la llave. Ojo rojo, dolor o molestia con la luz: se retira el lente y se consulta el mismo día."),
 "refs": ["Bullimore MA, et al. The risk of microbial keratitis with overnight corneal reshaping lenses. Optom Vis Sci. 2013;90(9):937-44.",
          "Bullimore MA, et al. Pediatric microbial keratitis with overnight orthokeratology in Russia. Eye Contact Lens. 2021;47(7):420-5.",
          "Vincent SJ, et al. BCLA CLEAR – Orthokeratology. Cont Lens Anterior Eye. 2021;44(2):240-69."]},
{"kicker": "Práctica clínica", "title": "Perlas clínicas y <em>reglas para padres</em>",
 "deck": "Funciona mejor en miopías bajas a moderadas, con astigmatismo corneal bajo y familias capaces de sostener la rutina.",
 "tips": [("Biometría, no refracción", "La orto-K modifica la refracción. Longitud axial al inicio y cada 6 meses."),
          ("Topografía en cada control", "Un tratamiento descentrado da mala visión, halos y menos efecto. La meta es la “diana” centrada."),
          ("Mirar el epitelio", "El mapa epitelial muestra el adelgazamiento central y ayuda a explicárselo a la familia.")],
 "body": """
<p>En cada visita: tinción con fluoresceína, estado del lente y del estuche, y reemplazo según el fabricante. Si a los 6–12 meses el ojo sigue creciendo rápido, se considera combinar con atropina en baja dosis. Para los padres: uso todas las noches, estuche limpio y renovado, solución nueva siempre y asistencia a todos los controles.</p>
<p>No la recomendamos cuando la higiene no es confiable, cuando hay alteraciones de la superficie ocular o cuando la familia no puede asistir a los controles; en esos casos hay alternativas con buena evidencia, como las gafas de desenfoque o la atropina.</p>
""",
 "callout": ("Buenas prácticas MML", "La orto-K es especialmente útil en niños activos, que hacen deporte o natación, o que no toleran las gafas, siempre que la familia la entienda como tratamiento médico y podamos asegurar el seguimiento."),
 "refs": []},
]},
# ---------------------------------------------------------------- ED 07
{
"num": "07", "date": "8 de octubre de 2026", "date_short": "8 oct 2026", "month": "Octubre 2026",
"slug": "boletin-ed07.html", "read": "~ 10 min",
"substack": "https://grupomiopialatam.substack.com/p/puede-una-calculadora-predecir-la",
"cover_title": "¿Puede una calculadora<br>predecir la miopía?",
"card_title": "¿Puede una calculadora predecir la miopía?",
"issue_title": "Calculadoras de miopía e inteligencia artificial",
"deck": "Qué tan confiables son las calculadoras de miopía que circulan en internet y cómo la inteligencia artificial puede hacerlas más precisas.",
"card_desc": "PreMO, BHVI y MPRAS · modelos de IA con historias clínicas y fondo de ojo · AUC, VPP y VPN explicados.",
"toc": ["Qué tan confiables son", "IA: promesa y cautela", "Cómo usarlas en consulta"],
"editorial_h": "Un número exacto no siempre es un número verdadero",
"editorial": [
"“Doctor, ¿cuánto va a subir la fórmula de mi hija?” Cada vez más padres llegan con una captura de pantalla de una calculadora en línea que les dio una cifra exacta para dentro de cinco años.",
"Estas herramientas sirven, pero cada una se validó de forma distinta. En esta edición separamos dos preguntas que se confunden —<strong>riesgo de inicio</strong> y <strong>proyección de progresión</strong>—, revisamos qué tan bien funcionan y cómo la inteligencia artificial puede mejorarlas.",
],
"sections": [
{"kicker": "Evidencia", "title": "Qué tan confiables <em>son</em>",
 "deck": "PreMO predice el inicio; la calculadora del BHVI proyecta la progresión. No responden la misma pregunta.",
 "body": """
<p><strong>PreMO</strong> (Ulster University) combina refracción bajo cicloplejía, longitud axial, edad y miopía parental. En su validación entre poblaciones, con puntaje ≥4 [1]: en niños del Reino Unido de 6–8 años, sensibilidad 97 % y especificidad 96 %; en Hong Kong de 6–8 años, 94 % y 64 %; de 9–10 años, 90 % y 72 %. Casi no deja escapar a un niño en riesgo, pero en poblaciones con mucha miopía marca como “de riesgo” a varios que no lo serán. <strong>Aún no está validada en niños latinoamericanos.</strong></p>
<p><strong>La calculadora del BHVI</strong> acertó en promedio en niños de Hong Kong (diferencia menor de 0,25 D), pero solo el 36 % de los niños quedó dentro del margen esperado; un tercio progresó hasta 1,92 D menos y otro hasta 2,33 D más [2]. En ARVO 2023 se vio que asume que los niños asiáticos progresan casi el doble que los caucásicos, cuando un metaanálisis sugiere una diferencia cercana al 30 % [3].</p>
<p><strong>MPRAS</strong> (L V Prasad, India) integra diez factores. Frente a expertos mostró sensibilidad de 89–91 % y especificidad de 84–86 %, pero en una validación prospectiva pequeña la especificidad bajó al 60 % [4].</p>
""",
 "callout": ("Pregunta abierta para LATAM", "¿Con qué etnia debería ingresarse a un niño latinoamericano, si la calculadora solo ofrece “asiático” o “blanco”?"),
 "refs": ["Fulton JM, et al. Cross-population validation of the PreMO risk indicator for predicting myopia onset in children. Ophthalmic Physiol Opt. 2025;45(1):89-99.",
          "Yang Y, et al. Comparison between estimated and measured myopia progression in Hong Kong children. Ophthalmic Physiol Opt. 2021;41(6):1363-70.",
          "Jong M, Brennan NA, Cheng X, Bullimore MA. Comparison of myopia progression calculators. Invest Ophthalmol Vis Sci. 2023;64(8):814 (ARVO abstract).",
          "Manoharan MK, et al. Myopia progression risk assessment score (MPRAS). Sci Rep. 2023;13:8858."]},
{"kicker": "Inteligencia artificial", "title": "IA: <em>promesa y cautela</em>",
 "deck": "Cifras impresionantes en poblaciones asiáticas. Ninguna es todavía una calculadora pública validada para nuestra región.",
 "body": """
<p>Un modelo <em>random forest</em> entrenado con casi 700.000 registros de refracción de más de 129.000 niños chinos predijo miopía alta a 3 años con un AUC de 0,87–0,98 en validación externa [5]. En Singapur, un sistema de <em>deep learning</em> con fotos de fondo de ojo y datos clínicos alcanzó un AUC de 0,97 para el riesgo de miopía alta a 5 años [6].</p>
<p><strong>AUC, VPP y VPN.</strong> El AUC mide qué tan bien separa la herramienta a quienes progresarán (0,5 es azar; 1, perfecto). Pero el valor predictivo depende de la prevalencia: con sensibilidad de 94 % y especificidad de 64 % en un grupo con 20 % de futuros miopes, de cada 10 niños marcados “en riesgo” solo unos 4 lo serán (VPP ≈ 39 %), mientras que un “sin riesgo” acierta el 98 % de las veces. Con estas cifras, una calculadora sirve más para descartar que para confirmar.</p>
<ul>
<li><strong>Más datos por niño:</strong> longitud axial, curvatura corneal, coroides y hábitos.</li>
<li><strong>Puntos de corte según el uso:</strong> priorizar VPN en tamizaje escolar y VPP antes de indicar tratamiento.</li>
<li><strong>Recalibrar con datos locales</strong> y <strong>predecir con incertidumbre honesta</strong>: un rango que se actualiza en cada control.</li>
</ul>
""",
 "callout": None,
 "refs": ["Lin H, et al. Prediction of myopia development among Chinese school-aged children using refraction data from electronic medical records. PLoS Med. 2018;15(11):e1002674.",
          "Foo LL, et al. Deep learning system to predict the 5-year risk of high myopia using fundus imaging in children. NPJ Digit Med. 2023;6:10.",
          "Gifford KL, et al. IMI – Clinical Management Guidelines Report. Invest Ophthalmol Vis Sci. 2019;60(3):M184-M203."]},
{"kicker": "Práctica clínica", "title": "Cómo usarlas <em>en consulta</em>",
 "deck": "Buenas herramientas para educar y estratificar el riesgo. Ninguna reemplaza el seguimiento real del ojo de cada niño.",
 "tips": [("Riesgo de inicio", "La lógica de PreMO: cicloplejía, longitud axial, edad y padres miopes. Poca hipermetropía y ojo largo: seguimiento cercano."),
          ("Progresión como ilustración", "La curva del BHVI explica el problema, no es una promesa. Es un promedio poblacional."),
          ("El estándar es la biometría", "Longitud axial con biometría óptica cada 6 meses, en línea con las guías IMI.")],
 "body": """
<p>Para las familias: usar las calculadoras para entender el problema, no para fijar una meta exacta; pedir la medición de la longitud axial; llevar el historial de fórmulas —el cambio en el último año es uno de los mejores predictores—; y mantener las bases con evidencia: aire libre diario y pausas en el trabajo de cerca.</p>
""",
 "callout": ("Propuesta MML", "Un AUC alto en un artículo no garantiza un VPP útil en nuestra consulta. Proponemos validar estas herramientas en niños latinoamericanos, con refracción bajo cicloplejía y longitud axial registradas con el mismo protocolo, antes de usarlas para decidir tratamientos."),
 "refs": []},
]},
# ---------------------------------------------------------------- ED 08
{
"num": "08", "date": "10 de octubre de 2026", "date_short": "10 oct 2026", "month": "Octubre 2026",
"slug": "boletin-ed08.html", "read": "~ 8 min",
"substack": "https://grupomiopialatam.substack.com/p/lo-que-una-red-de-datos-revela-sobre",
"cover_title": "Lo que una red<br>de datos revela",
"card_title": "Lo que una red de datos revela",
"issue_title": "Análisis de redes aplicado a la miopía infantil",
"deck": "Cómo una herramienta de salud pública, el análisis de redes, puede ayudarnos a ver patrones que la consulta individual no muestra.",
"card_desc": "Similitud de Jaccard · ejemplo didáctico de 12 niños · triángulo de riesgo, aire libre protector y sesgo de indicación.",
"toc": ["Redes y similitud de Jaccard", "Lo que muestra la red", "Datos LATAM con rigor"],
"editorial_h": "Mirar a los niños como una red",
"editorial": [
"En un curso sobre inteligencia artificial en salud poblacional de la Universidad Johns Hopkins, el profesor Ian McCulloh mostró cómo usó redes para entender la transmisión de infecciones en Baltimore: no miraba a cada paciente por separado, sino las conexiones entre personas y lugares.",
"¿Qué pasaría si hiciéramos lo mismo con la miopía? En esta edición presentamos un <strong>ejercicio didáctico</strong> que muestra qué factores “viajan juntos” y por qué los datos que registramos en cada consulta pueden convertirse en conocimiento regional.",
],
"sections": [
{"kicker": "Método", "title": "Redes y <em>similitud de Jaccard</em>",
 "deck": "Nodos que son características del niño; enlaces cuya fuerza mide cuánto coinciden.",
 "body": """
<p>Una red tiene nodos y enlaces. Aquí, cada nodo es un factor de riesgo, un tratamiento o un resultado. La fuerza del enlace se mide con la <strong>similitud de Jaccard</strong>, propuesta en 1912 por el botánico Paul Jaccard para comparar la flora alpina [1]:</p>
<div class="callout"><div class="callout-title">Fórmula</div><div class="callout-text">Jaccard = niños con ambas características ÷ niños con al menos una de ellas. Va de 0 (nunca coinciden) a 1 (siempre van juntas) y corrige por tamaño.</div></div>
<p>Este enfoque ya se usó para construir “redes de comorbilidad” a partir de millones de registros hospitalarios [2]. Para ilustrarlo construimos un <strong>ejemplo ficticio de 12 niños</strong> —no son pacientes reales— con 10 variables: padres miopes, más de 3 h de pantallas, menos de 1 h al aire libre, 2 h o más al aire libre, atropina, orto-K, gafas de desenfoque, tratamiento combinado, progresión rápida y buena respuesta. Se conservaron solo los enlaces de 0,40 o más.</p>
""",
 "callout": None,
 "refs": ["Jaccard P. The distribution of the flora in the alpine zone. New Phytol. 1912;11(2):37-50.",
          "Hidalgo CA, et al. A dynamic network approach for the study of human phenotypes. PLoS Comput Biol. 2009;5(4):e1000353."]},
{"kicker": "Hallazgos", "title": "Lo que <em>muestra la red</em>",
 "deck": "El ejemplo es inventado; los patrones coinciden con los estudios reales.",
 "tips": [("Triángulo de riesgo", "Pantallas, poco aire libre y progresión rápida van casi siempre juntos (Jaccard 0,67–0,83), con la herencia sumada al núcleo."),
          ("El aire libre protege", "Es el nodo protector más conectado: la buena respuesta se asocia más con él que con cualquier tratamiento aislado."),
          ("La trampa de la atropina", "Queda “en el medio” porque se receta a quienes ya progresan rápido: sesgo de indicación.")],
 "body": """
<p>La evidencia real va en la misma línea. En Guangzhou, 40 minutos diarios de clase al aire libre redujeron la incidencia de miopía a tres años de 39,5 % a 30,4 % [3]. Un metaanálisis asoció el uso de dispositivos inteligentes con mayor probabilidad de miopía, más aún combinado con computador [4]. Y el IMI reconoce la miopía parental y el poco tiempo al aire libre como factores de riesgo establecidos [5].</p>
""",
 "callout": ("Recordatorio", "Una red muestra asociaciones, no causas. Sirve para generar preguntas; las respuestas se confirman con estudios bien diseñados."),
 "refs": ["He M, et al. Effect of time spent outdoors at school on the development of myopia among children in China. JAMA. 2015;314(11):1142-8.",
          "Foreman J, et al. Association between digital smart device use and myopia: a systematic review and meta-analysis. Lancet Digit Health. 2021;3(12):e806-e818.",
          "Morgan IG, et al. IMI Risk Factors for Myopia. Invest Ophthalmol Vis Sci. 2021;62(5):3."]},
{"kicker": "Futuro LATAM", "title": "Datos latinoamericanos, <em>con rigor</em>",
 "deck": "Si cada consulta registra hábitos, tratamiento y longitud axial de forma estructurada, en unos años podremos construir redes reales con miles de niños.",
 "body": """
<ul>
<li><strong>El tiempo al aire libre es parte del tratamiento</strong>, no un consejo opcional al final de la consulta.</li>
<li><strong>El niño que reúne varios factores</strong> (padres miopes, muchas pantallas, poco aire libre) merece vigilancia estrecha y un plan desde el inicio.</li>
<li><strong>Los datos que registramos valen oro:</strong> con información de varios países podríamos comparar si el peso de las pantallas o del aire libre cambia entre Colombia, México, Ecuador o Puerto Rico.</li>
</ul>
<p>Para pasar de explorar a predecir hay que construir modelos con rigor y reportarlos con estándares como <strong>TRIPOD+AI</strong> [6]. Para las familias, el mensaje es simple: unas 2 horas diarias al aire libre, límites y pausas en las pantallas, controles tempranos si los padres son miopes y constancia en el seguimiento.</p>
""",
 "callout": ("Llamado a la red", "¿Su consulta registra hábitos y longitud axial de forma estructurada? Escríbanos a <strong>investigacion@miopialatam.org</strong> para sumar datos a una red regional."),
 "refs": ["Collins GS, et al. TRIPOD+AI statement. BMJ. 2024;385:e078378.",
          "Inspirado en: curso “AI for Population Health & Disease Management”, módulo 6.4, Dr. Ian McCulloh, Johns Hopkins University."]},
]},
# ---------------------------------------------------------------- ED 09
{
"num": "09", "date": "12 de octubre de 2026", "date_short": "12 oct 2026", "month": "Octubre 2026",
"slug": "boletin-ed09.html", "read": "~ 10 min",
"substack": "https://grupomiopialatam.substack.com/p/cuanto-vale-una-dioptria-el-costo",
"cover_title": "¿Cuánto vale<br>una dioptría?",
"card_title": "¿Cuánto vale una dioptría?",
"issue_title": "El costo oculto de no frenar la miopía",
"deck": "El control de la miopía da sus frutos dentro de 40 años, pero las decisiones se toman hoy. La economía de la salud tiene una forma de medirlo.",
"card_desc": "AVAC explicado sin fórmulas · costo-efectividad en Hong Kong y modelos globales · el vacío latinoamericano.",
"toc": ["Cada dioptría y el AVAC", "Costo-efectividad: la evidencia", "Lo que falta en LATAM"],
"editorial_h": "El beneficio llega en décadas; la factura, este mes",
"editorial": [
"“Doctor, ¿vale la pena pagar un tratamiento si con las gafas mi hijo ve bien?” Es una de las preguntas más honestas de la consulta. El tratamiento no busca mejorar la visión de hoy: busca bajar el riesgo de un adulto de 50 o 60 años con un ojo demasiado largo.",
"En esta edición ponemos ambas cosas en la misma balanza con las herramientas de la economía de la salud, y señalamos un vacío que nos toca llenar: <strong>no hay modelos latinoamericanos de costo-efectividad del control de miopía</strong>.",
],
"sections": [
{"kicker": "Conceptos", "title": "Cada dioptría <em>y el AVAC</em>",
 "deck": "Para comparar tratamientos se calcula el costo por año de vida ajustado por calidad ganado.",
 "body": """
<p>Con datos de unas 21.000 personas en cinco estudios poblacionales, Bullimore y Brennan estimaron que cada dioptría adicional de miopía se asocia con un <strong>67 % más de prevalencia de maculopatía miópica</strong>; frenar la miopía en una dioptría reduciría ese riesgo en torno a un 40 % [1].</p>
<p>El <strong>AVAC</strong> (año de vida ajustado por calidad, QALY) vale 1 por un año con salud plena y menos de 1 si una condición limita la vida. Si el costo por AVAC ganado queda bajo el umbral que un país está dispuesto a pagar, el tratamiento es costo-efectivo.</p>
<p>El dilema es el <strong>descuento temporal</strong>: con un 3–3,5 % anual, un año de buena visión a los 60 pesa mucho menos que el dinero gastado a los 8. Como el beneficio del control de miopía llega tarde, el descuento lo castiga más que a casi cualquier otro tratamiento.</p>
""",
 "callout": None,
 "refs": ["Bullimore MA, Brennan NA. Myopia control: why each diopter matters. Optom Vis Sci. 2019;96(6):463-5."]},
{"kicker": "Evidencia", "title": "Costo-efectividad: <em>la evidencia</em>",
 "deck": "Pocos estudios, pero todos apuntan en la misma dirección.",
 "body": """
<ul>
<li><strong>Lentes de desenfoque en Hong Kong:</strong> en 100.000 niños de 6–11 años seguidos de por vida, la miopía alta bajó de 10,7 % a 5,9 %, con unos 26.400 dólares por AVAC (87 % de probabilidad de ser costo-efectivo). Sin descuento temporal, el control ahorraba dinero [2].</li>
<li><strong>Costo de por vida:</strong> la miopía de un niño de 8 años cuesta unos 7.400–8.000 dólares solo con corrección tradicional; las opciones de control redujeron la progresión entre 42 y 49 %, y algunas resultaron más baratas que no tratar, según país y precio local [3].</li>
<li><strong>Corto plazo (5 años):</strong> el aire libre ahorró dinero y la atropina al 0,05 % tuvo el menor costo por dioptría evitada; gafas de desenfoque, luz roja y orto-K también podrían ser costo-efectivas [4].</li>
<li><strong>Revisión sistemática:</strong> frenar la progresión probablemente es más costo-efectivo que tratar después la miopía patológica, aunque los estudios de prevención son escasos [5].</li>
</ul>
""",
 "callout": ("En la consulta", "No tratamos la visión de hoy, tratamos el riesgo de mañana. Cada dioptría evitada cuenta, y hay opciones para distintos presupuestos: la más barata, el tiempo al aire libre, es la de mejor relación costo-beneficio."),
 "refs": ["So C, et al. Lifetime cost-effectiveness of myopia control intervention for the children population. J Glob Health. 2024;14:04183.",
          "Fricke TR, et al. Establishing a method to estimate the effect of antimyopia management options on lifetime cost of myopia. Br J Ophthalmol. 2023;107(8):1043-50.",
          "Agyekum S, et al. Cost-effectiveness analysis of myopia progression interventions in children. JAMA Netw Open. 2023;6(11):e2340986.",
          "Agyekum S, et al. Cost-effectiveness analysis of myopia management: a systematic review. Front Public Health. 2023;11:1093836."]},
{"kicker": "Futuro LATAM", "title": "Lo que falta <em>en Latinoamérica</em>",
 "deck": "Casi todo viene de Asia, Europa y Oceanía. En economía de la salud los resultados no se trasladan sin más.",
 "body": """
<p>El precio local de una caja de lentes o de un frasco de atropina puede cambiar por completo la conclusión. Nos faltan datos propios de largo plazo: cuánto progresan nuestros niños, cuánto cuestan aquí las complicaciones y cuánto pesa en una familia perder visión a los 55 años. Una red como MML puede ayudar a responderlo si medimos de forma consistente la refracción bajo cicloplejía y la longitud axial.</p>
<p>La inteligencia artificial suma otra pieza: un tratamiento es más costo-efectivo cuanto mejor se elige a quién tratar. Si los modelos predicen qué niños progresarán rápido, el esfuerzo se concentra donde más dioptrías se evitan por cada peso invertido.</p>
<ul>
<li><strong>Para las familias:</strong> dos horas diarias al aire libre, pausas en el trabajo de cerca, control anual desde preescolar, no hipocorregir, constancia y comparar el <strong>costo total</strong> del tratamiento, no solo el del primer mes.</li>
</ul>
""",
 "callout": ("Llamado a la red", "¿Le interesa construir el primer modelo latinoamericano de costo-efectividad del control de miopía? Escríbanos a <strong>investigacion@miopialatam.org</strong>."),
 "refs": []},
]},
# ---------------------------------------------------------------- ED 10
{
"num": "10", "date": "15 de octubre de 2026", "date_short": "15 oct 2026", "month": "Octubre 2026",
"slug": "boletin-ed10.html", "read": "~ 8 min",
"substack": "https://grupomiopialatam.substack.com/p/premiopia-como-ver-venir-la-miopia",
"cover_title": "Premiopía: verla venir<br>antes de que llegue",
"card_title": "Premiopía: verla venir antes de que llegue",
"issue_title": "Cómo se detecta y qué se puede hacer a tiempo",
"deck": "Un niño puede no ser miope todavía y aun así ya estar en camino. Qué es la premiopía, cómo se detecta y qué se puede hacer a tiempo.",
"card_desc": "Definición IMI · puntos de corte CLEERE · aire libre y LAMP2 · tres cosas que mirar en consulta.",
"toc": ["Qué es la premiopía", "Lo que dice la evidencia", "En la consulta y en casa"],
"editorial_h": "Llegar antes que la miopía",
"editorial": [
"“Doctor, el niño ve perfecto. ¿Para qué lo volvemos a revisar en seis meses?” A veces, debajo de ese “ve perfecto”, hay un dato que preocupa: un ojo de 6 años que ya no tiene la reserva de hipermetropía que debería tener a esa edad.",
"A eso le llamamos premiopía: <strong>una ventana de oportunidad para cambiar la historia antes de que empiece</strong>. Detectarla requiere algo que no siempre se hace: medir bien y comparar con lo esperado para la edad.",
],
"sections": [
{"kicker": "Conceptos", "title": "Qué es <em>la premiopía</em>",
 "deck": "La reserva de hipermetropía que se gasta demasiado pronto.",
 "body": """
<p>Casi todos los niños nacen con algo de hipermetropía. Con el crecimiento, el ojo se alarga y esa reserva baja hasta acercarse a cero. El problema es cuando se gasta demasiado pronto: si a los 6 años ya está prácticamente en cero, al ojo le queda poco margen antes de cruzar hacia la miopía.</p>
<p>El IMI la definió en 2019 como una refracción entre <strong>+0,75 y −0,50 D</strong> en un niño cuya edad, refracción y otros factores de riesgo hacen suficientemente probable que desarrolle miopía, al punto de justificar medidas preventivas [1]. El matiz: un +0,50 a los 11 años puede ser normal; el mismo +0,50 a los 6 es una alerta.</p>
<p>Importa porque la miopía que empieza temprano tiene más años para avanzar: en Singapur, quienes se volvieron miopes antes tuvieron más riesgo de llegar a miopía alta [2].</p>
""",
 "callout": None,
 "refs": ["Flitcroft DI, et al. IMI – Defining and classifying myopia. Invest Ophthalmol Vis Sci. 2019;60(3):M20-M30.",
          "Chua SY, et al. Age of onset of myopia predicts risk of high myopia in later childhood. Ophthalmic Physiol Opt. 2016;36(4):388-94."]},
{"kicker": "Evidencia", "title": "Lo que dice <em>la evidencia</em>",
 "deck": "La refracción bajo cicloplejía predice mejor que cualquier otro dato.",
 "body": """
<p><strong>CLEERE</strong> siguió a 4.512 niños no miopes en EE. UU. El mejor predictor fue la refracción ciclopléjica, con puntos de corte por edad: <strong>menos de +0,75 D a los 6 años; +0,50 D o menos a los 7–8; +0,25 D o menos a los 9–10</strong>. Con la refracción incluida, el AUC fue de 0,87 a 0,93; la miopía parental y la longitud axial aportaron información adicional pero modesta [3].</p>
<p><strong>Aire libre:</strong> en Guangzhou, una clase diaria de 40 minutos afuera redujo la incidencia de miopía a tres años de 39,5 % a 30,4 % [4]. Es barata, sin efectos adversos y funciona mejor antes de que aparezca la miopía.</p>
<p><strong>Atropina en dosis baja:</strong> en LAMP2 (474 niños de 4–9 años con refracción entre 0,00 y +1,00 D), la miopía apareció a dos años en el 28,4 % con 0,05 % frente al 53,0 % con placebo; la concentración de 0,01 % no se diferenció del placebo [5].</p>
""",
 "callout": ("Leer con calma", "LAMP2 es un solo ensayo, en población china y con dos años de seguimiento. No es una indicación para todos los niños con refracción baja, sino una herramienta para casos de riesgo seleccionados y con seguimiento cercano."),
 "refs": ["Zadnik K, et al. Prediction of juvenile-onset myopia. JAMA Ophthalmol. 2015;133(6):683-9.",
          "He M, et al. Effect of time spent outdoors at school on the development of myopia among children in China. JAMA. 2015;314(11):1142-8.",
          "Yam JC, et al. Effect of low-concentration atropine eyedrops vs placebo on myopia incidence in children: the LAMP2 randomized clinical trial. JAMA. 2023;329(6):472-81."]},
{"kicker": "Práctica clínica", "title": "En la consulta <em>y en casa</em>",
 "deck": "Tres cosas que mirar en cada niño en edad escolar, más allá de la agudeza visual.",
 "tips": [("Cicloplejía", "Comparar la refracción con lo esperado para la edad. Sin gotas, un premiope pasa desapercibido."),
          ("Factores de riesgo", "Padres miopes, poco tiempo al aire libre y mucha carga de trabajo de cerca desde muy pequeño."),
          ("La tendencia", "Un ojo que crece más rápido de lo esperado entre visitas dice más que una sola medición.")],
 "body": """
<p>Si el niño cumple criterios, el plan casi siempre empieza por lo más simple: aire libre y hábitos, con controles más frecuentes. La atropina se reserva para casos con varios factores de riesgo, tras conversar con la familia sobre beneficios, limitaciones y lo que aún no sabemos.</p>
<p><strong>Para los padres:</strong> pidan refracción bajo cicloplejía entre los 5 y los 8 años; pregunten por la reserva de hipermetropía; apunten a unas dos horas diarias de juego afuera; si son miopes, comiencen los controles desde preescolar; y no esperen a que el niño “no vea”: cuando aparecen las quejas, la miopía ya llegó.</p>
""",
 "callout": ("Futuro LATAM", "Sin datos latinoamericanos de refracción por edad, seguimos usando puntos de corte de otras poblaciones. Medir de forma consistente en toda la región es una prioridad de la red MML."),
 "refs": []},
]},
]
