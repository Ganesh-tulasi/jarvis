@echo off
echo ==========================================
echo JARVIS Assistant - Windows Setup
echo ==========================================

echo [1/3] Creating Python Virtual Environment...
python -m venv venv

echo [2/3] Activating Virtual Environment...
call venv\Scripts\activate.bat

echo [3/3] Upgrading pip and installing requirements...
python -m pip install --upgrade pip
pip install -r requirements.txt

echo.
if not exist .env (
    echo [*] Creating .env file from .env.example...
    copy .env.example .env
)

echo.
echo Setup Complete!
echo You can now start JARVIS by running: 
echo   ^> venv\Scripts\activate
echo   ^> python main.py
echo.
pause
