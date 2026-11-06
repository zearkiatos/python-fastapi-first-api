@echo off

:activate
if exist venv (
    echo Python environment was activated
    call venv\Scripts\activate.bat
) else (
    echo The folder environment doesn't exist
    python3 -m venv venv
    call venv\Scripts\activate.bat
    echo The environment folder was created and the python environment was activated
)
exit /b 0

:install
pip3 install -r requirements.txt
exit /b 0

:run
fastapi dev src/main.py
exit /b 0