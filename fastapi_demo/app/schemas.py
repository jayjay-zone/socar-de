"""api request/response model definition"""
from typing import Optional
from pydantic import BaseModel

""" request 용도 """
class CarBase(BaseModel):
    name: str
    brand: str
    year: int

class CarCreate(CarBase):
    pass

class CarUpdate(CarBase):
    name: Optional[str] = None
    brand: Optional[str] = None
    year: Optional[int] = None

""" response 용도 """
class CarResponse(CarBase):
    id: int

    class Config:
        """
        SQLAlchemy 모델 객체를 바로 FastAPI 응답 모델에 넣어도 자동으로 JSON으로 변환
        """
        from_attributes = True  
    