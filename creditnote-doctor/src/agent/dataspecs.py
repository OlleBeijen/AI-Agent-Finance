
# Beschrijving van minimale kolommen per CSV (MVP)
INVOICES_REQUIRED = ["invoice_id","line_id","product_id","customer_id","order_id","quantity","unit_price","delivery_date","po_reference"]
CREDITS_REQUIRED  = ["credit_note_id","line_id","source_invoice_id","product_id","customer_id","order_id","quantity","unit_price","reason_text","po_reference"]
ORDERS_REQUIRED   = ["order_id","product_id","customer_id","requested_date","delivery_date","quantity","po_reference"]
CUSTOMERS_REQUIRED= ["customer_id","customer_name","segment"]
PRODUCTS_REQUIRED = ["product_id","sku","product_name","price_list"]
