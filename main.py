from fastapi import FastAPI
from models import create_tables
from contextlib import asynccontextmanager




# Create tables on startup
@asynccontextmanager
async def lifespan(app: FastAPI):
    create_tables()
    yield

app = FastAPI(lifespan=lifespan)

@app.get("/")
def read_root():
    return {"message": "Hello Candidate!"}


# TODO: create a new message endpoint
# TODO: Store the message response in the database




# TODO: Get all the messages from the database
