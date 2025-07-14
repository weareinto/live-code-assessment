from fastapi import FastAPI, Depends, HTTPException, Header
from sqlalchemy.orm import Session
from ai import LLM
from models import create_tables
from config import settings
from contextlib import asynccontextmanager


app = FastAPI()

# Create tables on startup
@asynccontextmanager
async def lifespan(app: FastAPI):
    create_tables()
    yield

@app.get("/")
def read_root():
    return {"message": "Hello Candidate!"}


# TODO: create the new endpoint here








# TODO: Get all the messages from the database