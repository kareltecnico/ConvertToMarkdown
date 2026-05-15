@echo off
title ConvertToMarkdown - Launcher
color 0A

:: Activar el entorno virtual
call "%~dp0.venv\Scripts\activate.bat"

:MENU
cls
color 0A
echo.
echo  +------------------------------------------------------+
echo  ^|       ConvertToMarkdown  -  Menu Principal           ^|
echo  +------------------------------------------------------+
echo  ^|                                                      ^|
echo  ^|   [1]  Convertir archivos a Markdown                 ^|
echo  ^|                                                      ^|
echo  ^|   [2]  Abrir carpeta INPUT  (archivos de entrada)    ^|
echo  ^|                                                      ^|
echo  ^|   [3]  Abrir carpeta OUTPUT (Markdown generados)     ^|
echo  ^|                                                      ^|
echo  ^|   [4]  Limpiar carpeta INPUT                         ^|
echo  ^|                                                      ^|
echo  ^|   [5]  Limpiar carpeta OUTPUT                        ^|
echo  ^|                                                      ^|
echo  ^|   [0]  Salir                                         ^|
echo  ^|                                                      ^|
echo  +------------------------------------------------------+
echo.
set OPCION=
set /p OPCION=  Elige una opcion: 

if "%OPCION%"=="1" goto CONVERTIR
if "%OPCION%"=="2" goto ABRIR_INPUT
if "%OPCION%"=="3" goto ABRIR_OUTPUT
if "%OPCION%"=="4" goto LIMPIAR_INPUT
if "%OPCION%"=="5" goto LIMPIAR_OUTPUT
if "%OPCION%"=="0" goto SALIR

echo.
echo  [!] Opcion no valida. Intenta de nuevo.
timeout /t 2 >nul
goto MENU

:CONVERTIR
cls
color 0B
echo.
echo  ================================================
echo   Convirtiendo archivos a Markdown...
echo  ================================================
echo.
python "%~dp0convert_all.py"
echo.
echo  ================================================
echo   Proceso finalizado.
echo  ================================================
echo.
pause
goto MENU

:ABRIR_INPUT
explorer "%~dp0input"
goto MENU

:ABRIR_OUTPUT
explorer "%~dp0output"
goto MENU

:LIMPIAR_INPUT
cls
color 0E
echo.
echo  ================================================
echo   Limpiar carpeta INPUT
echo  ================================================
echo.
choice /c SN /n /m "  Esto borrara tus archivos de entrada. Continuar? [S/N]: "
if errorlevel 2 goto MENU
python "%~dp0clean_folder.py" input
echo.
pause
goto MENU

:LIMPIAR_OUTPUT
cls
color 0E
echo.
echo  ================================================
echo   Limpiar carpeta OUTPUT
echo  ================================================
echo.
choice /c SN /n /m "  Esto borrara los Markdown generados y reportes. Continuar? [S/N]: "
if errorlevel 2 goto MENU
python "%~dp0clean_folder.py" output
echo.
pause
goto MENU

:SALIR
color 07
cls
echo.
echo  Hasta luego!
echo.
timeout /t 2 >nul
exit
