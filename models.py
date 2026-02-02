from dataclasses import dataclass
from datetime import datetime

@dataclass
class WeatherModel:
    temp_max: float
    temp_min: float
    rain_prob: int
    wmo_code: int

    def display_message(self) -> str:
        current_day = datetime.today().strftime('%d %B %Y')
        return f"""
{current_day} - {weather_map.get(self.wmo_code, "???")}
Température max : {self.temp_max}°C
Température min : {self.temp_min}°C
Probabilité de pluie: {self.rain_prob}%
"""
    
weather_map = {
    0: "☀️ Ensoleillé",
    1: "🌤️ Globalement ensoleillé",
    2: "⛅ Partiellement nuageux",
    3: "☁️ Couvert",
    45: "🌫️ Brouillard",
    48: "🌫️ Brouillard givrant",
    51: "🌧️ Bruine légère",
    53: "🌧️ Bruine",
    55: "🌧️ Bruine dense",
    56: "❄️ Bruine verglaçante légère",
    57: "❄️ Bruine verglaçante",
    61: "☔ Pluie faible",
    63: "☔ Pluie",
    65: "☔ Pluie forte",
    66: "❄️ Pluie verglaçante légère",
    67: "❄️ Pluie verglaçante",
    71: "🌨️ Neige faible",
    73: "🌨️ Neige",
    75: "🌨️ Neige forte",
    77: "🌨️ Grains de neige",
    80: "🌧️ Averses légères",
    81: "🌧️ Averses",
    82: "🌧️ Fortes averses",
    85: "❄️ Averses de neige légères",
    86: "❄️ Averses de neige",
    95: "⚡ Orage",
    96: "⚡ Orage avec grêle légère",
    99: "⚡ Orage avec grêle"
}