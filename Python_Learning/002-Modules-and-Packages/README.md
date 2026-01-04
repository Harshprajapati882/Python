# Pips & Modules — Notes and Examples

## Overview

This document covers the essential topics for working with Python packages and modules and using `pip` and virtual environments. It includes commands, concepts, and runnable examples in `main.py` and the example package `mypkg`.

## Topics to Learn

- **pip basics**: install, uninstall, list, show, search
- **Virtual environments**: `venv`, `virtualenv`, `pipenv`, `poetry`
- **Requirements management**: `requirements.txt`, `pip freeze` and `pip install -r`
- **Creating modules & packages**: `.py` modules, `__init__.py`, package structure, relative vs absolute imports
- **Editable installs & development workflows**: `pip install -e .`, `pyproject.toml`, `setup.cfg`
- **Publishing**: building wheels, `twine upload` (high level)
- **Dependency tools**: `pipx`, `venv`, `pip-tools`, `poetry` basics
- **Security & reproducibility**: pinning versions, hashes, virtual env per-project

## Common pip & venv Commands

```bash
# create virtual env (recommended per project)
python -m venv .venv
source .venv/bin/activate   # Linux/macOS
.venv\Scripts\activate     # Windows (PowerShell) - use appropriate shell

# install packages
pip install requests

# freeze current env to requirements
pip freeze > requirements.txt

# install from requirements
pip install -r requirements.txt

# install editable package for development
pip install -e .

# list installed packages
pip list

# show package info
pip show requests

# install a package globally with pipx (CLI tools)
pipx install black
```

## Creating Modules and Packages

- A module is a single `.py` file. Example: `utils.py`.
- A package is a directory with an `__init__.py` (can be empty) and modules.
- Use absolute imports for clarity; use relative imports within packages when appropriate.

Example package layout (this repo contains `mypkg`):

```
002-Modules-and-Packages/
  README.md
  main.py       # runnable examples
  mypkg/
    __init__.py
    math_ops.py
```

## Example: `mypkg` (local package)

- `mypkg/math_ops.py` exports `add` and `mul` functions.
- `mypkg/__init__.py` re-exports the simple API.

Use from the project root:

```bash
python main.py
```

Or open `main.py` to see example usage.

## Publishing & Packaging (brief)

- Prefer `pyproject.toml` for modern projects. Use `setuptools`/`flit`/`poetry` as backend.
- Build artifacts:
  - `python -m build` (produces wheel and sdist)
  - `twine upload dist/*` to publish (use credentials securely)

## Best Practices

- Use a venv per project and commit only `requirements.txt` or a lock file.
- Pin direct dependencies; use lock files for reproducible installs.
- Prefer editable installs during development: `pip install -e .`.
- Avoid running `pip` as root; use venv or user install.

## Links & Further Reading

- Official pip docs: https://pip.pypa.io/
- Packaging guide: https://packaging.python.org/

---

## Quick Try (commands)

From the `002-Modules-and-Packages` folder run:

```bash
python -m venv .venv
source .venv/bin/activate
python main.py
```

This will run the example script which imports the local `mypkg` package.

---

File references:

- Pips examples: [main.py](main.py)
- Example package: [mypkg/__init__.py](mypkg/__init__.py) and [mypkg/math_ops.py](mypkg/math_ops.py)
