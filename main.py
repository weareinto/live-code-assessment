from fastapi import FastAPI
from ai import LLM
app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello Candidate!"}


# TODO: create the new endpoint here
# The payload should have, the text and the model name