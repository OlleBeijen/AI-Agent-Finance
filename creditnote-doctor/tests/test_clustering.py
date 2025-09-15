
import pandas as pd
from src.analysis.clustering import cluster_failure_patterns

def test_cluster():
    df = pd.DataFrame({
        "root_cause":["prijs"]*5 + ["hoeveelheid"]*5,
        "reason_text":["test"]*10,
        "product_id":["P1"]*10,
        "customer_id":["C1"]*10
    })
    out = cluster_failure_patterns(df, by="product_id")
    assert "cluster" in out.columns
