@echo off
if exist .venv\Scripts\python (
  .venv\Scripts\python "space_blaster.py"
) else (
  python "space_blaster.py"
)
