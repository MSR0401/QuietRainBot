import requests
from twilio.rest import Client

account_sid = "Account_Sid"
auth_token = "Auth_token"
api_key = "Api_key"


weather_params = {
    "lat": 78.807510,
    "exclude": "current,minutely,daily",
    "lon": -79.508910,
    "appid": api_key
}
response = requests.get(url="https://api.openweathermap.org/data/2.8/onecall", params=weather_params)
response.raise_for_status()
data = response.json()
weather_slice = data["hourly"][:11]  # Want a total of 12 hours of data

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today.Don't forget to carry your umbrella ☂",
        from_='+12342991016',
        to='+15198317960'
    )
    print(message.status)