# =============================================================================
# Script to build the package into an executable with pyinstaller.
# =============================================================================
python3 -m pip install pyinstaller
python3 -m pip install -e .

pyinstaller \
    -F \
    -n swiss-1.0.0 \
    --hidden-import copier \
    --hidden-import black \
    --hidden-import isort \
    --hidden-import ruff \
    --hidden-import jinja2_ansible_filters \
    --optimize 1 \
    src/swiss/__main__.py
