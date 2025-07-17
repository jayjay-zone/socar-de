"""DB table scheme (model) definition"""
from sqlalchemy import Column, Integer, String
from app.database import Base

class CarInfoScheme(Base):
    __tablename__ = "car_info"

    id = Column(Integer, primary_key=True, index=True)
    # NOTE: MySQL은 VARCHAR 타입을 사용할 때 길이를 반드시 명시
    name = Column(String(100))    
    brand = Column(String(100))   
    year = Column(Integer)