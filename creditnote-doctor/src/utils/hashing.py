
import hashlib

def sha256_hex(text: str, salt: str = "") -> str:
    h = hashlib.sha256((salt + text).encode("utf-8"))
    return h.hexdigest()
