from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from typing import List
import schemas
import models
from database import get_db
from hashing import Hashing
import oauth2
# from repository import user as userRepo

router = APIRouter(
    prefix="/user",
    tags=["Users"]
)


@router.post("",response_model=schemas.ShowUser)
def create_user(user:schemas.User,db: Session = Depends(get_db)):
    new_user = models.User(name=user.name,email=user.email,password=Hashing.encrypt_password(user.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.get("",response_model=List[schemas.ShowUser])
def get_users(db: Session = Depends(get_db)):
    return db.query(models.User).all()

@router.get("/{id}",status_code=status.HTTP_200_OK,response_model=schemas.ShowUser)
def get_user(id:int,db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"user with id {id} not found")
    return user


