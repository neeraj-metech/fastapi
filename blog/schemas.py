from pydantic import BaseModel,EmailStr,Field
from typing import Union,List
class Blog(BaseModel):
    title: str
    body: str
    published: Union[bool, None] = None
    user_id: int
    class Config():
        orm_mode = True
        
class User(BaseModel):
    name: str
    email: EmailStr
    password: str
    
class ShowUser(BaseModel):
    name: str
    email: EmailStr
    blogs: List[Blog] = []
    class Config():
        orm_mode = True
    

class ShowBlog(BaseModel):
    title: str
    body: str
    user: ShowUser
    class Config():
        orm_mode = True
        
class Login(BaseModel):
    username: EmailStr
    password: str
    
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: EmailStr | None = None
    

class Chat(BaseModel):
    question: str
    chat_id: int = Field(default=None)
    model: str = Field(default="gpt-4o-mini")
                                 
class ChatHistory(BaseModel):
    answer: str
    chat_id: str
    model: str
    