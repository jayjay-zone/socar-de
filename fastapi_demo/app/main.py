# main.py
from fastapi import FastAPI

from app.routes import cars  
from app.database import engine
from app.models import Base

print("📦 DB 테이블 생성 중...")
Base.metadata.create_all(bind=engine)
print("✅ 테이블 생성 완료!")

app = FastAPI()

@app.get("/")
def root():
    return {"message": "FastAPI 서버가 잘 돌아가고 있어요 🚀"}

app.include_router(cars.router)