from sqlalchemy.ext.declarative import as_declarative, declared_attr
from sqlalchemy.orm import class_mapper
import uuid
from datetime import datetime
from decimal import Decimal

from sqlalchemy import Column, Integer, String, Boolean, DateTime, Time, Float, Text, ForeignKey, JSON, Numeric, Date, \
    TIMESTAMP, UUID
from sqlalchemy.ext.declarative import declarative_base


@as_declarative()
class Base:
    id: int
    __name__: str

    # Auto-generate table name if not provided
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    # Generic to_dict() method
    def to_dict(self):
        """
        Converts the SQLAlchemy model instance to a dictionary, ensuring UUID fields are converted to strings.
        """
        result = {}
        for column in class_mapper(self.__class__).columns:
            value = getattr(self, column.key)
                # Handle UUID fields
            if isinstance(value, uuid.UUID):
                value = str(value)
            # Handle datetime fields
            elif isinstance(value, datetime):
                value = value.isoformat()  # Convert to ISO 8601 string
            # Handle Decimal fields
            elif isinstance(value, Decimal):
                value = float(value)

            result[column.key] = value
        return result




class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    created_at = Column(Time, primary_key=False)
    name = Column(String, primary_key=False)
    email = Column(String, primary_key=False)
    password = Column(String, primary_key=False)


class Leads(Base):
    __tablename__ = 'leads'
    id = Column(Integer, primary_key=True)
    created_at = Column(Time, primary_key=False)
    name = Column(String, primary_key=False)
    email = Column(String, primary_key=False)
    mobile = Column(String, primary_key=False)
    file_name = Column(String, primary_key=False)
    address = Column(String, primary_key=False)
    city = Column(String, primary_key=False)
    state = Column(String, primary_key=False)
    pincode = Column(String, primary_key=False)
    message = Column(String, primary_key=False)
    source_type = Column(String, primary_key=False)
    company = Column(String, primary_key=False)
    status = Column(String, primary_key=False)


class Admins(Base):
    __tablename__ = 'admins'
    id = Column(Integer, primary_key=True)
    created_at = Column(Time, primary_key=False)
    name = Column(String, primary_key=False)
    email = Column(String, primary_key=False)
    password = Column(String, primary_key=False)


