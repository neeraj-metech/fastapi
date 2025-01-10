from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from typing import List
import schemas
import models
from database import get_db
import oauth2

router = APIRouter()

@router.post("/blog",tags=["Blogs"])
def create_blog(blog: schemas.Blog, db: Session = Depends(get_db),get_current_user:schemas.User = Depends(oauth2.get_current_user)):
    new_blog = models.Blog(title=blog.title, body=blog.body, published=blog.published, user_id=blog.user_id)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

@router.get("/blog",tags=["Blogs"])
def get_blogs(db: Session = Depends(get_db),get_current_user:schemas.User = Depends(oauth2.get_current_user)):
    return db.query(models.Blog).all()

@router.get("/blog/{id}",status_code=status.HTTP_200_OK,response_model=schemas.ShowBlog,tags=["Blogs"])
def get_blog(id:int,db: Session = Depends(get_db),get_current_user:schemas.User = Depends(oauth2.get_current_user)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"blog with id {id} not found")
    return blog

@router.delete("/blog/{id}",status_code=status.HTTP_204_NO_CONTENT,tags=["Blogs"])
def delete_blog(id:int,db: Session = Depends(get_db),get_current_user:schemas.User = Depends(oauth2.get_current_user)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"blog with id {id} not found")
    db.delete(blog)
    db.commit()
    return {"message":"blog deleted successfully"}

@router.put("/blog/{id}",status_code=status.HTTP_202_ACCEPTED,tags=["Blogs"])
def update_blog(id:int,blog:schemas.Blog,db: Session = Depends(get_db),get_current_user:schemas.User = Depends(oauth2.get_current_user)):
    blog_to_update = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog_to_update:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"blog with id {id} not found")
    blog_to_update.title = blog.title
    blog_to_update.body = blog.body
    blog_to_update.published = blog.published
    db.commit()
    return {"message":"blog updated successfully"}
