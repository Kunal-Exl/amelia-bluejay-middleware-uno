import os
import requests
import urllib3
from dotenv import load_dotenv

load_dotenv()
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

CHAT_INIT_URL = os.getenv("CHAT_INIT_URL")

def initiate_chat(token):
    headers = {
        "Content-Type":"application/json",
        "X-Amelia-Rest-Token":token
    }

    payload = {
        "deliveryMode": "POLLING",
        "domain": "exl",
        "webhookUrl": "https://exl.partners.amelia.com/webhook/amelia/",
        "secret": "restchat"
    }

    response = requests.post(CHAT_INIT_URL ,json=payload, headers=headers , timeout=10, verify=False)

    data = response.json()

    return data["sessionId"]