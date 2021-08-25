import requests
import json
import pyperclip
import os
from twilio.rest import Client

account_sid = "AC281b8e1fd4997c8afcca9f1a0a3cb2f8"
auth_token = "04b3c12980555da7605dd192a7476560"

OMW_Endpoint = "http://api.openweathermap.org/data/2.5/onecall"
API_KEY = "0dd054aec8adde42e4afafa78edbdd77"

parameters ={
    "lat": 52.229800,
    "lon": 21.011800,
    "appid": API_KEY,
    "exclude": "current,minutely,daily"
}


r = requests.get(OMW_Endpoint, params=parameters)
r.raise_for_status()
data = r.json()

will_rain = False

for i in range(47):
    condition_code = (data["hourly"][i]["weather"][0]["id"])
    if int(condition_code) < 700:
        will_rain = True
 
print(will_rain)



# if will_rain:
#     client = Client(account_sid, auth_token)
#     message = client.messages \
#                 .create(
#                      body="It is going to rain. Remember to take umbrella",
#                      from_='+18587682467',
#                      to='+48516500626'
#                  )

#     print(message.status)
