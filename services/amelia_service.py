from services.auth_service import get_auth_token
from services.chat_service import initiate_chat
from services.message_service import send_message
from services.receive_service import poll_response
from services.conversation_store import get_session_id , set_session_id , clear_session

def process_with_amelia(simulation_result_id: str, message:str, end_conversation: bool = False):
    
    try:
        token = get_auth_token()

        session_Id = get_session_id(simulation_result_id)

        if not session_Id:
            session_Id = initiate_chat(token)
            set_session_id(simulation_result_id, session_Id)

        send_message(
                token=token,
                session_Id=session_Id,
                message=message
            )
        bot_message = poll_response(
                token=token,
                session_Id=session_Id
            )
        
        print("Amela bot reply:",bot_message)
        
        print({
            "simulation_result_id" : simulation_result_id,
            "session_id" : session_Id,
            "reply":bot_message
        })

        if end_conversation:
            clear_session(simulation_result_id)
    
    except Exception as e:
        print("Amelia process failed:", str(e))





# DOS COMMIT

# def process_with_amelia(simulation_result_id: str, message:str):

#     token = get_auth_token()
#     session_Id = initiate_chat(token)
#     send_message(
#             token=token,
#             session_Id=session_Id,
#             message=message
#         )
#     bot_message = poll_response(
#             token=token,
#             session_Id=session_Id
#         )
    
#     print({
#         "simulation_reult_id" : simulation_result_id,
#         "reply":bot_message
#     })