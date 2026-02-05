from fastapi import FastAPI , HTTPException , Request , Header 
import json
from services.auth_service import get_auth_token
from services.chat_service import initiate_chat
from services.message_service import send_message
from services.receive_service import poll_response
from services.bluejay_signature import verify_bluejay_signature
from services.bluejay_send_service import send_message_to_bluejay

app = FastAPI()

@app.post("/bluejay/webhook")
async def bluejay_webhook(
    request: Request,
    X_bluejay_signature: str | None = Header(default=None)
):
    
    raw_body = await request.body()

    if not X_bluejay_signature:
        raise HTTPException(status_code=401, detail="Missing Bluejay signature")
    
    if not verify_bluejay_signature(raw_body, X_bluejay_signature):
        raise HTTPException(status_code=401, detail="Invalid Bluejay signature")
    
    try:
        payload = json.loads(raw_body)
    except json.JSONDecodeError:
        raise HTTPException(status_code=400, detail="Invalid JSON payload")

    incoming_message = payload.get("message")
    if not incoming_message:
        raise HTTPException(status_code=400, detail="Message not found")

    token = await get_auth_token()
    session_id = await initiate_chat(token)

    await send_message(
        token=token,
        session_id=session_id,
        message=incoming_message
    )

    bot_message = await poll_response(token, session_id)

    return {
        "status" : "success",
        "reply" : bot_message
    }
# from typing import Union

# from fastapi import FastAPI , HTTPException , Request , Header 
# from pydantic import BaseModel
# from services.auth_service import get_auth_token
# from services.chat_service import initiate_chat
# from services.message_service import send_message
# from services.receive_service import poll_response
# from services.bluejay_signature import verify_bluejay_signature
# from services.bluejay_send_service import send_message_to_bluejay

# app = FastAPI()


# class MessageRequest(BaseModel):
#     message: str

# @app.get("/")
# def read_root():
#     return {"status": "Middleware Running"}


# @app.post("/bluejay/webhook")
# async def blujay_webhook(request: Request, X_blujay_signature : str | None = Header(default=None), X_simulation_result_id: str | None = Header(default=None)):
#     raw_body = await request.body()

#     # if not X_blujay_signature:
#     #     raise HTTPException(status_code=401, detail="Missing Bluejay signature")

#     # if not verify_bluejay_signature(raw_body, X_blujay_signature):
#     #     raise HTTPException(status_code=401, detail="Invalid blujay signature")
    
#     payload = await request.json()
#     incoming_message = payload.get("message")
#     message_id = payload.get("message_id") #I think it needs to be unique
#     end_conversation = payload.get("end_conversation",False)

#     if not incoming_message:
#         raise HTTPException(status_code=400, detail="Missing message")
    
#     token = get_auth_token()
#     session_Id = initiate_chat(token)
#     send_result = send_message(
#             token=token,
#             session_Id=session_Id,
#             message=incoming_message
#         )
#     bot_message = poll_response(
#             token=token,
#             session_Id=session_Id
#         )
    
#     send_message_to_bluejay(
#         simulation_result_id= X_simulation_result_id,
#         message=bot_message,
#         message_id=message_id, # this should be unique everytime i think not sure
#         end_conversation=end_conversation,
#         end_turn=False
#     )

#     return {"simulation_result_id":X_simulation_result_id,
#             "status":"received",
#             "reply":bot_message
#     }


# @app.post("/bluejay/webhook")
# async def blujay_webhook(request: Request, X_blujay_signature : str | None = Header(default=None), X_simulation_result_id: str | None = Header(default=None)):
#     raw_body = await request.body()

#     # if not X_blujay_signature:
#     #     raise HTTPException(status_code=401, detail="Missing Bluejay signature")

#     # if not verify_bluejay_signature(raw_body, X_blujay_signature):
#     #     raise HTTPException(status_code=401, detail="Invalid blujay signature")
    
#     payload = await request.json()
#     incoming_message = payload.get("message")
#     message_id = payload.get("message_id") #I think it needs to be unique
#     end_conversation = payload.get("end_conversation",False)

#     if not incoming_message:
#         raise HTTPException(status_code=400, detail="Missing message")
    
#     token = get_auth_token()
#     session_Id = initiate_chat(token)
#     send_result = send_message(
#             token=token,
#             session_Id=session_Id,
#             message=incoming_message
#         )
#     bot_message = poll_response(
#             token=token,
#             session_Id=session_Id
#         )
    
#     send_message_to_bluejay(
#         simulation_result_id= X_simulation_result_id,
#         message=bot_message,
#         message_id=message_id, # this should be unique everytime i think not sure
#         end_conversation=end_conversation,
#         end_turn=False
#     )

#     return {"simulation_result_id":X_simulation_result_id,
#             "status":"received",
#             "reply":bot_message
#     }


# @app.post("/bluejay/webhook")
# async def blujay_webhook(request: Request, X_blujay_signature : str = Header(...), X_simulation_result_id: str = Header(...)):
#     raw_body = await request.body()

#     if not X_blujay_signature:
#         raise HTTPException(status_code=401, detail="Missing Bluejay signature")

#     if not verify_bluejay_signature(raw_body, X_blujay_signature):
#         raise HTTPException(status_code=401, detail="Invalid blujay signature")
    
#     payload = await request.json()
#     incoming_message = payload.get("message")
#     message_id = payload.get("message_id") #I think it needs to be unique
#     end_conversation = payload.get("end_conversation",False)

#     if not incoming_message:
#         raise HTTPException(status_code=400, detail="Missing message")
    
#     token = get_auth_token()
#     session_Id = initiate_chat(token)
#     send_result = send_message(
#             token=token,
#             session_Id=session_Id,
#             message=incoming_message
#         )
#     bot_message = poll_response(
#             token=token,
#             session_Id=session_Id
#         )
    
#     send_message_to_bluejay(
#         simulation_result_id= X_simulation_result_id,
#         message=bot_message,
#         message_id=message_id, # this should be unique everytime i think not sure
#         end_conversation=end_conversation,
#         end_turn=False
#     )

#     return {"simulation_result_id":X_simulation_result_id,
#             "status":"received",
#             "reply":bot_message
#     }


# @app.post("/conversation")
# def conversation(request: MessageRequest):
#     # user_message = request.message

#     # token = get_auth_token()
#     try:
#         token = get_auth_token()
#         session_Id = initiate_chat(token)
#         send_result = send_message(
#             token=token,
#             session_Id=session_Id,
#             message=request.message
#         )
#         bot_message = poll_response(
#             token=token,
#             session_Id=session_Id
#         )
#     except Exception as e:
#         raise HTTPException(status_code=401,detail=str(e))

#     # processed_message = f"Received : {user_message}"

#     return{
#         "message_received" : request.message,
#         "auth_token":token,
#         "session_Id":session_Id,
#         "send_result":send_result,
#         "bot_response":bot_message
#     }


# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}