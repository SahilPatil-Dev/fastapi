from fastapi import FastAPI, Path, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field, computed_field
from typing import Annotated, Literal, Optional
import json

app = FastAPI()

class Patient(BaseModel):
    id: Annotated[str, Field(..., description="ID of the patient", examples=["P001"])]
    name: Annotated[str, Field(..., description="Name of the patient")]
    city: Annotated[str, Field(..., description="City where the patient is living")]
    age: Annotated[int, Field(..., gt=0, lt=120, description="Age of the patient")]
    gender: Annotated[Literal["Male", "Female", "Others"], Field(..., description="Gender of the patient")]
    height: Annotated[float, Field(..., gt=0, description="Height of the patient in mtrs")]
    weight: Annotated[float, Field(..., gt=0, description="Weight of the patient in kgs")]
    
    @computed_field
    @property
    def verdict(self) -> str:
        if self.bmi < 18.5:
            return "Underweight"
        elif self.bmi < 25:
            return "Normal"
        elif self.bmi < 30:
            return "Overweight"
        else:
            return "Obese"
        
    @computed_field
    @property
    def bmi(self) -> float:
        bmi = round(self.weight/(self.height**2), 2)
        return bmi

class PatientUpdate(BaseModel):
    name: Annotated[Optional[str], Field(default=None)]
    city: Annotated[Optional[str], Field(default=None)]
    age: Annotated[Optional[int], Field(default=None, gt=0)]
    gender: Annotated[Optional[Literal["Male", "Female", "Others"]], Field(default=None)]
    height: Annotated[Optional[float], Field(default=None, gt=0)]
    weight: Annotated[Optional[float], Field(default=None, gt=0)]

def load_data():
    try:
        with open("patients.json", 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def save_data(data):
    with open("patients.json", "w") as f:
        json.dump(data, f, indent=4)
        
@app.get("/")
def root():
    return {"message": "Patient Management System API"}

@app.get("/patients")
def get_all_patients():
    data = load_data()
    result = []

    for patient_id, patient_info in data.items():
        patient_copy = patient_info.copy()
        patient_copy["id"] = patient_id
        result.append(Patient(**patient_copy))

    return result

@app.get("/patients/{patient_id}")
def get_patient(patient_id: Annotated[str, Path(pattern="^P\\d{3}$")]):
    data = load_data()

    if patient_id not in data:
        raise HTTPException(status_code=404, detail="Patient Not Found")

    patient_data = data[patient_id].copy()
    patient_data["id"] = patient_id

    return Patient(**patient_data)

@app.post("/patients", response_model=Patient)
def create_patient(patient: Patient):
    data = load_data()

    if patient.id in data:
        raise HTTPException(status_code=400, detail="Patient already exists")
    
    data[patient.id] = patient.model_dump(exclude=["id", "bmi", "verdict"])
    
    save_data(data)

    return patient

@app.put('/edit/{patient_id}')
def update_patient(patient_id: Annotated[str, Path(pattern="^P\\d{3}$")], patient_update: PatientUpdate):
    data = load_data()

    if patient_id not in data:
        raise HTTPException(status_code=404, detail="Patient Not Found")
    
    existing_patient_info = data[patient_id]
    
    updated_patient_info = patient_update.model_dump(exclude_unset=True)

    for key, value in updated_patient_info.items():
        existing_patient_info[key] = value
        
    # existing_patient_info -> pydantic object -> updated bmi + verdict
    existing_patient_info["id"] = patient_id
    patient_pydantic_obj = Patient(**existing_patient_info)
    
    # -> pydantic object -> dict
    existing_patient_info = patient_pydantic_obj.model_dump(exclude=["id", "bmi", "verdict"])
    
    # add this dict to data
    data[patient_id] = existing_patient_info

    # save data
    save_data(data)
    
    return JSONResponse(status_code=200, content={"message": "patient updated"})

@app.delete('/delete/{patient_id}')
def delete_patient(patient_id: Annotated[str, Path(pattern="^P\\d{3}$")]):
    
    data = load_data()

    if patient_id not in data:
        raise HTTPException(status_code=404, detail="Patient Not Found")
    
    del data[patient_id]
    
    save_data(data)

    return JSONResponse(status_code=200, content={'message': 'Patient Deleted'})
