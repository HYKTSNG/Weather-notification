import requests
import json
from secure import OPEN_WEATHER_API_KEY


def get_weather():
    response = requests.get(
        "http://api.openweathermap.org/data/2.5/weather?q=Shinagawa,JP&appid="
        + OPEN_WEATHER_API_KEY)

    data = json.loads(response.text)

    # print(data["name"])
    # print(data["main"])
    # print(data["weather"][0]["icon"])

    icon = data["weather"][0]["icon"]
    if icon == "09d" or \
            icon == "o9n" or \
            icon == "10d" or \
            icon == "10n" or \
            icon == "11d" or \
            icon == "11n":
        return "雨"
    else:
        temp = data["main"]["temp"]
        return temp - 273.15
