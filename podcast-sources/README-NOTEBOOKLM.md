# Guia para generar podcasts con NotebookLM

## Pasos para cada tema (6 articulos)

1. Ve a **https://notebooklm.google.com** (login con cuenta Google)
2. Click en **"New notebook"** (Nuevo notebook)
3. Click en **"Upload sources"** o arrastra el archivo `.txt` correspondiente
4. Espera unos segundos a que NotebookLM procese la fuente
5. En el panel derecho, busca **"Audio Overview"** o **"Resumen de audio"**
6. Click en **"Generate"** o **"Generar"** (toma 5-10 minutos)
7. Cuando termine, click en el boton de **descarga (icono download)** para bajar el MP3
8. Renombra el archivo MP3 segun la tabla de abajo
9. Muevelo a `/audio/` en el proyecto

## Tabla de archivos

| Archivo .txt | Nombre del MP3 a guardar | Articulo HTML donde ira |
|---|---|---|
| `01-axl-vs-ser.txt` | `axl-vs-ser.mp3` | `articulo-axl-ser.html` |
| `02-ortok.txt` | `ortok.mp3` | `articulo-ortok.html` |
| `03-atropina.txt` | `atropina.mp3` | `articulo-atropina.html` |
| `04-lentes-oftalmicas.txt` | `lentes-oftalmicas.mp3` | `articulo-lentes-oftalmicas.html` |
| `05-lc-blandos.txt` | `lc-blandos.mp3` | `articulo-lc-blandos.html` |
| `06-terapias-combinadas.txt` | `terapias-combinadas.mp3` | `articulo-terapias-combinadas.html` |

## Tips para mejores podcasts

- **Customize prompt** en NotebookLM: agrega un prompt como "Make the discussion focused on Latin American clinical practice, in Spanish, between two experts: one optometrist and one ophthalmologist discussing the topic for fellow clinicians."
- **Idioma**: NotebookLM puede generar en español, pero a veces el español es mixto. Si el resultado sale en ingles, regenera y especifica "in Spanish please".
- **Duracion**: tipicamente 8-15 minutos por podcast.

## Cuando termines

Dime "ya tengo los MP3" y muevelos a `/audio/`. El sistema de audio player en cada articulo ya esta listo - los reproductores activaran automaticamente cuando detecten los archivos.
