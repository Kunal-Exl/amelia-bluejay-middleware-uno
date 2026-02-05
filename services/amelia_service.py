from services.auth_service import get_auth_token
from services.chat_service import initiate_chat
from services.message_service import send_message
from services.receive_service import poll_response

def process_with_amelia(simulation_result_id: str, message:str):

    token = get_auth_token()
    session_Id = initiate_chat(token)
    send_message(
            token=token,
            session_Id=session_Id,
            message=message
        )
    bot_message = poll_response(
            token=token,
            session_Id=session_Id
        )
    
    print({
        "simulation_reult_id" : simulation_result_id,
        "reply":bot_message
    })