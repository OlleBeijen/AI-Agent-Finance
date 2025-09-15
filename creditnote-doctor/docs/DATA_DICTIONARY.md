
# Data Dictionary (MVP)
## invoices.csv
- invoice_id (str)
- line_id (str)
- product_id (str)
- customer_id (str)
- order_id (str)
- quantity (float)
- unit_price (float)
- delivery_date (YYYY-MM-DD)
- po_reference (str)

## credit_notes.csv
- credit_note_id (str)
- line_id (str)
- source_invoice_id (str)
- product_id (str)
- customer_id (str)
- order_id (str)
- quantity (float)
- unit_price (float)
- reason_text (str)
- po_reference (str)
