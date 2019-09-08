#!/bin/bash

flake8 --max-line-length=100
black src --check
pylint src app.py
