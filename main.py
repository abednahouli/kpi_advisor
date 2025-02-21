from fastapi import FastAPI, Depends
from schema_extractor import get_database_schema, check_kpi_availability
from database import get_db

app = FastAPI()

@app.get("/schema", response_model=dict)  # Explicitly setting response_model as dict
def fetch_schema(db=Depends(get_db)):  # Fix: Correct way to use Depends
    schema = get_database_schema()
    return {"database_schema": schema}

@app.get("/check-kpis")
def check_kpis(db=Depends(get_db)):
    missing_columns = check_kpi_availability()
    return {"missing_columns": missing_columns}

@app.get("/")
def read_root():
    return {"message": "Welcome to the KPI Extractor API"}
