from fastapi import FastAPI
from src.api.routes import router as fhir_router

app = FastAPI(title="Healthcare EHR Management System")

# FHIR Base URL
app.include_router(fhir_router, prefix="/fhir")

@app.get("/health")
async def health():
    return {"status": "ok", "standard": "FHIR R4"}
