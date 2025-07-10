from sqlalchemy.orm import Session
from app.models import Car
from app.schemas import CarCreate

def get_cars(db: Session):
    return db.query(Car).all()

def get_car_by_id(db: Session, car_id: int):
    return db.query(Car).filter(Car.id == car_id).first()

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

def update_car(db: Session, car_id: int, car: CarCreate):
    db_car = db.query(Car).filter(Car.id == car_id).first()
    db_car.name = car.name
    db_car.brand = car.brand
    db_car.year = car.year
    db.commit()
    db.refresh(db_car)
    return db_car

def delete_car(db: Session, car_id: int):
    db_car = db.query(Car).filter(Car.id == car_id).first()
    db.delete(db_car)
    db.commit()
    return db_car