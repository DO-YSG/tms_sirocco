import uuid

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.dependencies import get_db
from app.services.city import CityService
from app.schemas.city import CityCreate, CityRead

router = APIRouter(prefix="/cities", tags=["cities"])


@router.get("/", response_model=list[CityRead])
def get_cities(db: Session = Depends(get_db)):
    service = CityService(db)
    return service.get_all()


@router.get("/by-country/{country_id}", response_model=list[CityRead])
def get_cities_by_country(country_id: uuid.UUID, db: Session = Depends(get_db)):
    service = CityService(db)
    return service.get_by_country(country_id)


@router.get("/{city_id}", response_model=CityRead)
def get_city(city_id: uuid.UUID, db: Session = Depends(get_db)):
    service = CityService(db)
    return service.get_by_id(city_id)


@router.post("/", response_model=CityRead)
def create_city(data: CityCreate, db: Session = Depends(get_db)):
    service = CityService(db)
    return service.create(data)