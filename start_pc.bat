@echo off
setlocal
cd /d "%~dp0"

where python >nul 2>nul
if errorlevel 1 (
  echo Python nao foi encontrado no PATH.
  echo Instale Python 3.11+ e tente novamente.
  exit /b 1
)

if not exist .venv (
  echo Criando ambiente virtual...
  python -m venv .venv
)

call .venv\Scripts\activate
python -m pip install --upgrade pip
python -m pip install -r backend\requirements.txt

cd frontend
if not exist node_modules (
  echo Instalando dependencias do frontend...
  npm install
)

cd ..

start "PC Backend" cmd /k "cd /d %~dp0\backend && call ..\.venv\Scripts\activate && uvicorn app.main:app --host 0.0.0.0 --port 8000"
start "PC Frontend" cmd /k "cd /d %~dp0\frontend && npm run dev -- --host 0.0.0.0 --port 5173"

start "PC Browser" http://localhost:5173

echo.
echo PC iniciou.
echo Acesse: http://localhost:5173
pause
