from typing import Optional, List
from pydantic import BaseModel

# Modelos de datos

class UserCreate(BaseModel):
    username: str
    password: str

class User(BaseModel):
    username: str
    disabled: Optional[bool] = None

class UserInDB(User):
    hashed_password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None

class PatientData(BaseModel):
    symptoms: str
    age: int
    medical_history: List[str]
    family_history: List[str]
    gender: str

class MedicalRecommendation(BaseModel):
    specialty: str
    severity: int