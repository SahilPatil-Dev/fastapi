from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):
    name: Annotated[str, Field(max_length=50, title="Name of the Patient.", description="Give the name of the patient in less than 50 chars", examples=["Sahil", "Amit"])]
    email: EmailStr
    linkedin_url: AnyUrl
    age: int = Field(gt=0, lt=120)
    weight: float = Field(gt=0, lt=120)
    married: Annotated[bool, Field(default=None, description="Is the patient married or not")]
    allergies: Annotated[Optional[List[str]], Field(default=None, max_length=5)]
    contact_details: Dict[str, str]

def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print(patient.married)
    print(patient.contact_details)
    print("Inserted")

def update_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print(patient.married)
    print(patient.contact_details)
    print("Updated")
    
patient_info = {"name":"Sahil Patil", "email":"Sahilpatil@example.com", "linkedin_url": "https://linkedin.com", "age": 20, "weight": 60.0, "married": False, "allergies":["pollen", "dust"], "contact_details":{"phone": "8989898989"}}

patient1 = Patient(**patient_info)
update_patient_data(patient1)