import uuid

from sqlalchemy.orm import Session

from app.models import Location
from app.schemas.location import LocationCreate, LocationUpdate
from app.repositories.location import LocationRepository


class LocationService:
    def __init__(self, db: Session):
        self.db = db
        self.repo = LocationRepository(db)

    def create(self, data: LocationCreate) -> Location:
        location = self.repo.create(data.model_dump())

        self.db.commit()
        self.db.refresh(location)

        return location

    def get_by_id(self, location_id: uuid.UUID) -> Location | None:
        return self.repo.get_by_id(location_id)

    def get_list(self, skip: int = 0, limit: int = 100) -> list[Location]:
        return self.repo.get_list(skip, limit)

    def update(self, location_id: uuid.UUID, data: LocationUpdate):
        if not self.repo.exists(location_id):
            return None

        update_data = data.model_dump(exclude_unset=True)
        if not update_data:
            return self.repo.get_by_id(location_id)

        location = self.repo.update(location_id, update_data)

        self.db.commit()
        self.db.refresh(location)
        return location

    def delete(self, location_id: uuid.UUID) -> bool:
        if not self.repo.exists(location_id):
            return False

        deleted = self.repo.delete(location_id)

        self.db.commit()

        return deleted > 0