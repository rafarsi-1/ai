from pydantic import BaseModel

class CharacterBase(BaseModel):
    name: str
    description: str
    icon: str = None

class CharacterCreate(CharacterBase):
    pass

class Character(CharacterBase):
    id: int
    creator_id: int

    class Config:
        from_attributes = True

class MessageBase(BaseModel):
    content: str

class MessageCreate(MessageBase):
    is_user: int

class Message(MessageBase):
    id: int
    character_id: int
    user_id: int
    timestamp: str
    is_user: int

    class Config:
        from_attributes = True