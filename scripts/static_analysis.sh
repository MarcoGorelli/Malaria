#!/bin/bash

flake8 --max-line-length=100
black . --check
pylint src app.py
mypy app.py src --ignore-missing-imports
