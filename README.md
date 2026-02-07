# Healthcare EHR Management System

[![FastAPI](https://img.shields.io/badge/FastAPI-0.109-009688.svg)](https://fastapi.tiangolo.com/)
[![FHIR](https://img.shields.io/badge/FHIR-R4-orange.svg)](https://hl7.org/fhir/R4/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A **production-grade Electronic Health Record (EHR) management system** built with FastAPI and strictly adhering to the HL7 FHIR (Fast Healthcare Interoperability Resources) R4 standard. This platform provides a robust foundation for building interoperable healthcare applications, ensuring data consistency and security.

## 🚀 Features

- **FHIR R4 Compliant**: Native support for Patient, Observation, and Practitioner resources.
- **Interoperability Core**: Standardized API endpoints for exchanging healthcare data across systems.
- **Strict Validation**: Pydantic-based schema enforcement for all FHIR resources.
- **Search Capabilities**: Flexible FHIR-compliant search parameters for efficient record retrieval.
- **Security & Privacy**: Designed with data protection in mind, ready for HIPAA-compliant extensions.
- **Containerized**: Modular Docker setup for seamless deployment in healthcare IT environments.

## 📁 Project Structure

```
healthcare-ehr-management-system/
├── src/
│   ├── api/          # FHIR REST API handlers
│   ├── schema/       # FHIR resource models (Pydantic)
│   ├── services/     # Business logic and persistence
│   └── main.py       # Application entrypoint
├── tests/            # Unit and interoperability tests
├── Dockerfile
├── docker-compose.yml
└── requirements.txt
```

## 🛠️ Quick Start

```bash
# Clone
git clone https://github.com/Shivay00001/healthcare-ehr-management-system.git

# Install
pip install -r requirements.txt

# Run API
uvicorn src.main:app --host 0.0.0.0 --port 8000
```

## 📄 License

MIT License
