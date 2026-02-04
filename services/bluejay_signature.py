import os
import hmac
import hashlib
import requests
import urllib3
from dotenv import load_dotenv

load_dotenv()

def verify_bluejay_signature(raw_body: bytes, received_signature: str) -> bool:
    secret = os.getenv("BLUEJAY_WEBHOOK_SECRET")

    if not secret:
        raise RuntimeError("BLUEJAY WEBHOOK SECRET not set")
    
    computed = hmac.new(
        key=secret.encode("utf-8"),
        msg=raw_body,
        digestmod=hashlib.sha256
    ).hexdigest()

    return hmac.compare_digest(computed, received_signature)