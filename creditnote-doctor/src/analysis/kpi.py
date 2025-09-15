
import pandas as pd

def compute_kpis(df: pd.DataFrame) -> dict:
    n_lines = len(df)
    n_notes = df["credit_note_id"].nunique()
    est_recovery = (df.get("quantity_cred", 0).astype(float) * df.get("unit_price_cred", 0).astype(float)).abs().sum()
    by_cause = df["root_cause"].value_counts().to_dict()
    return {
        "n_credit_lines": n_lines,
        "n_credit_notes": n_notes,
        "estimated_recovery_eur": float(est_recovery),
        "by_cause": by_cause
    }
