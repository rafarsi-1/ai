from sqlalchemy.orm import Session
from . import models, schemas

def create_character(db: Session, character: schemas.CharacterCreate, creator_id: int):
    db_character = models.Character(**character.dict(), creator_id=creator_id)
    db.add(db_character)
    db.commit()
    db.refresh(db_character)
    return db_character

def get_characters(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Character).offset(skip).limit(limit).all()

def create_message(db: Session, message: schemas.MessageCreate, character_id: int, user_id: int):
    db_message = models.Message(**message.dict(), character_id=character_id, user_id=user_id)
    db.add(db_message)
    db.commit()
    db.refresh(db_message)
    return db_message

def get_messages(db: Session, character_id: int, user_id: int, skip: int = 0, limit: int = 100):
    return db.query(models.Message).filter(
        models.Message.character_id == character_id,
        models.Message.user_id == user_id
    ).offset(skip).limit(limit).all()