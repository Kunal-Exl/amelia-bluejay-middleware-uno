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
        # print("DATA",data[0])

        # if data.get("messageText"):
        #     return data["messageText"]

        # if not isinstance(data, list):
        #     time.sleep(1)
        #     continue



        # if isinstance(data, list) and len(data) > 0:
        #     return data[0].get("messageText")
        
        for msg in reversed(data):
            if(
                msg.get("ameliaMessageType") == "OutboundTextMessage"
                and msg.get("speechMessageText")
                and msg.get("sourceUserType") == "Amelia"
            ):
                return msg.get("speechMessageText")

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