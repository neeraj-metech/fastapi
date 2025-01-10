from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from typing import List,Annotated
import schemas
import models
from database import get_db
from hashing import Hashing
import jwt_token
from fastapi.security import OAuth2PasswordRequestForm
# from repository import user as userRepo

router = APIRouter(
    prefix="/login",
    tags=["Authentication"]
)


@router.post("")
def login(login:Annotated[OAuth2PasswordRequestForm, Depends()],db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == login.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Invalid Credentials.")
    if not Hashing.verify_password(login.password,user.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Password is incorrect.")
    access_token = jwt_token.create_access_token(data={"sub": user.email})
    return {"access_token":access_token, "token_type":"bearer"}
