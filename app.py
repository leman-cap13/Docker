from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline


nlp = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

api = FastAPI(title="NLP Demo", version="0.1.0")

class Inp(BaseModel):
    text: str

@api.get("/health")
def health():
    return {"status": "ok"}

@api.post("/predict")
def predict(inp: Inp):
    res = nlp(inp.text)
    return {"input": inp.text, "prediction": res[0]}
