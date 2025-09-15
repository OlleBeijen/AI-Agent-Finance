
import pandas as pd

def build_features(df: pd.DataFrame) -> pd.DataFrame:
    out = df.copy()
    out["abs_value"] = out.get("quantity_cred", 0).astype(float) * out.get("unit_price_cred", 0).astype(float)
    return out
