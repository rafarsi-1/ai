from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import schemas, crud, database

router = APIRouter(prefix="/characters", tags=["characters"])

@router.post("/", response_model=schemas.Character)
def create_character(character: schemas.CharacterCreate, db: Session = Depends(database.get_db)):
    # Assume user_id=1 for simplicity; add auth later
    return crud.create_character(db=db, character=character, creator_id=1)

@router.get("/", response_model=list[schemas.Character])
def read_characters(skip: int = 0, limit: int = 100, db: Session = Depends(database.get_db)):
    return crud.get_characters(db=db, skip=skip, limit=limit)