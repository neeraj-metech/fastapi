from sqlalchemy.orm import Session
import models
import schemas
from hashing import Hashing

def create(db:Session,user:schemas.User):
    new_user = models.User(name=user.name,email=user.email,password=Hashing.encrypt_password(user.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
    