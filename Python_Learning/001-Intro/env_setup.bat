@echo off
python -m venv .venv
call .venv\Scripts\activate
python -m pip install --upgrade pip
if exist requirements.txt (
    pip install -r requirements.txt
)

echo Virtual environment created in .venv
echo Activate with: .venv\Scripts\activate.bat
