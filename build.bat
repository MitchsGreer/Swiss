ECHO OFF
@REM =============================================================================
@REM Script to build the package into an executable with pyinstaller.
@REM =============================================================================
python -m pip install pyinstaller
python -m pip install -e .

pyinstaller ^
    -F ^
    -n swiss-1.1.0 ^
    --hidden-import copier ^
    --hidden-import black ^
    --hidden-import isort ^
    --hidden-import ruff ^
    --hidden-import jinja2_ansible_filters ^
    --optimize 1 ^
    src/swiss/__main__.py
