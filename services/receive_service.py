import os
import time
import requests
import urllib3
from dotenv import load_dotenv

load_dotenv()
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

BASE_CONVERSATION_URL = os.getenv("BASE_CONVERSATION_URL")

def poll_response(token: str, session_Id: str, max_retries: int = 5 ):
    url = f"{BASE_CONVERSATION_URL}/{session_Id}/poll"

    headers = {
        "Content-Type":"application/json",
        "X-Amelia-Rest-Token":token
    }

    for attempet in range(max_retries):
        response = requests.post(url ,json={}, headers=headers , timeout=10, verify=False)
    
        if not response.ok:
            raise Exception(
                f"POLL message failed: {response.status_code} - {response.text}"
            )
        
        data = response.json()

        # if data.get("messageText"):
        #     return data["messageText"]
        if isinstance(data, list) and len(data) > 0:
            return data[0].get("messageText")

        # if isinstance(data, list):
        #     message= []
        #     for msg in data:
        #         if isinstance(msg, dict) and "messageText" is  msg:
        #             message.append(msg["messageText"])
        #     if message:
        #             return message

        time.sleep(1)

    print("Inside Poll Function")

    return[]