import os
from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient
from mangum import Mangum

# Configuración de MongoDB
MONGODB_URI = os.getenv("MONGODB_URI")
client = AsyncIOMotorClient(MONGODB_URI)
db = client[os.getenv("MONGODB_NAME")]
users_collection = db["users"]

# Configuración JWT
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 525600 * 100