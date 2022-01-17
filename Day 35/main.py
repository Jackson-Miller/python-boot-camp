import os
import requests
from twilio.rest import Client

MY_LAT = 22.279199
MY_LONG = 114.171809
hours_to_forcast = 12
rain_forcast = True
ow_api_endpoint = "https://api.openweathermap.org/data/2.5/onecall"
ow_api_key = os.environ.get("OW_API_KEY")
twilio_account = os.environ.get("TWILIO_ACCOUNT")
twilio_api_key = os.environ.get("TWILIO_AUTH_TOKEN")

ow_parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "units": "imperial",
    "exclude": "current,minutely,daily",
    "appid": ow_api_key,
}

response = requests.get(ow_api_endpoint, params=ow_parameters)
response.raise_for_status()
weather_data = response.json()["hourly"]

for index in range(hours_to_forcast):
    hourly_data = weather_data[index]["weather"][0]
    if hourly_data["id"] < 700:
        rain_forcast = True

if rain_forcast:
    client = Client(twilio_account, twilio_api_key)
    message = client.messages \
        .create(
        body="It is going to rain today, remember to bring an ☔",
        from_='<phone number>',
        to='<phone number>'
    )

    print(message)
