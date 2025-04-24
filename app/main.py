# main.py
from fastapi import FastAPI, Body
from mangum import Mangum
from fastapi import Depends, HTTPException, status
from settings import (
    users_collection,
)
from fastapi.middleware.cors import CORSMiddleware
from security import (
    get_user,
    get_current_user,
    pwd_context,
    authenticate_user,
    create_access_token
)
from models import (
    UserInDB,
    UserCreate,
    Token,
    User,
    PatientData
)
from utils.string_utils import get_medical_recommendation

# Configuración inicial
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

MAIN_ROUTE = "/api/v1"

@app.post(f"{MAIN_ROUTE}/register")
async def register(user_data: UserCreate):  # Usa el modelo como parámetro
    existing_user = await get_user(user_data.username)
    if existing_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    
    hashed_password = pwd_context.hash(user_data.password)
    user = UserInDB(username=user_data.username, hashed_password=hashed_password)
    
    await users_collection.insert_one(user.model_dump())
    return {"message": "User created successfully"}

@app.post(f"{MAIN_ROUTE}/login", response_model=Token)
async def login_for_access_token(form_data: UserCreate):
    user = await authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}

@app.post(f"{MAIN_ROUTE}/diagnosis")
async def diagnosis(current_user: User = Depends(get_current_user), 
                    patient_data: PatientData = Body(...)):
    diagnosis = await get_medical_recommendation(patient_data)
    return diagnosis

handler = Mangum(app)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)