from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.crud import (
    get_cars as get_all_cars_from_db,
    get_car_by_id as get_car_from_db,
    create_car as create_car_in_db,
    update_car as update_car_in_db,
    delete_car as delete_car_in_db,
)
from app.schemas import CarCreate, Car

router = APIRouter()

@router.get("/cars")
def get_all_cars(db: Session = Depends(get_db)):
    return get_all_cars_from_db(db)

@router.get("/cars/{car_id}")
def get_single_car(car_id: int, db: Session = Depends(get_db)):
    return get_car_from_db(db, car_id)

@router.post("/cars")
def create_car(car: CarCreate, db: Session = Depends(get_db)):
    return create_car_in_db(db=db, car=car)

@router.put("/cars/{car_id}")
def update_car(car_id: int, car: CarCreate, db: Session = Depends(get_db)):
    return update_car_in_db(db=db, car_id=car_id, car=car)

@router.delete("/cars/{car_id}")
def delete_car(car_id: int, db: Session = Depends(get_db)):
    return delete_car_in_db(db=db, car_id=car_id)
