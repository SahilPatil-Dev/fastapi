from pydantic import BaseModel
from typing import Optional

class Address(BaseModel):
    city: str
    state: str
    pin: str
    
class Patient(BaseModel):
    name: str
    gender: str
    age: int
    address: Optional[Address] = None
    
address_dict = {'city':'Mumbai', 'state': 'Maharashtra', 'pin': '400003'}
address1 = Address(**address_dict)
patient_dict = {'name':'sahil', 'gender':'male', 'age': 20, 'address': address1}
patient1 = Patient(**patient_dict)

patient_dict1 = {'name':'sahil', 'gender':'male', 'age': 20}
patient2 = Patient(**patient_dict1)

temp = patient1.model_dump()
temp1 = patient1.model_dump_json()
temp2 = patient1.model_dump(include=["name"])
temp3 = patient1.model_dump(exclude={"address":["state"]})
temp4 = patient2.model_dump(exclude_unset=True)

print(temp)
print(temp1)
print(temp2)
print(temp3)
print(temp4)
print(type(temp))
print(type(temp1))
print(type(temp2))