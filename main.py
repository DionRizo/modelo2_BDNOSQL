import os
from fastapi import FastAPI
from pymongo import MongoClient
from routes import router

MONGODB_URI = os.getenv('MONGODB_URI', 'mongodb://localhost:27017')
DB_NAME = os.getenv('MONGODB_DB_NAME', 'Proyecto')

app = FastAPI()
app.include_router(router, tags=["travel"], prefix="/travel")

async def startup_event():
    app.mongodb_client = MongoClient(MONGODB_URI)
    app.database = app.mongodb_client[DB_NAME]
    print(app.database.client)
    print(f"Connected to MongoDB at: {MONGODB_URI} \n\t Database: {DB_NAME}")

async def shutdown_event():
    app.mongodb_client.close()
    print("Bye bye...!!")

app.add_event_handler("startup", startup_event)
app.add_event_handler("shutdown", shutdown_event)
