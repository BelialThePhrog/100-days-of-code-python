import requests
import html
import smtplib

api_key = "YOUR_API_KEY_HERE"
my_email = "example_of_an_email@gmail.com"
password = "YOUR_APP_PASSWORD"

parameters = {
    "lat":54.352024,
    "lon":18.646639,
    "appid":api_key,
    "cnt": 4
}

try:
    response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast",params = parameters)
    print(response)
except requests.exceptions.HTTPError as errh:
  print("HTTP Error")
  print(errh.args[0])
except requests.exceptions.ReadTimeout as errrt:
  print("Time out")
except requests.exceptions.ConnectionError as conerr:
  print("Connection error")

response.raise_for_status()
will_rain = False
weather_data = response.json()
raining = weather_data["list"][0]["weather"][0]["id"]
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
if will_rain:
    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls
    connection.login(user = my_email, password = password)
    connection.sendmail(from_addr = my_email, t_addrs = "addreser@gmail.com", msg="Subject:Rain Alert\n\nWill Rain")
    connection.close()

    
print(weather_data)
