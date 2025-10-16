import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENWEATHER_API_KEY")
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

city = input("Enter city name: ")

params = {"q": city, "appid": API_KEY, "units": "metric"}

response = requests.get(BASE_URL, params=params)

if response.status_code == 200:
    data = response.json()
    print(f"🌤️ Weather in {data['name']}: {data['main']['temp']}°C")
    print(f"Condition: {data['weather'][0]['description']}")
elif response.status_code == 401:
    print("❌ Invalid API key. Please check your .env file or API key format.")
elif response.status_code == 404:
    print("🌧️ City not found. Please check the spelling.")
else:
    print(f"⚠️ Something went wrong (Error {response.status_code})")
