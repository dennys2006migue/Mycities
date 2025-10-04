from sqlalchemy import Column, Integer, String, Float
from .database import Base

class Incident(Base):
    __tablename__ = "incidents"
    id = Column(Integer, primary_key=True, index=True)
    type = Column(String, index=True)  # e.g., "basura", "accidente"
    latitude = Column(Float)
    longitude = Column(Float)
    description = Column(String)