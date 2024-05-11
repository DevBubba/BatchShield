@echo off
color a
title BatchShield Module Installer - Initializing...


set "version=1.0"

:updateCheck
curl -o latest_version.txt https://raw.githubusercontent.com/DevBubba/BatchShield/main/version.txt > nul 2>&1
set /p latest_version=<latest_version.txt
del latest_version.txt

if "%latest_version%" GTR "%version%" (
	title BatchShield Module Installer - Updating...
	echo [+] Your Current Version of BatchShield Is Out-Dated!
	echo.
	echo.[+] BatchShield Module Installer Version %latest_version% Is Now Available!"
	echo.
    echo [+] Updating Installer...
    echo.
	timeout /t 3 > nul
    curl -o "%~f0.tmp" https://raw.githubusercontent.com/DevBubba/BatchShield/main/installer.bat > nul 2>&1
    move /y "%~f0.tmp" "%~f0" > nul 2>&1
    echo [+] Installer Updated Successfully To Version %latest_version%!
	echo [+] Press Any Key To Continue...
	pause > nul
    echo.
) else (
	echo [+] No Updates Found!
)

:pythonCheck
where python >nul 2>&1
if errorlevel 1 (
	title BatchShield Module Installer - Error!
    echo.
    echo [-] Python Is Not Installed On This System!
    echo.
    echo [+] Please Install Python V3.0+ And Run This Script Again!
    echo.
    pause
    exit /b
)

:requirementsFileCheck
if not exist requirements.txt (
	title BatchShield Module Installer - Downloading Requirements...
    echo.
    echo [-] requirements.txt Not Found!
    echo.
    echo [+] Downloading requirements.txt...
    echo.
    curl -o requirements.txt https://raw.githubusercontent.com/DevBubba/BatchShield/main/requirements.txt > nul 2>&1
    timeout /t 2 > nul
    echo [+] Successfully Completed Download!
)

:confirmInstall
title BatchShield Module Installer - Installing Modules...
echo.
echo [+] Installing All Required Modules...
echo.
echo [+] Please Wait...

pip install -r requirements.txt > nul 2>&1
    
title BatchShield Module Installer - Done!
echo.
echo [+] Successfully Installed All Required Modules!
echo.

echo [+] Press Any Key To Continue...
pause > nul
