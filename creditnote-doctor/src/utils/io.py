
from pathlib import Path
import pandas as pd
from typing import Optional
import os

def ensure_dirs(cfg):
    cfg.paths.data.mkdir(parents=True, exist_ok=True)
    cfg.paths.reports.mkdir(parents=True, exist_ok=True)
    cfg.paths.indexes.mkdir(parents=True, exist_ok=True)

def save_uploaded_file(file, dest: Path) -> Path:
    dest.parent.mkdir(parents=True, exist_ok=True)
    with open(dest, "wb") as f:
        f.write(file.getbuffer())
    return dest

def load_csv_safe(path: Path) -> Optional[pd.DataFrame]:
    if not path.exists():
        return None
    try:
        return pd.read_csv(path)
    except Exception:
        return None
