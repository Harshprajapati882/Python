install:
	python -m venv .venv
	. .venv/bin/activate && python -m pip install --upgrade pip
	@if [ -f requirements.txt ]; then . .venv/bin/activate && pip install -r requirements.txt; fi

install-windows:
	powershell -NoProfile -Command "python -m venv .venv; .\.venv\Scripts\Activate.ps1; python -m pip install --upgrade pip; if (Test-Path requirements.txt) { pip install -r requirements.txt }"
