import requests

base_url = "https://air-quality-api.open-meteo.com/v1/air-quality?"

def get_air_quality(miasto):
    url = f"{base_url}latitude={miasta[miasto][0]}&longitude={miasta[miasto][1]}&current=pm2_5"
    response = requests.get(url)
    data = response.json()
    return data

miasta = {
    "Wrocław": (51.1, 17.03),
    "Warszawa": (52.23, 21.01),
    "Kraków": (50.06, 19.95),
    "Gdańsk": (54.35, 18.65),
    "Poznań": (52.4, 16.93)
}

wyniki = {}
for miasto in miasta:
    wyniki[miasto] = get_air_quality(miasto)["current"]["pm2_5"]
print(f"Obecne wartości PM 2.5: {wyniki}")

najgorsze_miasta = sorted(wyniki, key = lambda x: wyniki[x], reverse = True)
print(f"Najwyższy poziom PM 2.5: {najgorsze_miasta[0]} ({wyniki[najgorsze_miasta[0]]} μg/m³)")




