from geopy.geocoders import Nominatim
import requests
import os
from dotenv import load_dotenv
from weather_api import get_weather

load_dotenv()

city = os.getenv("CITY")
geolocator = Nominatim(user_agent="meteo-discord")
location = geolocator.geocode(city)

weather = get_weather(location.latitude, location.longitude)

webhook_url = os.getenv("DISCORD_WEBHOOK_URL")
data = { "content": weather.display_message() }
requests.post(webhook_url, json=data)