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


def recommend_food_beverage_services():
    suffix = "/travel/food-beverage-evaluations"
    endpoint = AIRPORTS_API_URL + suffix
    response = requests.get(endpoint)
    if response.ok:
        json_resp = response.json()
        for evaluation in json_resp:
            airport = evaluation["evaluated_airport"]
            average_rating = evaluation["average_rating"]
            passenger_volume = evaluation["passenger_volume"]
            
            if passenger_volume > 100000 and average_rating < 3:
                print(f"Recomendado abrir servicios de alimentos/bebidas en {airport}")
    else:
        print(f"No es recomendable: {response}")

def main():
    log.info(f"Welcome to airport food and beverage service recommendation. App requests to: {AIRPORTS_API_URL}")
    recommend_food_beverage_services()

if __name__ == "__main__":
    main()
