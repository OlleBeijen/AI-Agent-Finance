
import pandas as pd

def priority_score(df: pd.DataFrame) -> pd.Series:
    # Eenvoudige prioritisering: waarde * frequentie per product/klant
    value = (df.get("quantity_cred", 0).astype(float) * df.get("unit_price_cred", 0).astype(float)).abs()
    return value.rank(pct=True)
