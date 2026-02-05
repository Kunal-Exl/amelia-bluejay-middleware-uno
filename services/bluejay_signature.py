import os
import hmac
import hashlib
import requests
import urllib3
from dotenv import load_dotenv

load_dotenv()

def verify_bluejay_signature(raw_body: bytes, received_signature: str) -> bool:
    secret = os.getenv("BLUEJAY_WEBHOOK_SECRET")

    print("sign:",secret)

    if not secret:
        raise RuntimeError("BLUEJAY WEBHOOK SECRET not set")
    
    if received_signature.startswith("sha256="):
        received_signature =received_signature.replace("sha256=","")
    
    computed = hmac.new(
        key=secret.encode("utf-8"),
        msg=raw_body,
        digestmod=hashlib.sha256
    ).hexdigest()

    return hmac.compare_digest(computed, received_signature)