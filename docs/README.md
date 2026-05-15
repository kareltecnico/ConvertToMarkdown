# ConvertToMarkdown

Herramienta de automatizacion para convertir archivos compatibles con MarkItDown a formato Markdown,
disenada para facilitar el procesamiento de documentos con modelos de lenguaje (IA).

**Compatible con Windows y macOS.**

---

## Tabla de Contenidos

- [Descripcion del Proyecto](#descripcion-del-proyecto)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Requisitos](#requisitos)
- [Instalacion](#instalacion)
- [Uso](#uso)
- [Archivos del Proyecto](#archivos-del-proyecto)
- [Solucion de Problemas](#solucion-de-problemas)

---

## Descripcion del Proyecto

**ConvertToMarkdown** convierte documentos y otros archivos soportados a archivos `.md` (Markdown) de forma masiva.
El resultado es texto limpio y estructurado, ideal para ser procesado por modelos de IA,
herramientas de RAG, pipelines de analisis o cualquier sistema que trabaje con texto plano.

**Casos de uso tipicos:**

- Extraer texto de contratos, planos, reportes, facturas, hojas de calculo y presentaciones
- Preparar documentos para embeddings o busqueda semantica
- Automatizar la ingesta de archivos en flujos de trabajo con IA

---

## Estructura del Proyecto

```
ConvertToMarkdown/
|
+-- ConvertToMarkdown.bat       <- Launcher para Windows  (doble clic)
+-- ConvertToMarkdown.command   <- Launcher para macOS    (doble clic)
+-- convert_all.py       <- Script de conversion a Markdown
|
+-- input/               <- Coloca aqui los archivos a convertir
+-- output/              <- Los archivos .md generados aparecen aqui
+-- docs/                <- Documentacion del proyecto
+-- .venv/               <- Entorno virtual de Python (dependencias)
```

---

## Requisitos

| | Windows | macOS |
|---|---|---|
| Sistema | Windows 10 / 11 | macOS 12 Monterey o superior |
| Python | 3.10+ (python.org) | 3.10+ (`brew install python`) |
| Launcher | `ConvertToMarkdown.bat` | `ConvertToMarkdown.command` |

---

## Instalacion

### 1. Copiar el proyecto

Copia la carpeta `ConvertToMarkdown` a cualquier ubicacion de tu equipo.

---

### 2. Crear el entorno virtual

**Windows (PowerShell):**
```powershell
python -m venv .venv
```

**macOS (Terminal):**
```bash
python3 -m venv .venv
```

---

### 3. Instalar dependencias

**Windows:**
```powershell
.\.venv\Scripts\Activate
pip install "markitdown[pdf,docx,pptx,xlsx,xls,outlook,audio-transcription]"
```

**macOS:**
```bash
source .venv/bin/activate
pip install "markitdown[pdf,docx,pptx,xlsx,xls,outlook,audio-transcription]"
```

Esto instala la libreria `markitdown` junto con dependencias para PDF, Word,
PowerPoint, Excel, mensajes de Outlook y audio.

---

### 4. (Solo macOS) Dar permisos de ejecucion al launcher

Este paso solo se hace una vez despues de copiar el proyecto:

```bash
chmod +x "ConvertToMarkdown.command"
```

---

## Uso

### Opcion A — Launcher con menu (recomendado)

**Windows:** Doble clic en `ConvertToMarkdown.bat`

**macOS:** Doble clic en `ConvertToMarkdown.command`

> Si macOS bloquea el archivo la primera vez, ve a **Ajustes > Privacidad y Seguridad**
> y haz clic en **"Abrir de todas formas"**.

Se abrira una ventana de terminal con el menu:

```
+------------------------------------------------------+
|       ConvertToMarkdown  -  Menu Principal           |
+------------------------------------------------------+
|                                                      |
|   [1]  Convertir archivos a Markdown                 |
|                                                      |
|   [2]  Abrir carpeta INPUT  (archivos de entrada)    |
|                                                      |
|   [3]  Abrir carpeta OUTPUT (Markdown generados)     |
|                                                      |
|   [0]  Salir                                         |
|                                                      |
+------------------------------------------------------+
```

1. Coloca tus archivos en la carpeta `input/`
2. Presiona `1` y Enter para iniciar la conversion
3. Revisa el resultado y presiona Enter para volver al menu
4. Los archivos `.md` apareceran en la carpeta `output/`
5. Presiona `0` para salir

En macOS, la opcion `0` cierra automaticamente la ventana de Terminal abierta por
`ConvertToMarkdown.command`.

---

### Opcion B — Ejecucion directa por terminal

**Windows:**
```powershell
.\.venv\Scripts\Activate
python convert_all.py
```

**macOS:**
```bash
source .venv/bin/activate
python convert_all.py
```

---

## Archivos del Proyecto

### `ConvertToMarkdown.bat` (Windows)

Launcher de Windows que:
- Activa automaticamente el entorno virtual `.venv`
- Presenta un menu interactivo con opciones numeradas
- Llama a los scripts de Python segun la seleccion del usuario
- No requiere conocimientos de terminal para operar

### `ConvertToMarkdown.command` (macOS)

Launcher equivalente para macOS que:
- Requiere permiso de ejecucion (`chmod +x`) solo la primera vez
- Activa automaticamente el entorno virtual `.venv`
- Presenta el mismo menu con colores ANSI en Terminal.app
- Verifica que el `.venv` exista y muestra instrucciones si no esta configurado
- Usa `open` para abrir carpetas en Finder
- Cierra automaticamente la ventana de Terminal al elegir `0`

### `convert_all.py`

Script principal de conversion. Realiza las siguientes operaciones:

1. Escanea la carpeta `input/` en busca de archivos soportados
2. Convierte cada archivo a texto usando la API de `MarkItDown`
3. Valida que el contenido no este vacio antes de guardar
4. Guarda el resultado como archivo `.md` en la carpeta `output/`
5. Reporta el estado de cada archivo: `[OK]`, `[WARNING]` o `[ERROR]`

**Ejemplo de salida:**

```
Converting: REPORTE_001.xlsx
  [OK] Saved: REPORTE_001.md
Converting: DOCUMENTO_VACIO.pdf
  [WARNING] Empty output for: DOCUMENTO_VACIO.pdf

Done: 1 converted, 1 failed.
```

---

## Solucion de Problemas

| Problema | SO | Causa probable | Solucion |
|---|---|---|---|
| El `.bat` se cierra solo | Windows | `.venv` no existe | Crea el entorno y reinstala dependencias |
| `.command` bloqueado | macOS | Gatekeeper (seguridad) | Ajustes > Privacidad > "Abrir de todas formas" |
| `.command` no abre Terminal | macOS | Sin permiso de ejecucion | Ejecuta `chmod +x ConvertToMarkdown.command` |
| `[ERROR]` al convertir | Ambos | Archivo protegido, danado o formato no soportado | Verifica que el archivo se abra manualmente |
| `[WARNING]` contenido vacio | Ambos | Archivo sin texto extraible o escaneado sin OCR | Usa OCR antes de convertir |
| `markitdown` no encontrado | Ambos | Dependencias no instaladas | Ejecuta `pip install "markitdown[pdf,docx,pptx,xlsx,xls,outlook,audio-transcription]"` en el `.venv` |

---

## Dependencias

| Paquete | Version minima | Funcion |
|---|---|---|
| `markitdown` | 0.1.5 | Motor principal de conversion |
| `pdfminer-six` | 20251230 | Extraccion de texto de PDF |
| `pdfplumber` | 0.11.9 | Lectura estructurada de PDF |
| `pypdfium2` | 5.8.0 | Renderizado de paginas PDF |
| `Pillow` | 9.1+ | Procesamiento de imagenes |
| `mammoth`, `python-pptx`, `openpyxl`, `pandas`, `xlrd` | segun MarkItDown | Lectura de Office y hojas de calculo |

---

## Creditos

Este proyecto esta construido sobre **[MarkItDown](https://github.com/microsoft/markitdown)**,
una herramienta open source desarrollada por **Microsoft** bajo licencia MIT.

Todo el credito del motor de conversion pertenece al equipo de Microsoft y sus colaboradores.
Este repositorio unicamente agrega un script de automatizacion masiva y launchers
con menu interactivo para Windows y macOS.

---

## Notas

- Los archivos basados en **imagenes escaneadas** (sin capa de texto) pueden generar archivos `.md` vacios.
  Para estos casos se recomienda aplicar OCR previamente (por ejemplo con `tesseract` o Adobe Acrobat).
- El script procesa **todos los archivos soportados** que encuentre en `input/` en cada ejecucion.
  Si no deseas reconvertir un archivo, retiralo de la carpeta antes de ejecutar.
