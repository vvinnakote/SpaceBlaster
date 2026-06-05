#!/usr/bin/env pwsh
python -m venv .venv
.venv\Scripts\python -m pip install --upgrade pip
.venv\Scripts\python -m pip install -r requirements.txt
Write-Host "Virtual environment created in .venv. Activate with: .\\.venv\\Scripts\\Activate.ps1"
