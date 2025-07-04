@echo off
echo Building World Class Tweaks...
pip install pyinstaller
pyinstaller --onefile --windowed --icon=assets\logo.ico WorldClassTweaks.py
pause
