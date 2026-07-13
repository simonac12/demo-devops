from fastapi import FastAPI, HTTPException
from prometheus_fastapi_instrumentator import Instrumentator
import logging
import time

logging.basicConfig(level=logging.INFO)

app = FastAPI()

Instrumentator().instrument(app).expose(app)

@app.get("/")
def home():
    logging.info("Home endpoint called")
    return {"message": "Hello DevOps Summer School"}

@app.get("/slow")
def slow():
    logging.info("Slow endpoint called")
    time.sleep(2)
    return {"message": "Slow endpoint"}

@app.get("/error")
def error():
    logging.error("Error endpoint called")
    raise HTTPException(status_code=500, detail="Something went wrong")