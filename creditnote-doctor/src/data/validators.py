
import pandas as pd

def validate_required_columns(df: pd.DataFrame, required: list[str]) -> list[str]:
    missing = [c for c in required if c not in df.columns]
    return missing
