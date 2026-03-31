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