# Assignment 1: NASA API

This Python program requests an asteroid from NASA's Near Earth Object API,
reads the JSON response into a small class, and prints a summary.

From the repository root, open the VS Code PowerShell terminal and run:

```powershell
py -3.14 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r .\assignment_1\requirements.txt
if (-not (Test-Path .\assignment_1\.env)) { Copy-Item .\assignment_1\.env.example .\assignment_1\.env }
.\.venv\Scripts\python.exe .\assignment_1\assignment_1.py
```

The `.env.example` file contains NASA's public `DEMO_KEY`, which has usage limits.

For your own key, register at https://api.nasa.gov/ and replace the value in
`assignment_1\.env`. The program reads `.env` from the same folder as the
Python file. Both `.env` and `.venv` are ignored by Git; do not commit your API
key.

To run it again later, use the last command above. You can also activate the
environment from the repository root with `.\.venv\Scripts\Activate.ps1` and
run `python .\assignment_1\assignment_1.py`.
