@echo off
title JARVIS Launcher
cd /d "%~dp0"
call venv\Scripts\activate.bat
python main.py
