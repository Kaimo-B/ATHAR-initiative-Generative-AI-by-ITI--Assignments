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

The `.env.example` file uses NASA's shared `DEMO_KEY` for initial testing. NASA
limits this key to 30 requests per IP address per hour and 50 per day. A
personal API key has a higher default limit of 1,000 requests per hour.

To avoid the shared demo-key limit, register for a personal key at
https://api.nasa.gov/ and replace `DEMO_KEY` in `assignment_1\.env` with your
key. Keep it private: `.env` and `.venv` are ignored by Git, so do not commit
your API key. NASA applies the personal-key limit across its APIs. If the
program reports HTTP 429, stop retrying and wait for the rate limit to reset;
the program will also suggest this when it detects the limit response.

To run it again later, use the last command above. You can also activate the
environment from the repository root with `.\.venv\Scripts\Activate.ps1` and
run `python .\assignment_1\assignment_1.py`.
