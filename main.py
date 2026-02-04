from fastapi import FastAPI, HTTPException
from prometheus_fastapi_instrumentator import Instrumentator
import random
import time

app = FastAPI(title="DevOps Master API")
Instrumentator().instrument(app).expose(app)

@app.get("/")
async def root():
    return {"message": "Bienvenido al taller"}

@app.get("/api/v1/data")
async def get_data():
    time.sleep(random.uniform(0.1, 0.5))
    return {"status": "success"}

@app.get("/api/v1/error")
async def trigger_error():
    print("ERROR: Fallo crítico detectado en el sistema")
    raise HTTPException(status_code=500, detail="Error del servidor")
