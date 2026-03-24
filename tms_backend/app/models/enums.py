import enum

from sqlalchemy import Enum as SAEnum


class Currency(str, enum.Enum):
    KZT = "KZT"
    USD = "USD"
    RUB = "RUB"
    EUR = "EUR"

CurrencyType = SAEnum(
    Currency,
    name="currency_enum",
    create_type=True,
    native_enum=True
)