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


@router.post("/demandas", response_description="Add a new food and beverage demand", 
             status_code=status.HTTP_201_CREATED, response_model=FoodBeverageDemand)
async def create_demanda(request: Request, demanda: FoodBeverageDemand = Body(...)):
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


@router.get("/airports", response_description="Get airports in a country", response_model=List[Airport])
def get_airports(request: Request, country: str = "USA"):
    airports = list(request.app.database["airports"].find({"country": {"$eq": country}}))
    return airports

@router.get("/food-beverage-evaluations/{airport_name}", response_description="Evaluate food and beverage services for a specific airport")
def evaluate_food_beverage_services(airport_name: str, request: Request, assessment_id: int = None):
    query = {"evaluated_airport": airport_name}
    if assessment_id is not None:
        query["assessment_id"] = assessment_id

    evaluations = list(request.app.database["demandas"].find(query))

    if not evaluations:
        raise HTTPException(status_code=404, detail=f"No evaluation data found for the specified criteria.")

    # Calcular el promedio de calificaciones y el volumen total de pasajeros
    total_rating, total_volume = 0, 0
    for evaluation in evaluations:
        total_rating += evaluation["average_rating"]
        total_volume += evaluation["passenger_volume"]
    
    if evaluations:
        average_rating = total_rating / len(evaluations)
    else:
        average_rating = 0

    # Lógica para determinar si es recomendable abrir servicios
    recommendation = "Not Recommended"
    if total_volume > 100000 and average_rating < 3:
        recommendation = "Recommended"

    return {"airport": airport_name, "recommendation": recommendation}
