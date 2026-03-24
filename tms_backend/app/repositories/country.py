import uuid

from sqlalchemy.orm import Session

from app.models import Country


class CountryRepository:

    def __init__(self, db: Session):
        self.db = db

    def get_all(self) -> list[Country]:
        return self.db.query(Country).order_by(Country.name).all()

    def get_by_id(self, country_id: uuid.UUID) -> Country | None:
        return self.db.query(Country).filter(Country.id == country_id).first()