from fastapi import FastAPI
import time
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI()

Instrumentator().instrument(app).expose(app)

@app.get("/")
def home():
    return {"message": "Welcome to DevOps Demo"}

@app.get("/products")
def products():
    return [
        {"id": 1, "name": "Laptop"},
        {"id": 2, "name": "Mouse"},
        {"id": 3, "name": "Keyboard"},
    ]

@app.get("/slow")
def slow():
    time.sleep(2)
    return {"message": "This endpoint is intentionally slow"}

@app.get("/error")
def error():
    raise Exception("Something went wrong")