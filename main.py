import os
import requests
from twilio.rest import Client

MY_LAT = 32.080898
MT_LONG = -81.091202
API_KEY = "bfbd05baca9a4d02d0159c62ae9b978a" # os.environ.get("API_KEY")
account_sid = "AC63f919d11afd5c70ffc6f27c3bf39e15"
auth_token = "bb7b95390da997ff37c04635842bbffe" # os.environ.get("AUTH_TOKEN")

BASE_URL = "https://api.openweathermap.org/data/2.5/forecast"

parameters = {
    "lat": MY_LAT,
    "lon": MT_LONG,
    "appid": API_KEY,
    "cnt": 4
}

weather_data = requests.get(url=BASE_URL, params=parameters).json()

will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It might rain in sometime, bring your umbrella ☔",
        from_="+16592772178",
        to="+917277679361"
    )
    print(message.status)
