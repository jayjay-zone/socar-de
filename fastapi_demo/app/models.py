"""DB table scheme (model) definition"""
from sqlalchemy import Column, Integer, String
from app.database import Base

class Car(Base):
    __tablename__ = "cars"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    brand = Column(String)
    year = Column(Integer)
