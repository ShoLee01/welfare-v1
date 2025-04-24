import os
from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient
from mangum import Mangum

# Configuración de MongoDB
MONGODB_URI = os.getenv("MONGODB_URI")
client = AsyncIOMotorClient(MONGODB_URI)
MONGODB_NAME = os.getenv("MONGODB_NAME")
db = client[MONGODB_NAME]
users_collection = db["users"]

# Configuración JWT
SECRET_KEY = "fastapi-insecure-7qp@z!16c03sb1qfgxqvxh=j5bhzcz!qo&p!p4dsiix&v$zrl9"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 525600 * 100