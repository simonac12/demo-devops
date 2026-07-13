from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator
from fastapi import HTTPException

app = FastAPI()

Instrumentator().instrument(app).expose(app)

@app.get("/")
def home():
    return {"message": "Welcome to DevOps Demo"}

@app.get("/buy")
def buy():
    raise HTTPException(status_code=500, detail="Database unavailable")


