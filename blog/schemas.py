from pydantic import BaseModel,EmailStr
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