
import pandas as pd
from src.analysis.kpi import compute_kpis

def test_kpis():
    df = pd.DataFrame({
        "credit_note_id":["A","A","B"],
        "quantity_cred":[1,2,3],
        "unit_price_cred":[10.0,10.0,5.0],
        "root_cause":["prijs","hoeveelheid","anders"]
    })
    k = compute_kpis(df)
    assert k["n_credit_lines"] == 3
    assert k["n_credit_notes"] == 2
