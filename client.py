import argparse
import logging
import os
import requests

# Set logger
log = logging.getLogger()
log.setLevel('INFO')
handler = logging.FileHandler('airports.log')
handler.setFormatter(logging.Formatter("%(asctime)s [%(levelname)s] %(name)s: %(message)s"))
log.addHandler(handler)

# Read env vars related to API connection
AIRPORTS_API_URL = os.getenv("AIRPORTS_API_URL", "http://localhost:8000")


def print_airport(airport):
    for k in airport.keys():
        print(f"{k}: {airport[k]}")
    print("="*50)


def list_airports(country):
    suffix = "/travel/airports"
    endpoint = AIRPORTS_API_URL + suffix
    params = {
        "country": country
    }

    response = requests.get(endpoint, params=params)
    if response.ok:
        json_resp = response.json()
        for airport in json_resp:
            print_airport(airport)
    else:
        print(f"Error: {response}")


def recommend_food_beverage_services(airport_name, assessment_id=None):
    suffix = f"/travel/food-beverage-evaluations/{airport_name}"
    params = {}
    if assessment_id:
        params['assessment_id'] = assessment_id
    endpoint = AIRPORTS_API_URL + suffix
    response = requests.get(endpoint, params=params)
    if response.ok:
        recommendation = response.json()
        if recommendation["recommendation"] == "Recommended":
            print(f"Recomendado abrir servicios de alimentos/bebidas en {airport_name}")
        else:
            print(f"No es recomendable abrir otro servicio de alimentos/bebidas en {airport_name}")
    else:
        print(f"Error al obtener datos para el aeropuerto {airport_name}: {response}")

def main():
    log.info(f"Welcome to the airport food and beverage service recommendation app. Requests to: {AIRPORTS_API_URL}")
    parser = argparse.ArgumentParser()
    parser.add_argument("-a", "--airport", help="Specify an airport to evaluate for food/beverage services", required=True)
    parser.add_argument("-id", "--id", help="Specify an assessment ID", type=int, default=None)
    args = parser.parse_args()

    recommend_food_beverage_services(args.airport, args.id)

if __name__ == "__main__":
    main()
