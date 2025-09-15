
import pandas as pd
from src.analysis.rules import detect_root_causes
from src.config import AppConfig

def test_detect_root_causes_price():
    cfg = AppConfig.load()
    data = {
        "credit_notes": pd.DataFrame([{"credit_note_id":"CR1","line_id":"1","source_invoice_id":"INV1","product_id":"P1","customer_id":"C1","order_id":"O1","quantity":1,"unit_price":110,"reason_text":"prijs","po_reference":"PO-1"}]),
        "invoices": pd.DataFrame([{"invoice_id":"INV1","line_id":"1","product_id":"P1","customer_id":"C1","order_id":"O1","quantity":1,"unit_price":100,"delivery_date":"2025-01-01","po_reference":"PO-1"}]),
        "orders": pd.DataFrame([{"order_id":"O1","product_id":"P1","customer_id":"C1","requested_date":"2025-01-01","delivery_date":"2025-01-01","quantity":1,"po_reference":"PO-1"}]),
        "customers": pd.DataFrame([{"customer_id":"C1","customer_name":"X","segment":"R"}]),
        "products": pd.DataFrame([{"product_id":"P1","sku":"S","product_name":"Y","price_list":"STD"}]),
    }
    df = detect_root_causes(data, cfg)
    assert "root_cause" in df.columns
