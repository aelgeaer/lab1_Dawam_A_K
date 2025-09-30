from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Dict, Any, Optional

class UserBase(BaseModel):
    name: str
    email: EmailStr
    is_verified: bool = False
    avatar: Optional[str] = None

class UserCreate(UserBase):
    pass

class UserUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    is_verified: Optional[bool] = None
    avatar: Optional[str] = None

class User(UserBase):
    id: int
    registration_date: datetime
    
    class Config:
        from_attributes = True

class NewsBase(BaseModel):
    title: str
    content: Dict[str, Any]
    cover: Optional[str] = None

class NewsCreate(NewsBase):
    author_id: int

class NewsUpdate(BaseModel):
    title: Optional[str] = None
    content: Optional[Dict[str, Any]] = None
    cover: Optional[str] = None

class News(NewsBase):
    id: int
    publication_date: datetime
    author_id: int
    
    class Config:
        from_attributes = True

class CommentBase(BaseModel):
    text: str

class CommentCreate(CommentBase):
    news_id: int
    author_id: int

class CommentUpdate(BaseModel):
    text: Optional[str] = None

class Comment(CommentBase):
    id: int
    publication_date: datetime
    news_id: int
    author_id: int
    
    class Config:
        from_attributes = True
