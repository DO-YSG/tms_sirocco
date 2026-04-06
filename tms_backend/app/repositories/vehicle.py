from uuid import UUID

from sqlalchemy import select
from sqlalchemy.orm import Session, selectinload

from app.models.vehicle import Vehicle
from app.models.enums import Status


class VehicleRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_by_id(self, vehicle_id: UUID) -> Vehicle | None:
        stmt = (
            select(Vehicle)
            .options(selectinload(Vehicle.owner))
            .where(Vehicle.id == vehicle_id)
        )
        result = self.db.execute(stmt)
        return result.scalar_one_or_none()

    def get_all(
        self,
        owner_id: UUID | None = None,
        status: Status | None = None,
        limit: int = 100,
        offset: int = 0,
    ) -> list[Vehicle]:
        stmt = select(Vehicle).options(selectinload(Vehicle.owner))

        if owner_id is not None:
            stmt = stmt.where(Vehicle.owner_id == owner_id)

        if status is not None:
            stmt = stmt.where(Vehicle.status == status)

        stmt = stmt.offset(offset).limit(limit)

        result = self.db.execute(stmt)
        return list(result.scalars().all())

    def get_by_vin(self, vin: str) -> Vehicle | None:
        stmt = select(Vehicle).where(Vehicle.vin == vin)
        result = self.db.execute(stmt)
        return result.scalar_one_or_none()

    def get_by_plate_number(self, plate_number: str) -> Vehicle | None:
        stmt = select(Vehicle).where(Vehicle.plate_number == plate_number)
        result = self.db.execute(stmt)
        return result.scalar_one_or_none()

    def get_by_sts_number(self, sts_number: str) -> Vehicle | None:
        stmt = select(Vehicle).where(Vehicle.sts_number == sts_number)
        result = self.db.execute(stmt)
        return result.scalar_one_or_none()

    def create(self, data: dict) -> Vehicle:
        vehicle = Vehicle(**data)
        self.db.add(vehicle)
        return vehicle

    def update(self, vehicle: Vehicle, data: dict) -> Vehicle:
        for field, value in data.items():
            setattr(vehicle, field, value)
        return vehicle

    def delete(self, vehicle: Vehicle) -> None:
        self.db.delete(vehicle)