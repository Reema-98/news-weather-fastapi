import requests
import os
from fastapi import HTTPException
from dotenv import load_dotenv

load_dotenv()

WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")
print(" WEATHER_API_KEY:", WEATHER_API_KEY)
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def fetch_weather(city: str):
    if not WEATHER_API_KEY:
        raise HTTPException(status_code=500, detail="Missing WEATHER_API_KEY in environment")

    params = {
        "q": city,
        "appid": WEATHER_API_KEY,
        "units": "metric"
    }

    response = requests.get(BASE_URL, params=params)

    if response.status_code != 200:
        raise HTTPException(status_code=502, detail="Failed to fetch weather data")

    data = response.json()
    
    return {
        "city": data.get("name"),
        "temperature": data["main"]["temp"],
        "weather": data["weather"][0]["description"],
        "humidity": data["main"]["humidity"],
        "wind_speed": data["wind"]["speed"]
    }