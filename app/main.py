from fastapi import FastAPI
from pydantic import BaseModel
from app.agent import generate_response

app = FastAPI()

class Request(BaseModel):
    query: str

@app.get("/")
def health():
    return {"status": "running"}

@app.post("/ask")
def ask(req: Request):
    return {"answer": generate_response(req.query)}