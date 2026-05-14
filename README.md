# IA Helpers - PDF to Markdown Converter

> Herramienta de automatizacion para convertir archivos PDF a Markdown,
> lista para usar con un solo doble clic. Compatible con **Windows** y **macOS**.

---

## Que hace?

Convierte todos los PDFs de la carpeta `input/` a archivos `.md` en `output/`.
El resultado es texto limpio ideal para pipelines de IA, RAG o analisis de documentos.

---

## Inicio Rapido

### Windows

```powershell
# 1. Clonar el repo
git clone https://github.com/kareltecnico/ia-helpers.git
cd ia-helpers

# 2. Crear entorno virtual e instalar dependencias
python -m venv .venv
.\.venv\Scripts\Activate
pip install "markitdown[pdf]"

# 3. Doble clic en IA_Helpers.bat
```

### macOS

```bash
# 1. Clonar el repo
git clone https://github.com/kareltecnico/ia-helpers.git
cd ia-helpers

# 2. Crear entorno virtual e instalar dependencias
python3 -m venv .venv
source .venv/bin/activate
pip install "markitdown[pdf]"

# 3. Dar permiso al launcher (solo la primera vez)
chmod +x IA_Helpers.command

# 4. Doble clic en IA_Helpers.command
```

---

## Uso

1. Copia tus PDFs a la carpeta `input/`
2. Abre el launcher (`IA_Helpers.bat` en Windows / `IA_Helpers.command` en Mac)
3. Presiona `1` para iniciar la conversion
4. Los archivos `.md` apareceran en `output/`

---

## Estructura

```
ia-helpers/
+-- IA_Helpers.bat       <- Launcher Windows
+-- IA_Helpers.command   <- Launcher macOS
+-- convert_all.py       <- Script de conversion
+-- input/               <- PDFs de entrada (ignorados por git)
+-- output/              <- Markdowns de salida (ignorados por git)
+-- docs/
    +-- README.md        <- Documentacion completa
```

---

## Documentacion completa

Ver [docs/README.md](docs/README.md) para instrucciones detalladas de instalacion,
solucion de problemas y referencia de archivos.

---

## Dependencias

- [markitdown](https://github.com/microsoft/markitdown) — Motor de conversion de Microsoft
- pdfminer-six, pdfplumber, pypdfium2 — Motores de lectura de PDF

---

## Licencia

MIT — Libre para uso personal y comercial.
