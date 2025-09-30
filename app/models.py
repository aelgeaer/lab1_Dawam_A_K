from sqlalchemy import Column, Integer, String, Boolean, DateTime, Text, ForeignKey, JSON
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from datetime import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, index=True, nullable=False)
    registration_date = Column(DateTime, default=datetime.utcnow)
    is_verified = Column(Boolean, default=False)
    avatar = Column(String(200), nullable=True)
    
    # Relationships
    news = relationship("News", back_populates="author")
    comments = relationship("Comment", back_populates="author")

class News(Base):
    __tablename__ = "news"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), nullable=False)
    content = Column(JSON, nullable=False)
    publication_date = Column(DateTime, default=datetime.utcnow)
    author_id = Column(Integer, ForeignKey("users.id"))
    cover = Column(String(200), nullable=True)
    
    # Relationships
    author = relationship("User", back_populates="news")
    comments = relationship("Comment", back_populates="news", cascade="all, delete-orphan")

class Comment(Base):
    __tablename__ = "comments"
    
    id = Column(Integer, primary_key=True, index=True)
    text = Column(Text, nullable=False)
    news_id = Column(Integer, ForeignKey("news.id"))
    author_id = Column(Integer, ForeignKey("users.id"))
    publication_date = Column(DateTime, default=datetime.utcnow)
    
    # Relationships
    news = relationship("News", back_populates="comments")
    author = relationship("User", back_populates="comments")
