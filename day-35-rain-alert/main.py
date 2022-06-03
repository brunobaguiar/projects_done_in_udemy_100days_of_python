import requests
from twilio.rest import Client

OWN_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "f7860c61cb9b5cdb72571a9d13c10a9e"
account_sid = 'ACa10d9456df04aa1cf8a254dabc06f48d'
auth_token = '3c81b534c1b685b95ae0aac1019f9e08'


weather_params = {
    "lat": -2.997450,
    "lon": -47.353450,
    "appid": api_key,
    "exclude": "current,minutely,daily",
}

response = requests.get(OWN_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
# print(weather_data["hourly"][0]["weather"][0]["id"])
weather_slice = weather_data["hourly"][:12]
# print(weather_slice)

is_going_to_rain = False
for hour in weather_slice:
    condition_code = hour["weather"][0]["id"]
    if int(condition_code) < 700:
        is_going_to_rain = True

if is_going_to_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an umbrella 🌂",
        from_='+1599999999',
        to='+5511999999999'
    )
    print(message.status)
