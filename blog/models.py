from database import Base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship

class Blog(Base):
    __tablename__ = "blog"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    body = Column(String)
    published = Column(Boolean, default=True)
    user_id = Column(Integer, ForeignKey("user.id"),default=1)
    user = relationship("User", back_populates="blogs")
    
class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)
    blogs = relationship("Blog", back_populates="user")
    
    