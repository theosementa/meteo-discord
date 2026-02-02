import requests
from models import WeatherModel

def get_weather(latitude: float, longitude: float) -> WeatherModel:
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
	    "latitude": latitude,
	    "longitude": longitude,
        "daily": ["weather_code", "temperature_2m_max", "temperature_2m_min", "precipitation_probability_max"],
        "timezone": "auto",
        "forecast_days": 1
	    # "hourly": ["temperature_2m", "weather_code"],
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()

        daily_data = data['daily']
        temp_max = daily_data['temperature_2m_max'][0]
        temp_min = daily_data['temperature_2m_min'][0]
        
        rain_prob = daily_data['precipitation_probability_max'][0]
        wmo_code = daily_data['weather_code'][0]

        return WeatherModel(temp_max, temp_min, rain_prob, wmo_code)

    except requests.exceptions.RequestException as error:
        print(error)