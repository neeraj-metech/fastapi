from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, status, HTTPException
import models
import schemas
from hashing import Hashing
from database import get_db

def create(db:Session,user:schemas.User):
    new_user = models.User(name=user.name,email=user.email,password=Hashing.encrypt_password(user.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def get_chat_history(chat_id:int=None,db:Session=None):
    chatHistory = db.query(models.ChatHistory).where(models.ChatHistory.chat_id == chat_id).all()
    messages = []
    for row in chatHistory:
        messages.extend([
            {"role": "user", "content": row.user_query},
            {"role": "assistant", "content": row.gpt_response}
        ])
    return messages

def insert_chat_history(chat:schemas.Chat,answer:str,db:Session=None):
    if not chat.chat_id:
        new_chat = models.Chat(chat_name=chat.question)
        db.add(new_chat)
        db.commit()
        db.refresh(new_chat)
        chat_id = new_chat.id
    else:
        chat_id = chat.chat_id
        
    chat_history = models.ChatHistory(chat_id=chat_id,user_query=chat.question,gpt_response=answer,model=chat.model)
    db.add(chat_history)
    db.commit()
    db.refresh(chat_history)
    return chat_id
    
    