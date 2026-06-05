# Space Blaster

Classic Space Blaster game using `turtle` and `pygame` audio.

Quick start

1. Clone the repo:

   git clone <repo-url>
   cd SpaceBlaster

2. Create a virtual environment and install dependencies:

   # Windows (PowerShell)
   .\setup.ps1

   # macOS / Linux
   ./setup.sh

   # Optional manual fallback if you want to do it yourself:
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1      # Windows PowerShell
   source .venv/bin/activate           # macOS / Linux
   python -m pip install --upgrade pip
   python -m pip install -r requirements.txt

   # Quick checks (optional):
   .\.venv\Scripts\python check_env.py

3. Run the game:

   # From an activated virtualenv
   python "space_blaster.py"

Notes
- The game uses the standard library `turtle` (which requires Tcl/Tk support). On most platforms, Python from python.org includes Tcl/Tk. If `turtle` fails, install the OS package that provides `tk` / `tkinter`.
 - Audio and image assets (GIF/MP3/WAV) are located in the `assets/` folder. Keep that folder next to `space_blaster.py`.

Provided helper scripts
- `setup.ps1` — Create venv and install dependencies on Windows (PowerShell).
- `setup.sh` — Create venv and install dependencies on Unix-like systems.
- `run.bat` / `run.sh` — Convenience runner that uses the venv if present.

Using the validator
-------------------
After creating the virtual environment and installing dependencies you can run the quick validator to confirm `tkinter`, `pygame`, and the main assets are available:

PowerShell:

   .\.venv\Scripts\python check_env.py

The script exits with code `0` on success and `1` if any required items are missing.

If you'd like, I can also:
- Add the missing asset files to the repository (GIF/WAV/MP3) if you want them tracked.
 - The main file was renamed to `space_blaster.py` to make running simpler.
