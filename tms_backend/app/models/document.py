from app.core.database import Base
from app.models.base import BaseModelMixin

from sqlalchemy import Column, String


class Document(Base, BaseModelMixin):
    __tablename__ = "documents"

    type = Column(String, nullable=False) # enum
    number = Column(String, nullable=False)
    issued_date = Column(String, nullable=True)
    expire_date = Column(String, nullable=True)
    issued_by = Column(String, nullable=True)