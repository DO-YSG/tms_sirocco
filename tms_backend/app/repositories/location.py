import uuid

from sqlalchemy.orm import Session
from sqlalchemy import select, update, delete, exists

from app.models import Location


class LocationRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, data: dict) -> Location:
        location = Location(**data)
        self.db.add(location)
        return location

    def get_by_id(self, location_id: uuid.UUID):
        stmt = select(Location).where(Location.id == location_id)
        return self.db.execute(stmt).scalar_one_or_none()

    def get_list(self, skip: int = 0, limit: int = 100):
        stmt = select(Location).offset(skip).limit(limit)
        return self.db.execute(stmt).scalars().all()

    def update(self, location_id: uuid.UUID, data: dict):
        stmt = (
            update(Location)
            .where(Location.id == location_id)
            .values(**data)
            .returning(Location)
        )
        return self.db.execute(stmt).scalar_one_or_none()

    def delete(self, location_id: uuid.UUID):
        stmt = delete(Location).where(Location.id == location_id)
        result = self.db.execute(stmt)
        return result.rowcount

    def exists(self, location_id: uuid.UUID) -> bool:
        stmt = select(exists().where(Location.id == location_id))
        return self.db.execute(stmt).scalar()