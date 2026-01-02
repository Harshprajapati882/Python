#!/usr/bin/env pwsh
python -m venv .venv
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass -Force -ErrorAction SilentlyContinue
. .\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
if (Test-Path requirements.txt) {
    pip install -r requirements.txt
}

Write-Host "Virtual environment created in .venv"
Write-Host "Activate with: .\.venv\Scripts\Activate.ps1"
