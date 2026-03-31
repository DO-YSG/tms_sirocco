import uuid

from sqlalchemy.orm import Session

from app.models import City


class CityRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_all(self) -> list[City]:
        return self.db.query(City).order_by(City.name).all()

    def get_by_id(self, city_id: uuid.UUID) -> City | None:
        return self.db.query(City).filter(City.id == city_id).first()

    def get_by_country(self, country_id: uuid.UUID) -> list[City]:
        return self.db.query(City).filter(City.country_id == country_id).order_by(City.name).all()

    def create(self, city: City) -> City:
        self.db.add(city)
        return city

    def exists(self, name: str, region: str, country_id: uuid.UUID) -> bool:
        return self.db.query(City).filter(
            City.name == name,
            City.region == region,
            City.country_id == country_id
        ).first() is not None