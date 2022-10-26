import uvicorn
from fastapi import FastAPI

app = FastAPI()
@app.get("/")
def road_root():
    return {"Hello World !! "}