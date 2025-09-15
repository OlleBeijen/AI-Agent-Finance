
import pandas as pd

def match_credit_to_invoice(credit: pd.DataFrame, invoices: pd.DataFrame):
    # Match op (source_invoice_id, product_id, customer_id), anders fallback op po_reference + product
    credit = credit.copy()
    invoices = invoices.copy()
    on_cols = ["source_invoice_id", "product_id", "customer_id"]
    merged = credit.merge(invoices, left_on=on_cols, right_on=["invoice_id","product_id","customer_id"], how="left", suffixes=("_credit","_inv"))
    if merged["invoice_id"].isna().any():
        # fallback
        fallback = credit.merge(invoices, left_on=["po_reference","product_id"], right_on=["po_reference","product_id"], how="left", suffixes=("_credit","_inv_fb"))
        merged = merged.combine_first(fallback)
    return merged
