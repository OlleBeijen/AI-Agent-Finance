
from dataclasses import dataclass

@dataclass
class InvoiceLine:
    invoice_id: str
    line_id: str
    product_id: str
    customer_id: str
    order_id: str | None
    quantity: float
    unit_price: float
    delivery_date: str | None
    po_reference: str | None

@dataclass
class CreditLine:
    credit_note_id: str
    line_id: str
    source_invoice_id: str | None
    product_id: str
    customer_id: str
    order_id: str | None
    quantity: float
    unit_price: float
    reason_text: str | None
    po_reference: str | None
