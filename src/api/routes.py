from fastapi import APIRouter, HTTPException, Path
from src.schema.fhir_models import Patient, Observation
from typing import List

router = APIRouter()

# Mock database
patients_db = {}
observations_db = {}

@router.post("/Patient", response_model=Patient)
async def create_patient(patient: Patient):
    patient_id = str(len(patients_db) + 1)
    patient.id = patient_id
    patients_db[patient_id] = patient
    return patient

@router.get("/Patient/{id}", response_model=Patient)
async def get_patient(id: str = Path(...)):
    if id not in patients_db:
        raise HTTPException(status_code=404, detail="Patient not found")
    return patients_db[id]

@router.post("/Observation", response_model=Observation)
async def create_observation(observation: Observation):
    obs_id = str(len(observations_db) + 1)
    observation.id = obs_id
    observations_db[obs_id] = observation
    return observation

@router.get("/Observation", response_model=List[Observation])
async def list_observations(patient_id: Optional[str] = None):
    if patient_id:
        return [obs for obs in observations_db.values() if obs.subject.get("reference") == f"Patient/{patient_id}"]
    return list(observations_db.values())
