from fastapi import FastAPI
from .routers import characters, chat
from .database import engine
from .models import Base

app = FastAPI()

Base.metadata.create_all(bind=engine)  # Create tables

app.include_router(characters.router)
app.include_router(chat.router)