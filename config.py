import os
from pathlib import Path

# Project root directory
PROJECT_ROOT = Path(__file__).parent.absolute()

# Data directory (creates if not exists)
DATA_DIR = PROJECT_ROOT / "data"
DATA_DIR.mkdir(exist_ok=True)

# Inventory file path
INVENTORY_FILE = DATA_DIR / "inventario.json"

# Available bodegas
BODEGAS = ["norte", "centro", "oriente"]

