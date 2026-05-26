# Digest editorial diario MML LATAM

Script automático que cada mañana a las **7:00 AM (Colombia)** lee novedades de **Review of Myopia Management** y **Myopia Profile**, las resume en español con Claude y envía un correo a `info@miopialatam.org`.

Implementa el item **diario** de la agenda editorial 2026–2027 ("skim de RoMM 5 min · curación de tema") de forma automatizada.

## Componentes

- `scripts/daily_digest.py` — script principal
- `scripts/requirements.txt` — dependencias Python
- `.github/workflows/daily-digest.yml` — workflow GitHub Actions con cron 12:00 UTC
- `state/last_seen.json` — memoria de URLs ya vistas (autogestionada)

## Setup inicial (una sola vez)

### 1. Obtener API key de Anthropic

1. Entrar a https://console.anthropic.com
2. Crear cuenta (es independiente de Claude Pro/Max)
3. Cargar **USD 5 de crédito inicial** (alcanza para ~3 años de digests con Haiku)
4. Sección **API Keys** → **Create Key** → copiar el valor (`sk-ant-...`)

### 2. Obtener la contraseña SMTP del buzón

La misma contraseña que usás para entrar al webmail de `info@miopialatam.org` en Namecheap Private Email (`https://privateemail.com`).

> Si no la recordás, podés resetearla desde Namecheap → Dashboard → Private Email → Manage → Reset password.

### 3. Cargar los secrets en GitHub

En el repo `Leormar/miopialatam-web`:

1. **Settings** → **Secrets and variables** → **Actions**
2. Click **New repository secret** y agregar dos secretos:

| Nombre | Valor |
|---|---|
| `ANTHROPIC_API_KEY` | la key del paso 1 (empieza con `sk-ant-`) |
| `SMTP_PASSWORD` | la contraseña del buzón `info@miopialatam.org` |

### 4. Primer disparo manual (para verificar)

1. Repo → pestaña **Actions** → workflow **"Digest MML diario"**
2. Click **Run workflow** → **Run workflow**
3. Esperar ~1 min · revisar los logs
4. Si todo OK, llega un email de bienvenida a `info@miopialatam.org` con asunto "📚 Digest MML activado · primer envío"

A partir de mañana corre solo cada día a las 7:00 AM Colombia.

## Costo operativo

| Recurso | Costo |
|---|---|
| GitHub Actions (público o privado free) | $0 |
| Anthropic Claude Haiku 4.5 (~7K tokens/día) | ~$0.15/mes |
| SMTP Namecheap ox-pro | ya está incluido en el plan del email |
| **Total** | **~$0.15/mes** (~$2/año) |

## Personalización

Variables de entorno opcionales (se pueden agregar al `env:` del workflow):

| Variable | Default | Uso |
|---|---|---|
| `EMAIL_TO` | `info@miopialatam.org` | Cambiar destinatario |
| `EMAIL_FROM` | `info@miopialatam.org` | Remitente del envío |
| `SMTP_USER` | `info@miopialatam.org` | Usuario login SMTP |
| `CLAUDE_MODEL` | `claude-haiku-4-5-20251001` | Cambiar a Sonnet para mejor calidad (~10x precio) |

## Cómo funciona

1. Lee `state/last_seen.json` para saber qué URLs ya envió.
2. Fetch al RSS de RoMM + scrape de Myopia Profile (clinical + science).
3. Compara contra el estado → identifica novedades.
4. Si hay nuevas, las envía a Claude (modelo Haiku) para resumen en español.
5. Compone email HTML branded MML y lo envía vía SMTP autenticado de Namecheap.
6. Actualiza `state/last_seen.json` (limitado a últimas 500 URLs).
7. El workflow commitea el state file de vuelta al repo para que la próxima corrida lo vea.

**Primer día:** modo *bootstrap*. Solo envía un email de bienvenida y guarda lo que ya existe como "ya visto" — para no inundar el inbox con 30 artículos viejos. A partir del día 2 solo recibís cosas verdaderamente nuevas.

## Pausar / reactivar

- **Pausar:** Actions → workflow → ⋯ → **Disable workflow**
- **Reanudar:** ⋯ → **Enable workflow**
- **Editar horario:** modificar la línea `cron: '0 12 * * *'` en `daily-digest.yml`. El formato es UTC.

## Resetear estado (si querés volver a recibir un digest "completo")

Eliminá `state/last_seen.json` y restaurá el contenido inicial:

```json
{ "seen_urls": [], "first_run": true, "last_run": null }
```

El siguiente run hará bootstrap de nuevo.
