import requests,datetime, smtplib, time
from twilio.rest import Client
twlio_number = "your twlio generated number"
auth_token = "your twlio auth token"
account_sid = "your twlio account sid"
para = {
    "lat" : "18.520430",
    "lon": "73.856743",
    "appid":"your id",
    "exclude":"current,minutely,daily"
}
response = requests.get(url="https://api.openweathermap.org/data/2.8/onecall", params=para)

weather_data = response.json()
hourly_data = weather_data["hourly"][:12]
weather_id = [i["weather"][0]["id"] for i in hourly_data]
will_rain = False
for i in weather_id:
    if i < 700:will_rain = True
if will_rain == True:
    client = Client(account_sid, auth_token)
    message = client.messages \
                .create(
                     body="It will rain today.\nBring Umberalla",
                     from_= twlio_number,
                     to='your number'
                 )