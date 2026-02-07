from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime

class FHIRResource(BaseModel):
    resourceType: str
    id: Optional[str] = None
    meta: Optional[dict] = None

class Patient(FHIRResource):
    resourceType: str = "Patient"
    active: bool = True
    name: List[dict] = []
    gender: Optional[str] = None
    birthDate: Optional[str] = None
    telecom: List[dict] = []

class Observation(FHIRResource):
    resourceType: str = "Observation"
    status: str
    code: dict
    subject: dict # Reference to Patient
    effectiveDateTime: Optional[datetime] = None
    valueQuantity: Optional[dict] = None
