# ConvertToMarkdown - Guia facil

Esta guia es para usar ConvertToMarkdown sin saber Git ni programacion.

## Que hace?

Convierte archivos como PDF, Word, Excel, PowerPoint, HTML, CSV, JSON y otros a
Markdown (`.md`), un formato de texto muy util para herramientas de IA.

## 1. Descargar

1. Abre esta pagina: https://github.com/kareltecnico/ConvertToMarkdown
2. Haz clic en el boton verde **Code**
3. Haz clic en **Download ZIP**
4. Descomprime el ZIP
5. Abre la carpeta `ConvertToMarkdown`

## 2. Instalar una sola vez

### Mac

1. Abre la app **Terminal**
2. Escribe `cd `, con un espacio al final
3. Arrastra la carpeta `ConvertToMarkdown` a la ventana de Terminal
4. Presiona Enter
5. Ejecuta estos comandos:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
chmod +x ConvertToMarkdown.command
```

### Windows

1. Abre **PowerShell**
2. Escribe `cd `, con un espacio al final
3. Arrastra la carpeta `ConvertToMarkdown` a PowerShell
4. Presiona Enter
5. Ejecuta estos comandos:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate
pip install -r requirements.txt
```

## 3. Convertir archivos

1. Copia tus archivos dentro de la carpeta `input`
2. En Mac, haz doble clic en `ConvertToMarkdown.command`
3. En Windows, haz doble clic en `ConvertToMarkdown.bat`
4. Presiona `1` y Enter
5. Al terminar, presiona Enter para volver al menu
6. Abre la carpeta `output`

Tus archivos Markdown apareceran en `output`.

## Menu

- `1`: convertir archivos a Markdown
- `2`: abrir carpeta `input`
- `3`: abrir carpeta `output`
- `4`: limpiar carpeta `input`
- `5`: limpiar carpeta `output`
- `0`: salir

Las opciones `4` y `5` piden confirmacion antes de borrar.

## Consejos

- Puedes poner subcarpetas dentro de `input`.
- Si un archivo no cambio, ConvertToMarkdown no lo convierte otra vez.
- El reporte de la ultima ejecucion queda en `output/conversion_report.txt`.
- Si un PDF escaneado sale vacio, probablemente necesita OCR primero.

## Si algo falla

Revisa que:

- Python este instalado.
- El entorno `.venv` exista.
- Hayas ejecutado `pip install -r requirements.txt`.
- El archivo se pueda abrir normalmente en tu computadora.
