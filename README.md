# ConvertToMarkdown - File to Markdown Converter

> Herramienta de automatizacion para convertir archivos compatibles con MarkItDown a Markdown,
> lista para usar con un solo doble clic. Compatible con **Windows** y **macOS**.

> **Basado en [MarkItDown](https://github.com/microsoft/markitdown) de Microsoft.**
> Este proyecto es un wrapper con interfaz CLI y launchers para facilitar su uso diario.

---

## Que hace?

Convierte los archivos soportados de la carpeta `input/` a archivos `.md` en `output/`.
El resultado es texto limpio ideal para pipelines de IA, RAG o analisis de documentos.

Formatos soportados por MarkItDown incluyen PDF, Word, PowerPoint, Excel, imagenes,
audio, HTML, CSV, JSON, XML, ZIP, EPUB y mas. La compatibilidad exacta depende de
las dependencias opcionales instaladas.

---

## Inicio Rapido

### Windows

```powershell
# 1. Clonar el repo
git clone https://github.com/kareltecnico/ConvertToMarkdown.git
cd ConvertToMarkdown

# 2. Crear entorno virtual e instalar dependencias
python -m venv .venv
.\.venv\Scripts\Activate
pip install "markitdown[pdf,docx,pptx,xlsx,xls,outlook,audio-transcription]"

# 3. Doble clic en ConvertToMarkdown.bat
```

### macOS

```bash
# 1. Clonar el repo
git clone https://github.com/kareltecnico/ConvertToMarkdown.git
cd ConvertToMarkdown

# 2. Crear entorno virtual e instalar dependencias
python3 -m venv .venv
source .venv/bin/activate
pip install "markitdown[pdf,docx,pptx,xlsx,xls,outlook,audio-transcription]"

# 3. Dar permiso al launcher (solo la primera vez)
chmod +x ConvertToMarkdown.command

# 4. Doble clic en ConvertToMarkdown.command
```

---

## Uso

1. Copia tus archivos a la carpeta `input/`
2. Abre el launcher (`ConvertToMarkdown.bat` en Windows / `ConvertToMarkdown.command` en Mac)
3. Presiona `1` para iniciar la conversion
4. Los archivos `.md` apareceran en `output/`

---

## Estructura

```
ConvertToMarkdown/
+-- ConvertToMarkdown.bat       <- Launcher Windows
+-- ConvertToMarkdown.command   <- Launcher macOS
+-- convert_all.py       <- Script de conversion
+-- input/               <- Archivos de entrada (ignorados por git)
+-- output/              <- Markdowns de salida (ignorados por git)
+-- docs/
    +-- README.md        <- Documentacion completa
```

---

## Documentacion completa

Ver [docs/README.md](docs/README.md) para instrucciones detalladas de instalacion,
solucion de problemas y referencia de archivos.

---

## Creditos

Este proyecto esta construido sobre **[MarkItDown](https://github.com/microsoft/markitdown)**,
una herramienta open source desarrollada por **Microsoft**.

Todo el credito del motor de conversion pertenece al equipo de Microsoft y sus colaboradores.
Este repositorio unicamente agrega:
- Un script de conversion masiva (`convert_all.py`)
- Launchers con menu interactivo para Windows (`.bat`) y macOS (`.command`)
- Documentacion de uso en espanol

---

## Dependencias

- [markitdown](https://github.com/microsoft/markitdown) — Motor de conversion (Microsoft, MIT License)
- pdfminer-six, pdfplumber, pypdfium2 — Motores de lectura de PDF
- mammoth, python-pptx, openpyxl, pandas, xlrd — Lectura de Office y hojas de calculo

---

## Licencia

MIT — Libre para uso personal y comercial.
Recuerda respetar la licencia original de [MarkItDown (MIT)](https://github.com/microsoft/markitdown/blob/main/LICENSE).
