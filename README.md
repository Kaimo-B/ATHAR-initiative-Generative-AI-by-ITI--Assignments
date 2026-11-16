# Assignment 1: NASA API

This Python program requests an asteroid from NASA's Near Earth Object API,
reads the JSON response into a small class, and prints a summary.

In the VS Code PowerShell terminal, run:

```powershell
py -3.14 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
if (-not (Test-Path .env)) { Copy-Item .env.example .env }
.\.venv\Scripts\python.exe "assignment 1.py"
```

The `.env` file starts with NASA's public `DEMO_KEY`, which has usage limits.

I am using a demo key for simplicity, However:
For your own key, register at https://api.nasa.gov/ and replace the value in
`.env`. The program reads `.env` from the same folder as the Python file.
Both `.env` and `.venv` are ignored by Git; do not commit your API key.

To run it again later, use the last command above. You can also activate the
environment with `.\.venv\Scripts\Activate.ps1` and run
`python "assignment 1.py"`.
