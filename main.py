from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    title="Text Token API",
    description="Welcome Koushik! Generate tokens and checksums.",
    version="1.0.0"
)

class TextRequest(BaseModel):
    text: str

@app.get("/")
def welcome():
    return {
        "message": "Welcome Koushik!"
    }

@app.post("/generate")
def generate(request: TextRequest):
    tokens = request.text.split()

    checksum = sum(ord(char) for char in request.text)

    return {
        "tokens": tokens,
        "checksum": checksum
    }
