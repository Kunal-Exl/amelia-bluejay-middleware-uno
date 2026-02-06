import os
import requests
from dotenv import load_dotenv

load_dotenv()

BLUEJAY_API_KEY = os.getenv("BLUEJAY_API_KEY")
BLUEJAY_SEND_MESSAGE_URL = os.getenv("BLUEJAY_SEND_MESSAGE_URL")

def send_message_to_bluejay(simulation_result_id:str, message:str, message_id:str, end_conversation:bool = False, end_turn: bool=True):
    if not BLUEJAY_API_KEY:
        raise RuntimeError("BLUEJAY_API_KEY not set")
    
    headers = {
        "Content-Type": "application/json",
        "X-API-Key": BLUEJAY_API_KEY
    }

    payload = {
        "simulation_result_id": simulation_result_id,
        "message": message,
        "message_id": message_id,
        "end_conversation": end_conversation,
        "end_turn": end_turn
    }

    response = requests.post(BLUEJAY_SEND_MESSAGE_URL, json=payload, headers=headers , timeout=10)

    print("Inside BLUE JAY SEND Function")

    response.raise_for_status()
    return response.json()






# DOS

# def send_message_to_bluejay(simulation_result_id:str, message:str, message_id:str, end_conversation:bool = False, end_turn: bool=True):
#     if not BLUEJAY_API_KEY:
#         raise RuntimeError("BLUEJAY_API_KEY not set")
    
#     headers = {
#         "Content-Type": "application/json",
#         "X-API-Key": BLUEJAY_API_KEY
#     }

#     payload = {
#         "simulation_result_id": simulation_result_id,
#         "message": message,
#         "message_id": message_id,
#         "end_conversation": end_conversation,
#         "end_turn": end_turn
#     }

#     response = requests.post(BLUEJAY_SEND_MESSAGE_URL, json=payload, headers=headers , timeout=10)

#     print("Inside BLUE JAY SEND Function")

#     response.raise_for_status()
#     return response.json()