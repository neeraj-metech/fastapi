from typing import List
from fastapi import APIRouter,Depends
import schemas,models
from sqlalchemy.orm import Session
from database import get_db
from repository.user import get_chat_history,insert_chat_history
from openai import OpenAI

OPENAI_API_KEY = ''
client = OpenAI(api_key=OPENAI_API_KEY)
# client = OpenAI()

router = APIRouter(
    prefix="/chat",
    tags=["ChatGPT"]
)

@router.post("")
def get_chatgpt(chat: schemas.Chat,db: Session = Depends(get_db)):
    messages= [{"role": "system","content": "You are a helpful assistant."}]
    if chat.chat_id:
        chat_history = get_chat_history(chat.chat_id,db)
        messages.extend(chat_history)
        messages.extend([{"role": "user", "content": chat.question}])
    else:
        messages= [{"role": "system","content": "You are a helpful assistant."},{"role": "user", "content": chat.question}]

    # Call OpenAI API
    response = client.chat.completions.create(
        model=chat.model,
        messages=messages,
        temperature= 0.7
    )
    answer = response.choices[0].message.content
    chat_id = insert_chat_history(chat,answer,db)
    return {"answer": answer,"chat_id": chat_id,"model": chat.model}

# @router.post("/create_chat")
# def create_chat(chat: schemas.Chat,db: Session = Depends(get_db)):
#     new_chat = models.Chat(chat_name=chat.chat_name)
#     db.add(new_chat)
#     db.commit()
#     db.refresh(new_chat)
#     return new_chat

# @router.get("/get_chats")
# def get_chats(db: Session = Depends(get_db)):
#     return db.query(models.Chat).all()

# @router.post("/create_chat_history")
# def create_chat_history(chathistory: schemas.ChatHistory,db: Session = Depends(get_db)):
#     new_chat_history = models.ChatHistory(chat_id=chathistory.chat_id,response=chathistory.response,status_code=chathistory.status_code,role=chathistory.role,content=chathistory.content)
#     db.add(new_chat_history)
#     db.commit()
#     db.refresh(new_chat_history)
#     return new_chat_history

# @router.get("/get_chat_histories")
# def get_chat_histories(db: Session = Depends(get_db)):
#     return db.query(models.ChatHistory).all()
