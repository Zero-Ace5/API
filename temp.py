import requests

KEY = "b660b92fd71230785504323bd4136050"
CITY = "Jaipur"

URL = "https://api.openweathermap.org/data/2.5/weather"
PARAMS = {
    "q": CITY,
    "appid": KEY,
    "units": "metric"
}

response = requests.get(URL, params=PARAMS, timeout=10)
data = response.json()

if data.get("cod") != 200:
    print("Error:", data.get("message"))
else:
    print(f"Temp in {CITY}: {data['main']['temp']}°C")
