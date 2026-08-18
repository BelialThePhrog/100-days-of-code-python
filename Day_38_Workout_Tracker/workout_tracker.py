import requests
import datetime
import time

APP_ID = "YOUR_APP_ID" # Security: Hidden APP_ID
APP_KEY = "YOUR_APP_KEY" # Security: Hidden APP_KEY
TOKEN = "YOUR_BEARER_TOKEN" # Security: Hidden Bearer Token

headers = {
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY
}

headers_2 = {
    "Authorization": f"Bearer {TOKEN}"
}
app_brewery_endpoint = "https://app.100daysofpython.dev//v1/nutrition/natural/exercise"
sheety_post = "YOUR_SHEETY_ENDPOINT" # Security: Hidden endpoint

year = int(input("Year: "))
month = int(input("Month: "))
day = int(input("Day: "))
hour = int(input("Hour: "))
minutes = int(input("Minute: "))
sec = int(input("Seconds: "))

date_obj = datetime.datetime(year, month, day)
hour_obj = datetime.time(hour, minutes, sec)

exercise_1 = str(input("What did you do?"))
exercise_config = {
        "query": exercise_1
    }
response = requests.post(url=app_brewery_endpoint, json=exercise_config, headers=headers)
result = response.json()
print(result["exercises"][0])

duration_done = result["exercises"][0]["duration_min"]
exercise_done = result["exercises"][0]["name"]
Calories_done = result["exercises"][0]["nf_calories"]
formatted_date = date_obj.strftime("%d/%m/%Y")
formmated_hour = hour_obj.strftime("%H:%M:%S")
for exercise in result.get("exercises", []):
    excel_config = {
            "workout": {
                "date": formatted_date,
                "time": formmated_hour,
                "exercise": exercise["name"].title(),
                "duration" : exercise["duration_min"],
                "calories": exercise["nf_calories"],
        }
    }
    response = requests.post(url=sheety_post, json=excel_config, headers=headers_2)
    time.sleep(3)

print(response.text)
