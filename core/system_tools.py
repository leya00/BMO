import datetime
import requests

def get_current_time():
    now = datetime.datetime.now()
    return now.strftime("%I:%M %p")

def get_current_date():
    today = datetime.date.today()
    return today.strftime("%A, %B %d")

def get_current_weather(city: str = "Melbourne") -> str:
    try:
        geo = requests.get(
            f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1",
            timeout=5
        ).json()

        lat = geo['results'][0]['latitude']
        lon = geo['results'][0]['longitude']

        wx = requests.get(
            f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true",
            timeout=5
        ).json()

        temp = wx['current_weather']['temperature']
        
        return f"{temp}°C in {city}"
    except Exception as e:
        return f"BMO could not check the weather! ({e})"