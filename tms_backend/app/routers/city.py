import uuid

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.models.city import City
from app.schemas.city import CityCreate, CityUpdate, CityRead
from app.dependencies import get_db


router = APIRouter(prefix="/cities", tags=["Cities"])


@router.post("/", response_model=CityRead)
def create_city(city: CityCreate, db: Session = Depends(get_db)):
    db_city = City(
        name=city.name,
        region=city.region,
        country=city.country
    )
    db.add(db_city)
    db.commit()
    db.refresh(db_city)
    return db_city


@router.get("/", response_model=list[CityRead])
def get_cities(db: Session = Depends(get_db)):
    return db.query(City).all()


@router.get("/{city_id}", response_model=CityRead)
def get_city(city_id: uuid.UUID, db: Session = Depends(get_db)):
    city = db.query(City).filter(City.id == city_id).first()
    if not city:
        raise HTTPException(status_code=404, detail="City not found")
    return city


@router.put("/{city_id}", response_model=CityRead)
def update_city(city_id: uuid.UUID, city_data: CityUpdate, db: Session = Depends(get_db)):
    city = db.query(City).filter(City.id == city_id).first()
    if not city:
        raise HTTPException(status_code=404, detail="City not found")

    update_data = city_data.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(city, key, value)

    db.commit()
    db.refresh(city)
    return city


@router.delete("/{city_id}")
def delete_city(city_id: uuid.UUID, db: Session = Depends(get_db)):
    city = db.query(City).filter(City.id == city_id).first()
    if not city:
        raise HTTPException(status_code=404, detail="City not found")

    db.delete(city)
    db.commit()
    return {"message": "City deleted successfully"}