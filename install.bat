@echo off
color c
title Batch Obfuscator V2.2 - Installing Requirements...

echo.
echo Installing Requirements...
echo.

pip install -r requirements.txt

title Batch Obfuscater V2.2 - Succsesfully Installed Requirements

echo.
echo.
echo Succsesfully Installed Requirements! Do Not Close Out Of This Tab Please Wait 5 Seconds Or Press Any Key To Continue!
echo.

TIMEOUT /T 5

start /b "" cmd /c del "%~f0"&exit /b
