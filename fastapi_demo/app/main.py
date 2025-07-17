# main.py
from fastapi import FastAPI

from app.routes import cars  
from app.database import engine


app = FastAPI()

@app.get("/")
def root():
    return {"message": "FastAPI 서버가 잘 돌아가고 있어요 🚀"}

app.include_router(cars.router)