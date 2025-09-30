from fastapi import FastAPI, Depends, HTTPException
from app.database import get_db, Base, engine
from app.repositories.sqlalchemy_repo import SQLAlchemyRepository
from app import models, schemas, crud
from typing import List

app = FastAPI(title="News API", version="1.0.0")

# Create tables
Base.metadata.create_all(bind=engine)

# User routes
@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db = Depends(get_db)):
    return crud.create_user(db, user)

@app.get("/users/", response_model=List[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db = Depends(get_db)):
    return crud.get_users(db, skip=skip, limit=limit)

@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

# News routes
@app.post("/news/", response_model=schemas.News)
def create_news(news: schemas.NewsCreate, db = Depends(get_db)):
    # Check if user is verified
    author = crud.get_user(db, user_id=news.author_id)
    if not author or not author.is_verified:
        raise HTTPException(status_code=400, detail="User is not verified to create news")
    return crud.create_news(db, news)

@app.get("/news/", response_model=List[schemas.News])
def read_news(skip: int = 0, limit: int = 100, db = Depends(get_db)):
    return crud.get_news(db, skip=skip, limit=limit)

@app.get("/news/{news_id}", response_model=schemas.News)
def read_news_item(news_id: int, db = Depends(get_db)):
    db_news = crud.get_news_item(db, news_id=news_id)
    if db_news is None:
        raise HTTPException(status_code=404, detail="News not found")
    return db_news

@app.put("/news/{news_id}", response_model=schemas.News)
def update_news(news_id: int, news: schemas.NewsUpdate, db = Depends(get_db)):
    return crud.update_news(db, news_id=news_id, news=news)

@app.delete("/news/{news_id}")
def delete_news(news_id: int, db = Depends(get_db)):
    crud.delete_news(db, news_id=news_id)
    return {"message": "News deleted successfully"}

# Comment routes
@app.post("/comments/", response_model=schemas.Comment)
def create_comment(comment: schemas.CommentCreate, db = Depends(get_db)):
    return crud.create_comment(db, comment)

@app.get("/comments/", response_model=List[schemas.Comment])
def read_comments(skip: int = 0, limit: int = 100, db = Depends(get_db)):
    return crud.get_comments(db, skip=skip, limit=limit)

@app.get("/comments/{comment_id}", response_model=schemas.Comment)
def read_comment(comment_id: int, db = Depends(get_db)):
    db_comment = crud.get_comment(db, comment_id=comment_id)
    if db_comment is None:
        raise HTTPException(status_code=404, detail="Comment not found")
    return db_comment

@app.put("/comments/{comment_id}", response_model=schemas.Comment)
def update_comment(comment_id: int, comment: schemas.CommentUpdate, db = Depends(get_db)):
    return crud.update_comment(db, comment_id=comment_id, comment=comment)

@app.delete("/comments/{comment_id}")
def delete_comment(comment_id: int, db = Depends(get_db)):
    crud.delete_comment(db, comment_id=comment_id)
    return {"message": "Comment deleted successfully"}

@app.get("/news/{news_id}/comments", response_model=List[schemas.Comment])
def read_news_comments(news_id: int, db = Depends(get_db)):
    return crud.get_comments_by_news(db, news_id=news_id)
