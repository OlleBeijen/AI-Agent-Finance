
from pathlib import Path
import pandas as pd
from typing import Optional

def load_csv(path: Path) -> pd.DataFrame:
    return pd.read_csv(path)

def load_csv_safe(path: Path) -> Optional[pd.DataFrame]:
    try:
        return pd.read_csv(path)
    except Exception:
        return None

def load_all_inputs(data_dir: Path) -> Optional[dict]:
    files = {
        "invoices": data_dir / "invoices.csv",
        "credit_notes": data_dir / "credit_notes.csv",
        "orders": data_dir / "orders.csv",
        "customers": data_dir / "customers.csv",
        "products": data_dir / "products.csv",
    }
    out = {}
    for k, p in files.items():
        if not p.exists():
            return None
        out[k] = pd.read_csv(p)
    return out
