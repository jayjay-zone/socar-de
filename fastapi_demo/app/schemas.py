"""api request/response model definition"""

from pydantic import BaseModel

class CarBase(BaseModel):
    name: str
    brand: str
    year: int

class CarCreate(CarBase):
    pass

class Car(CarBase):
    id: int

    class Config:
        orm_mode = True

    