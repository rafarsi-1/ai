from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.sql import func
from .database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)

class Character(Base):
    __tablename__ = "characters"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)  # Personality, greeting, etc.
    creator_id = Column(Integer, ForeignKey("users.id"))
    icon = Column(String)  # URL to icon

class Message(Base):
    __tablename__ = "messages"
    id = Column(Integer, primary_key=True, index=True)
    character_id = Column(Integer, ForeignKey("characters.id"))
    user_id = Column(Integer, ForeignKey("users.id"))
    content = Column(String)
    is_user = Column(Integer)  # 1 for user, 0 for AI
    timestamp = Column(DateTime(timezone=True), server_default=func.now())