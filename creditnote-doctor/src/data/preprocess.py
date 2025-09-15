
import pandas as pd

def normalize_columns(df: pd.DataFrame) -> pd.DataFrame:
    # Lowercase, strip spaces, replace spaces with underscores
    df = df.copy()
    df.columns = [c.strip().lower().replace(" ", "_") for c in df.columns]
    return df

def to_numeric(df: pd.DataFrame, cols: list[str]) -> pd.DataFrame:
    df = df.copy()
    for c in cols:
        df[c] = pd.to_numeric(df[c], errors="coerce")
    return df
