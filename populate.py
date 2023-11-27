import csv
import requests

BASE_URL = "http://localhost:8000"


def load_air():
    with open("Data/Airports.csv") as fd:
        airports_csv = csv.DictReader(fd)
        for airport in airports_csv:
            del airport["airport_id"]
            x = requests.post(BASE_URL+"/travel/airports", json=airport)
            if not x.ok:
                print(f"Failed to post airport {x} - {airport}")


def load_demandas():
    with open("Data/demandas_de_alimentos.csv") as fd:
        demandas_csv = csv.DictReader(fd)
        for demanda in demandas_csv:
            demanda["passenger_volume"] = int(demanda["passenger_volume"])
            demanda["average_rating"] = float(demanda["average_rating"])
            try:
                response = requests.post(BASE_URL + "/travel/demandas", json=demanda)
                if not response.ok:
                    print(f"Error: {response.status_code}, Response: {response.text}")
            except Exception as e:
                print(f"Error al realizar la solicitud: {e}")






def load_travels():
    with open("Data/flights.csv") as fd:
        travels_csv = csv.DictReader(fd)
        for travel in travels_csv:
            x = requests.post(BASE_URL + "/travel/travels", json=travel)
            if not x.ok:
                print(f"Failed to post travel {x} - {travel}")


if __name__ == "__main__":
    # Mandamos ejecutar las cargas de datos
    load_air()
    load_demandas()
    load_travels()