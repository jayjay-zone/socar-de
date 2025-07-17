from fastapi import HTTPException

from sqlalchemy.orm import Session
from app.models import CarInfoScheme as Car
from app.schemas import *

def get_cars(db: Session):
    return db.query(Car).all()

def get_car_by_id(db: Session, car_id: int):
    car = db.query(Car).filter(Car.id == car_id).first()
    if car is None:
        raise HTTPException(status_code=404, detail=f"car_id {car_id} is not found") 

    return car

def create_car(db: Session, car: CarCreate):
    db_car = Car(
        name=car.name,
        brand=car.brand,
        year=car.year
    )
    db.add(db_car)
    db.commit()
    db.refresh(db_car)
    return db_car

# TODO:
# CarCreate가 세개의 값을 필수로 받아야 할지??
# name, brand, year 를 optional로 주면 됨
# NOTE: refresh와 commit 의 차이? 
# commit: INSERT, refresh: SELECT 
def update_car(db: Session, car_id: int, car:CarUpdate):
    db_car = db.query(Car).filter(Car.id == car_id).first()
    # TODO: parameter들이 엄청 많다면? dict -> **params
    if car.name is not None:
        db_car.name = car.name
    if car.brand is not None:
        db_car.brand = car.brand
    if car.year is not None:
        db_car.year = car.year
    db.commit()
    db.refresh(db_car) 
    return db_car


# NOTE: refresh를 안하는 이유?
# refresh는 새로 추가된 데이터를 DB에서 select해서 가져오는 용도. 
# 따라서 delete한 객체는 DB상에 없기 때문에 refresh(SELECT)할 수 없음
def delete_car(db: Session, car_id: int):
    db_car = db.query(Car).filter(Car.id == car_id).first()
    db.delete(db_car)
    db.commit()
    return db_car

# NOTE: flush vs commit
# flush: 트랜잭션 유지 -> rollback 가능
# commit: 트랜잭션 종료 -> rollback 불가

# NOTE: flush 가 sqlalchemy에만 있는지,  다른 데에서도 쓰느지? database 상에서도 있는 개념인지 확인필요!


# TODO: year -> formaitting (YYY-MM-DD), input을 0~10사이로 넣던지
# request model자체에 넣어서, 그게 안맞으면 아예 요청이 튕기게끔