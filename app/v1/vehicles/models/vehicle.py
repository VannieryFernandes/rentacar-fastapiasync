from sqlalchemy import Column, Integer, String, Boolean

from v1.db.config import Base

class Vehicle(Base):
    __tablename__ = 'vehicles'

    id = Column(Integer, primary_key=True)
    model = Column(String, nullable=False)
    license_number = Column(String, nullable=False)
    reserved = Column(Boolean, nullable=False)