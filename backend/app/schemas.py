from pydantic import BaseModel

class IncidentCreate(BaseModel):
    type: str
    latitude: float
    longitude: float
    description: str

class Incident(IncidentCreate):
    id: int