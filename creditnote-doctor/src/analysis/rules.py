
import pandas as pd
from ..config import AppConfig

def detect_root_causes(data: dict, cfg: AppConfig) -> pd.DataFrame:
    credit = data["credit_notes"].copy()
    inv = data["invoices"].copy()
    orders = data["orders"].copy()

    # Zorg voor kolommen
    for df in (credit, inv, orders):
        df.columns = [c.lower() for c in df.columns]

    # Baseline joins
    merged = credit.merge(inv, left_on=["source_invoice_id","product_id","customer_id"], right_on=["invoice_id","product_id","customer_id"], how="left", suffixes=("_cred","_inv"))
    merged = merged.merge(orders, left_on=["order_id","product_id"], right_on=["order_id","product_id"], how="left", suffixes=("","_ord"))

    # Heuristieken
    tol_pct = float(cfg.analysis.get("price_tolerance_pct", 1.0))
    delivery_tol = int(cfg.analysis.get("delivery_tolerance_days", 1))

    def price_mismatch(r):
        try:
            up_c = float(r.get("unit_price_cred", r.get("unit_price_x", 0.0)))
            up_i = float(r.get("unit_price_inv", r.get("unit_price_y", 0.0)))
            if up_i == 0:
                return False
            diff_pct = abs(up_c - up_i) / abs(up_i) * 100.0
            return diff_pct > tol_pct
        except Exception:
            return False

    def qty_mismatch(r):
        try:
            qc = abs(float(r.get("quantity_cred", r.get("quantity_x", 0.0))))
            qi = float(r.get("quantity_inv", r.get("quantity_y", 0.0)))
            return qc != qi
        except Exception:
            return False

    def delivery_mismatch(r):
        try:
            dd = str(r.get("delivery_date_ord", r.get("delivery_date", ""))) or ""
            ad = str(r.get("delivery_date_inv", r.get("delivery_date_y", ""))) or ""
            if not dd or not ad:
                return False
            from datetime import datetime
            fmt = "%Y-%m-%d"
            d1 = datetime.strptime(dd[:10], fmt)
            d2 = datetime.strptime(ad[:10], fmt)
            return abs((d2 - d1).days) > delivery_tol
        except Exception:
            return False

    def reference_error(r):
        po = str(r.get("po_reference", "")) or ""
        return po.strip() == ""

    causes = []
    for _, r in merged.iterrows():
        cause = None
        if price_mismatch(r):
            cause = "prijs"
        elif qty_mismatch(r):
            cause = "hoeveelheid"
        elif delivery_mismatch(r):
            cause = "leverdatum"
        elif reference_error(r):
            cause = "referentie"
        else:
            cause = "anders"
        causes.append(cause)

    merged["root_cause"] = causes
    needed = ["credit_note_id","line_id","source_invoice_id","product_id","customer_id","order_id",
              "quantity_cred","unit_price_cred","unit_price_inv","po_reference","root_cause"]
    # Sommige kolommen kunnen anders heten; vul aan
    for c in needed:
        if c not in merged.columns:
            merged[c] = None
    return merged
