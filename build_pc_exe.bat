@echo off
setlocal
cd /d "%~dp0"

where python >nul 2>nul
if errorlevel 1 (
  echo Python nao foi encontrado no PATH.
  exit /b 1
)

if not exist .venv (
  echo Criando ambiente virtual...
  python -m venv .venv
)

call .venv\Scripts\activate
python -m pip install --upgrade pip
python -m pip install -r backend\requirements.txt

cd backend
pyinstaller --onefile --name PC --distpath ..\dist --workpath ..\build pc_launcher.py

echo.
echo Build do executavel concluido.
echo Arquivo gerado em: %~dp0dist\PC.exe
pause
