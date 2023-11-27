import uuid
from pydantic import BaseModel, Field



class Airport(BaseModel):
    airport_id: str = Field(default_factory=uuid.uuid4, alias="_id")
    airport_name: str
    city: str
    country: str

    class Config:
        populate_by_name  = True
        json_schema_extra = {
            "example": {
                "_id": "066de609-b04a-4b30-b46c-32537c7f1f6e",
                "airport_name": "Some Airport",
                "city": "Some City",
                "country": "Some Country"
            }
        }


class Travel(BaseModel):
    airline: str
    from_airport: str
    to_airport: str
    day: int
    month: int
    year: int
    age: int
    gender: str
    reason: str
    stay: str
    transit: str
    connection: bool
    wait: int

    class Config:
        populate_by_name = True
        json_schema_extra = {
            "example": {
                "airline": "Volaris",
                "from_airport": "066de609-b04a-4b30-b46c-32537c7f1f6e",
                "to_airport": "fbb3a71a-9f27-4aef-9a92-00a9b5884d42",
                "day": 1,
                "month": 12,
                "year": 2023,
                "age": 28,
                "gender": "Male",
                "reason": "Vacaciones/Placer",
                "stay": "Hotel",
                "transit": "Taxi del aeropuerto",
                "connection": False,
                "wait": 0
            }
        }


class FoodBeverageDemand(BaseModel):
    assessment_id: int = Field(...)
    evaluated_airport: str = Field(...)
    passenger_volume: int = Field(...)
    average_rating: float = Field(...)

    class Config:
        populate_by_name = True
        json_schema_extra = {
            "example": {
                "assessment_id": 1,
                "evaluated_airport": "LAX",
                "passenger_volume": 113250,
                "average_rating": 2.0
            }
        }
