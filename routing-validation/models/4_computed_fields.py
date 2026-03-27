from pydantic import BaseModel, EmailStr, computed_field
from typing import List, Dict

class Patient(BaseModel):
    name: str
    email: EmailStr
    age: int
    height: float
    weight: float
    married: bool 
    allergies: List[str]
    contact_details: Dict[str, str]
    
    @computed_field
    @property
    def caculate_bmi(self) -> float:
        bmi = round(self.weight/(self.height**2),2)
        return bmi
    
def update_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print(patient.married)
    print("BMI", patient.caculate_bmi)
    print("Updated")

patient_info = {
    "name": "sahil patil",
    "email": "Sahilpatil@hdfc.com", 
    "age": 40,
    "height": 1.7,
    "weight": 60.0,
    "married": False,
    "allergies": ["pollen", "dust"],
    "contact_details": {"phone": "8989898989"}
}

patient1 = Patient(**patient_info)
update_patient_data(patient1)