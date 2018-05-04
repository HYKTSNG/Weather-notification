import requests
from weather import get_weather
import time

from secure import LINE_API_TOKEN


def notify_the_weather():
    line_notify_token = LINE_API_TOKEN

    line_notify_api = 'https://notify-api.line.me/api/notify'

    weather_info = get_weather()
    if weather_info == "雨":
        message = "品川区 " + "雨だよ"
    else:
        message = "品川区 " + str(weather_info) + "℃"

    payload = {'message': message}
    headers = {'Authorization': 'Bearer ' + line_notify_token}  # 発行したトークン
    requests.post(line_notify_api, data=payload, headers=headers)


def worker():
    print(time.time())
    time.sleep(0)


interval = 3600
while True:
    notify_the_weather()
    time.sleep(interval)
