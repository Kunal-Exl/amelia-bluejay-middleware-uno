import os
import requests
import urllib3
from dotenv import load_dotenv

load_dotenv()
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

AUTH_URL = os.getenv("AUTH_URl")
username = os.getenv("username")
password = os.getenv("password")


def get_auth_token():
    payload = {
        "ameliaUrl":"https://exl.partners.amelia.com/Amelia/",
        "username": "kunal.sonawane@exlservice.com",
        "password": "xiJRdnOOBPkahJ@1"
    }

    headers = {
        "Content-Type": "application/json"
    }

    response = requests.post(AUTH_URL, json=payload, headers=headers , timeout=10, verify=False)

    if not response.ok:
        raise Exception(f"Auth failed: {response.text}")
    
    data = response.json()

    return data["token"]

    # fake_token = "mock-auth-token-12345"

    # return fake_token