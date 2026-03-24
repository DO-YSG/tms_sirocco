import uuid

from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.models import City
from app.repositories.city import CityRepository
from app.schemas.city import CityCreate


class CityService:

    def __init__(self, db: Session):
        self.repo = CityRepository(db)

    def get_all(self) -> list[City]:
        return self.repo.get_all()

    def get_by_id(self, city_id: uuid.UUID) -> City:
        city = self.repo.get_by_id(city_id)
        if not city:
            raise HTTPException(status_code=404, detail="City not found")
        return city

    def get_by_country(self, country_id: uuid.UUID) -> list[City]:
        return self.repo.get_by_country(country_id)

    def create(self, data: CityCreate) -> City:
        if self.repo.exists(data.name, data.region, data.country_id):
            raise HTTPException(status_code=400, detail="City already exists in this region and country")

        city = City(**data.model_dump())
        return self.repo.create(city)