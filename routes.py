from fastapi import APIRouter, Request, HTTPException, status, Body
from typing import List
from model import Airport, FoodBeverageDemand, Travel
from fastapi.encoders import jsonable_encoder

router = APIRouter()


@router.post("/airports", response_description="Add a new airport",
             status_code=status.HTTP_201_CREATED, response_model=Airport)
def create_airport(request: Request, airport: Airport = Body(...)):
    airport = jsonable_encoder(airport)
    new_airport = request.app.database["airports"].insert_one(airport)
    created_airport = request.app.database["airports"].find_one(
        {"_id": new_airport.inserted_id}
    )
    return created_airport


@router.post("/demandas", response_description="Add a new food and beverage demand", status_code=status.HTTP_201_CREATED)
def create_demanda(request: Request, demanda: FoodBeverageDemand = Body(...)):
    demanda_dict = jsonable_encoder(demanda)
    new_demanda = request.app.database["demandas"].insert_one(demanda_dict)
    created_demanda = request.app.database["demandas"].find_one({"_id": new_demanda.inserted_id})
    return created_demanda



@router.post("/travels", response_description="Add a new travel",
             status_code=status.HTTP_201_CREATED, response_model=Travel)
def create_travel(request: Request, travel: Travel = Body(...)):
    travel = jsonable_encoder(travel)
    new_travel = request.app.database["travels"].insert_one(travel)
    created_travel = request.app.database["travels"].find_one(
        {"_id": new_travel.inserted_id}
    )
    return created_travel


@router.get("/", response_description="Get airports in a country", response_model=List[Airport])
def get_airports(request: Request, country: str = "USA"):
    airports = list(request.app.database["airports"].find({"country": {"$eq": country}}))
    return airports



