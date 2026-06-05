#!/usr/bin/env bash
if [ -f .venv/bin/python ]; then
  .venv/bin/python "space_blaster.py"
else
  python3 "space_blaster.py"
fi
