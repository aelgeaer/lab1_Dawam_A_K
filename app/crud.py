from sqlalchemy.orm import Session
from app import models, schemas
from typing import List, Optional

# User CRUD operations
def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_users(db: Session, skip: int = 0, limit: int = 100) -> List[models.User]:
    return db.query(models.User).offset(skip).limit(limit).all()

def get_user(db: Session, user_id: int) -> Optional[models.User]:
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_user_by_email(db: Session, email: str) -> Optional[models.User]:
    return db.query(models.User).filter(models.User.email == email).first()

# News CRUD operations
def create_news(db: Session, news: schemas.NewsCreate):
    db_news = models.News(**news.dict())
    db.add(db_news)
    db.commit()
    db.refresh(db_news)
    return db_news

def get_news(db: Session, skip: int = 0, limit: int = 100) -> List[models.News]:
    return db.query(models.News).offset(skip).limit(limit).all()

def get_news_item(db: Session, news_id: int) -> Optional[models.News]:
    return db.query(models.News).filter(models.News.id == news_id).first()

def update_news(db: Session, news_id: int, news: schemas.NewsUpdate):
    db_news = db.query(models.News).filter(models.News.id == news_id).first()
    if db_news:
        update_data = news.dict(exclude_unset=True)
        for field, value in update_data.items():
            setattr(db_news, field, value)
        db.commit()
        db.refresh(db_news)
    return db_news

def delete_news(db: Session, news_id: int):
    db_news = db.query(models.News).filter(models.News.id == news_id).first()
    if db_news:
        db.delete(db_news)
        db.commit()
    return db_news

# Comment CRUD operations
def create_comment(db: Session, comment: schemas.CommentCreate):
    db_comment = models.Comment(**comment.dict())
    db.add(db_comment)
    db.commit()
    db.refresh(db_comment)
    return db_comment

def get_comments(db: Session, skip: int = 0, limit: int = 100) -> List[models.Comment]:
    return db.query(models.Comment).offset(skip).limit(limit).all()

def get_comment(db: Session, comment_id: int) -> Optional[models.Comment]:
    return db.query(models.Comment).filter(models.Comment.id == comment_id).first()

def get_comments_by_news(db: Session, news_id: int) -> List[models.Comment]:
    return db.query(models.Comment).filter(models.Comment.news_id == news_id).all()

def update_comment(db: Session, comment_id: int, comment: schemas.CommentUpdate):
    db_comment = db.query(models.Comment).filter(models.Comment.id == comment_id).first()
    if db_comment:
        update_data = comment.dict(exclude_unset=True)
        for field, value in update_data.items():
            setattr(db_comment, field, value)
        db.commit()
        db.refresh(db_comment)
    return db_comment

def delete_comment(db: Session, comment_id: int):
    db_comment = db.query(models.Comment).filter(models.Comment.id == comment_id).first()
    if db_comment:
        db.delete(db_comment)
        db.commit()
    return db_comment
