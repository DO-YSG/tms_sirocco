import enum

from sqlalchemy import Enum as SAEnum


class Currency(str, enum.Enum):
    KZT = "KZT"
    USD = "USD"
    RUB = "RUB"
    EUR = "EUR"

CurrencyType = SAEnum(Currency, name="currency_enum", create_type=True)


class Status(str, enum.Enum):
    active = "active"
    inactive = "inactive"
    blocked = "blocked"
    archived = "archived"

StatusType = SAEnum(Status, name="status_enum", create_type=True)


class LocationType(str, enum.Enum):
    plant = "plant"
    warehouse = "warehouse"
    dealer = "dealer"
    parking = "parking"
    service = "service"
    other = "other"

LocationTypeType = SAEnum(LocationType, name="location_type_enum", create_type=True)


class LicenseCategory(str, enum.Enum):
    a1 = "A1"
    a = "A"
    b1 = "B1"
    b = "B"
    c1 = "C1"
    c = "C"
    d1 = "D1"
    d = "D"
    be = "BE"
    c1e = "C1E"
    ce = "CE"
    d1e = "D1E"
    de = "DE"

LicenseCategoryType = SAEnum(LicenseCategory, name="license_category_enum", create_type=True)

class VehicleType(str, enum.Enum):
    truck_tractor = "truck_tractor"
    semi_trailer = "semi_trailer"
    tow_truck = "tow_truck"
    trailer = "trailer"
    car = "car"
    van = "van"

VehicleTypeType = SAEnum(VehicleType, name="vehicle_type_enum", create_type=True)


class VehicleCategory(str, enum.Enum):
    m1 = "M1"
    m2 = "M2"
    m3 = "M3"
    n1 = "N1"
    n2 = "N2"
    n3 = "N3"
    o1 = "O1"
    o2 = "O2"
    o3 = "O3"

VehicleCategoryType = SAEnum(VehicleCategory, name="vehicle_category_enum", create_type=True)