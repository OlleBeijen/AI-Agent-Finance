
from .hashing import sha256_hex

def mask_customer_id(customer_id: str, salt: str) -> str:
    return sha256_hex(customer_id, salt)[:10]
