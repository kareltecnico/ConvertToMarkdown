#!/bin/bash
# ============================================================
#  ConvertToMarkdown - Launcher (macOS)
#  Activa el entorno virtual y presenta el menu de opciones
# ============================================================

# Cambiar al directorio donde esta el script (necesario al hacer doble clic)
cd "$(dirname "$0")"

# Colores ANSI
GREEN="\033[0;32m"
CYAN="\033[0;36m"
YELLOW="\033[1;33m"
RED="\033[0;31m"
RESET="\033[0m"

close_terminal_window() {
    if [ "${TERM_PROGRAM:-}" = "Apple_Terminal" ]; then
        (sleep 0.2; osascript -e 'tell application "Terminal" to close front window') >/dev/null 2>&1 &
    fi
}

# Activar el entorno virtual
if [ -f ".venv/bin/activate" ]; then
    source ".venv/bin/activate"
else
    echo -e "${RED}[ERROR] No se encontro el entorno virtual (.venv).${RESET}"
    echo "Ejecuta primero: python3 -m venv .venv && .venv/bin/pip install markitdown[pdf,docx,pptx,xlsx,xls,outlook,audio-transcription]"
    echo ""
    read -p "Presiona Enter para salir..."
    exit 1
fi

menu() {
    clear
    echo ""
    echo -e "${GREEN}  +------------------------------------------------------+"
    echo -e "  |       ConvertToMarkdown  -  Menu Principal           |"
    echo -e "  +------------------------------------------------------+"
    echo -e "  |                                                      |"
    echo -e "  |   [1]  Convertir archivos a Markdown                 |"
    echo -e "  |                                                      |"
    echo -e "  |   [2]  Abrir carpeta INPUT  (archivos de entrada)    |"
    echo -e "  |                                                      |"
    echo -e "  |   [3]  Abrir carpeta OUTPUT (Markdown generados)     |"
    echo -e "  |                                                      |"
    echo -e "  |   [0]  Salir                                         |"
    echo -e "  |                                                      |"
    echo -e "  +------------------------------------------------------+${RESET}"
    echo ""
}

while true; do
    menu
    read -p "  Elige una opcion: " OPCION

    case "$OPCION" in

        1)
            clear
            echo -e "${CYAN}"
            echo "  ================================================"
            echo "   Convirtiendo archivos a Markdown..."
            echo "  ================================================"
            echo -e "${RESET}"
            python convert_all.py
            echo ""
            echo -e "${GREEN}  ================================================"
            echo "   Proceso finalizado."
            echo -e "  ================================================${RESET}"
            echo ""
            read -p "  Presiona Enter para volver al menu..."
            ;;

        2)
            open "$(pwd)/input"
            ;;

        3)
            open "$(pwd)/output"
            ;;

        0)
            clear
            echo ""
            echo "  Hasta luego!"
            echo ""
            close_terminal_window
            exit 0
            ;;

        *)
            echo ""
            echo -e "${YELLOW}  [!] Opcion no valida. Intenta de nuevo.${RESET}"
            sleep 2
            ;;
    esac
done
