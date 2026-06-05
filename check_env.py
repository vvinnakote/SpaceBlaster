"""Simple environment validator for the Space Blaster project.

Checks:
- Python version >= 3.8
- Running inside a virtual environment (recommended)
- `tkinter` import
- `pygame` import and version
- presence of `assets/` folder and key asset files

Exit code: 0 on success, 1 on any failure.
"""
import sys
import os
import importlib

MIN_PY = (3, 8)
ASSETS = [
    "assets/ship.gif",
    "assets/bullet.gif",
    "assets/enemy.gif",
    "assets/explosion.gif",
    "assets/small_enemy.gif",
    "assets/space-bg.gif",
    "assets/spship_ambience.mp3",
]

def ok(msg):
    print("[OK] ", msg)

def fail(msg):
    print("[FAIL]", msg)

def main():
    errors = 0

    # Python version
    if sys.version_info >= MIN_PY:
        ok(f"Python {sys.version_info.major}.{sys.version_info.minor} detected")
    else:
        fail(f"Python >= {MIN_PY[0]}.{MIN_PY[1]} required, found {sys.version_info.major}.{sys.version_info.minor}")
        errors += 1

    # virtualenv recommendation
    in_venv = hasattr(sys, 'real_prefix') or (getattr(sys, 'base_prefix', sys.prefix) != sys.prefix)
    if in_venv:
        ok("Running inside a virtual environment")
    else:
        print("[WARN] Not running inside a virtual environment. It's recommended to create one.")

    # tkinter
    try:
        importlib.import_module('tkinter')
        ok('tkinter import OK')
    except Exception as e:
        fail(f'tkinter import failed: {e}')
        errors += 1

    # pygame
    try:
        pg = importlib.import_module('pygame')
        ok(f'pygame import OK (version {getattr(pg, "__version__", "?")})')
    except Exception as e:
        fail(f'pygame import failed: {e}')
        errors += 1

    # assets
    missing = []
    for p in ASSETS:
        if not os.path.exists(p):
            missing.append(p)

    if missing:
        fail('Missing asset files: ' + ', '.join(missing))
        errors += 1
    else:
        ok('All required asset files present (basic check)')

    if errors:
        print(f"\nEnvironment check failed ({errors} issue(s)). See messages above.")
        sys.exit(1)
    else:
        print('\nEnvironment appears ready. You can run:')
        print('  python space_blaster.py')
        sys.exit(0)

if __name__ == '__main__':
    main()
