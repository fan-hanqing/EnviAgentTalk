@echo off
REM ============================================================
REM  Environmental Agent Roundtable - double-click launcher
REM  Starts the backend and opens the browser when it is ready.
REM  Keep this window open; closing it stops the server.
REM ============================================================
chcp 65001 >nul
title Environmental Agent Roundtable - server (keep this window open)
cd /d "%~dp0"

echo.
echo   Environmental Agent Roundtable
echo   folder: %CD%
echo.

REM --- is python on PATH? ------------------------------------
where python >nul 2>nul
if errorlevel 1 (
  echo   [X] Python was not found on PATH.
  echo       Install Python 3.10+ , or open Anaconda Prompt and run:  python app.py
  echo.
  pause
  exit /b 1
)

REM --- are the dependencies installed? ------------------------
python -c "import fastapi, uvicorn, httpx, pydantic" >nul 2>nul
if errorlevel 1 (
  echo   first run: installing dependencies ...
  python -m pip install -r requirements.txt
  if errorlevel 1 (
    echo.
    echo   [X] Install failed. Try running this by hand:
    echo       python -m pip install fastapi uvicorn httpx pydantic
    echo.
    pause
    exit /b 1
  )
  echo   dependencies OK
  echo.
)

REM --- a system proxy breaks a domestic endpoint like DashScope
REM     cleared for this window only; your system settings are untouched
set HTTP_PROXY=
set HTTPS_PROXY=
set http_proxy=
set https_proxy=

REM --- open the browser as soon as /health answers ------------
start "" /min powershell -NoProfile -Command "for($i=0;$i -lt 60;$i++){try{$null=Invoke-WebRequest -UseBasicParsing 'http://127.0.0.1:8000/health' -TimeoutSec 1; Start-Process 'http://127.0.0.1:8000'; break}catch{Start-Sleep -Milliseconds 500}}"

echo   starting server - the browser opens by itself in a few seconds
echo   api keys live in api.json - edit them at "Set API" in the page header
echo   press Ctrl+C to stop
echo.

python app.py

REM --- only reached if the server exits or crashes ------------
echo.
echo   server stopped.
pause
