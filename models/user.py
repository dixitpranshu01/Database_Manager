from pydantic import BaseModel


class User(BaseModel):
    person_name: str
    educational_qualification: str
    address: int and str
    email: str
    phone: int
    medical_history: int and str
    family_income: int
    voter_id: int
