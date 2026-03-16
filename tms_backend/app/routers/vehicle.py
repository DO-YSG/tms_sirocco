import uuid

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.models.vehicle import Vehicle
from app.schemas.vehicle import VehicleCreate, VehicleRead, VehicleUpdate
from app.dependencies import get_db


router = APIRouter(prefix="/vehicles", tags=["Vehicles"])


@router.post("/", response_model=VehicleRead, status_code=201)
def create_vehicle(vehicle: VehicleCreate, db: Session = Depends(get_db)):
    existing_plate = db.query(Vehicle).filter(Vehicle.plate_number == vehicle.plate_number).first()
    if existing_plate:
        raise HTTPException(status_code=400, detail="Vehicle with this plate number already exists")

    existing_vin = db.query(Vehicle).filter(Vehicle.vin == vehicle.vin).first()
    if existing_vin:
        raise HTTPException(status_code=400, detail="Vehicle with this VIN already exists")

    db_vehicle = Vehicle(
        owner_id=vehicle.owner_id,
        vehicle_type=vehicle.vehicle_type,
        sts_number=vehicle.sts_number,
        plate_number=vehicle.plate_number,
        brand=vehicle.brand,
        model=vehicle.model,
        vin=vehicle.vin,
        year=vehicle.year,
        required_license_category=vehicle.required_license_category,
        vehicle_category=vehicle.vehicle_category,
        engine_volume_cc=vehicle.engine_volume_cc,
        color=vehicle.color,
        unladen_weight_kg=vehicle.unladen_weight_kg,
        gross_weight_kg=vehicle.gross_weight_kg,
        registered_owner_name=vehicle.registered_owner_name,
        special_notes=vehicle.special_notes,
        status=vehicle.status,
    )

    db.add(db_vehicle)
    db.commit()
    db.refresh(db_vehicle)

    return db_vehicle


@router.get("/", response_model=list[VehicleRead])
def get_vehicles(db: Session = Depends(get_db)):
    return db.query(Vehicle).all()


@router.get("/{vehicle_id}", response_model=VehicleRead)
def get_vehicle(vehicle_id: uuid.UUID, db: Session = Depends(get_db)):
    vehicle = db.query(Vehicle).filter(Vehicle.id == vehicle_id).first()

    if not vehicle:
        raise HTTPException(status_code=404, detail="Vehicle not found")

    return vehicle


@router.put("/{vehicle_id}", response_model=VehicleRead)
def update_vehicle(vehicle_id: uuid.UUID, vehicle_data: VehicleUpdate, db: Session = Depends(get_db)):
    vehicle = db.query(Vehicle).filter(Vehicle.id == vehicle_id).first()

    if not vehicle:
        raise HTTPException(status_code=404, detail="Vehicle not found")

    if vehicle_data.plate_number:
        existing_plate = (
            db.query(Vehicle)
            .filter(Vehicle.plate_number == vehicle_data.plate_number, Vehicle.id != vehicle_id)
            .first()
        )
        if existing_plate:
            raise HTTPException(status_code=400, detail="Vehicle with this plate number already exists")

    if vehicle_data.vin:
        existing_vin = (
            db.query(Vehicle)
            .filter(Vehicle.vin == vehicle_data.vin, Vehicle.id != vehicle_id)
            .first()
        )
        if existing_vin:
            raise HTTPException(status_code=400, detail="Vehicle with this VIN already exists")

    update_data = vehicle_data.model_dump(exclude_unset=True)

    for field, value in update_data.items():
        setattr(vehicle, field, value)

    db.commit()
    db.refresh(vehicle)

    return vehicle


@router.delete("/{vehicle_id}", status_code=200)
def delete_vehicle(vehicle_id: uuid.UUID, db: Session = Depends(get_db)):
    vehicle = db.query(Vehicle).filter(Vehicle.id == vehicle_id).first()

    if not vehicle:
        raise HTTPException(status_code=404, detail="Vehicle not found")

    db.delete(vehicle)
    db.commit()

    return {"message": "Vehicle deleted successfully"}