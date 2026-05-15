# ConvertToMarkdown - File to Markdown Converter

> Herramienta de automatizacion para convertir archivos compatibles con MarkItDown a Markdown,
> lista para usar con un solo doble clic. Compatible con **Windows** y **macOS**.

> **Basado en [MarkItDown](https://github.com/microsoft/markitdown) de Microsoft.**
> Este proyecto es un wrapper con interfaz CLI y launchers para facilitar su uso diario.

---

## Que hace?

Convierte los archivos soportados de la carpeta `input/` a archivos `.md` en `output/`.
El resultado es texto limpio ideal para pipelines de IA, RAG o analisis de documentos.
Tambien procesa subcarpetas, omite archivos que no cambiaron desde la ultima conversion
y genera un reporte en `output/conversion_report.txt`.

Formatos soportados por MarkItDown incluyen PDF, Word, PowerPoint, Excel, imagenes,
audio, HTML, CSV, JSON, XML, ZIP, EPUB y mas. La compatibilidad exacta depende de
las dependencias opcionales instaladas.

---

## Inicio Rapido

### Para usuarios no tecnicos

Si no usas Git ni terminal todos los dias, empieza por la
[Guia facil para usuarios](GUIA_FACIL.md).

### Windows

```powershell
# 1. Clonar el repo
git clone https://github.com/kareltecnico/ConvertToMarkdown.git
cd ConvertToMarkdown

# 2. Crear entorno virtual e instalar dependencias
python -m venv .venv
.\.venv\Scripts\Activate
pip install "markitdown[pdf,docx,pptx,xlsx,xls,outlook,audio-transcription]"
# o, recomendado:
pip install -r requirements.txt

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
# o, recomendado:
pip install -r requirements.txt

# 3. Dar permiso al launcher (solo la primera vez)
chmod +x ConvertToMarkdown.command

# 4. Doble clic en ConvertToMarkdown.command
```

---

## Uso

1. Copia tus archivos a la carpeta `input/`
2. Abre el launcher (`ConvertToMarkdown.bat` en Windows / `ConvertToMarkdown.command` en Mac)
3. Presiona `1` para iniciar la conversion
4. Presiona Enter al finalizar para volver al menu
5. Los archivos `.md` apareceran en `output/`

En macOS, la opcion `0` cierra automaticamente la ventana de Terminal abierta por
`ConvertToMarkdown.command`.

Opciones utiles del menu:
- `4`: limpiar `input/` conservando `input/README.md`
- `5`: limpiar `output/` conservando `output/README.md`

---

## Estructura

```
ConvertToMarkdown/
+-- ConvertToMarkdown.bat       <- Launcher Windows
+-- ConvertToMarkdown.command   <- Launcher macOS
+-- convert_all.py       <- Script de conversion
+-- clean_folder.py      <- Limpieza segura de input/output
+-- requirements.txt     <- Dependencias recomendadas
+-- input/               <- Archivos de entrada (ignorados por git)
+-- output/              <- Markdowns de salida (ignorados por git)
+-- docs/
    +-- README.md        <- Documentacion completa
```

---

## Documentacion completa

Ver [docs/README.md](docs/README.md) para instrucciones detalladas de instalacion,
solucion de problemas y referencia de archivos.

Ver [GUIA_FACIL.md](GUIA_FACIL.md) para instrucciones paso a paso pensadas para
usuarios no tecnicos.

---

## Creditos

Este proyecto esta construido sobre **[MarkItDown](https://github.com/microsoft/markitdown)**,
una herramienta open source desarrollada por **Microsoft**.

Todo el credito del motor de conversion pertenece al equipo de Microsoft y sus colaboradores.
Este repositorio unicamente agrega:
- Un script de conversion masiva (`convert_all.py`)
- Un script de limpieza segura (`clean_folder.py`)
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
