# Windows — VS Code Python setup

1. Install Python for Windows from https://python.org and check "Add Python to PATH".
2. Install Visual Studio Code: https://code.visualstudio.com/
3. In VS Code, install the **Python** extension (ms-python.python).
4. Open this repository folder in VS Code.
5. Create the virtual environment:
   - Run `env_setup.ps1` in PowerShell or `env_setup.bat` in Command Prompt.
6. Select interpreter: press `Ctrl+Shift+P` → `Python: Select Interpreter` → choose `.venv\Scripts\python.exe`.
7. Recommended (workspace) settings: create `.vscode/settings.json` with:
   ```json
   {
     "python.pythonPath": ".venv\\Scripts\\python.exe",
     "python.terminal.activateEnvironment": true
   }
   ```
8. If using PowerShell, you may need to allow running the activation script: run PowerShell as Admin and set `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`.

See `env_setup.ps1` and `env_setup.bat` for automated steps.
