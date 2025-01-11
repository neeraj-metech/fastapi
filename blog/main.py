from fastapi import FastAPI
import models
from database import engine
from routers import users,blogs,login,chatgpt

app = FastAPI()

models.Base.metadata.create_all(bind=engine)
app.include_router(login.router)
app.include_router(chatgpt.router)
app.include_router(users.router)
app.include_router(blogs.router)
