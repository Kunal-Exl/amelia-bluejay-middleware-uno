import os
import requests
import urllib3
from dotenv import load_dotenv

load_dotenv()
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

BASE_CONVERSATION_URL = os.getenv("BASE_CONVERSATION_URL")

def send_message(token: str, session_Id: str, message: str):
    url = f"{BASE_CONVERSATION_URL}/{session_Id}/send"

    headers = {
        "Content-Type": "application/json",
        "X-Amelia-Rest-Token":token
    }

    payload = {
        "messageText": message
    }
    
    response = requests.post(url ,json=payload, headers=headers , timeout=10, verify=False)

    if not response.ok:
        raise Exception(
            f"SEND message failed: {response.status_code} - {response.text}"
        )
    
    data = response.json()

    return data if response.text else {"status":"sent"}