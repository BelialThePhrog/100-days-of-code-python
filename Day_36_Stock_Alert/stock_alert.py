import os
import smtplib
import requests

API_KEY = "6DQXC5QJNY5GZWGK"
MY_EMAIL = "example_of_an_email@gmail.com"
APP_PASSWORD = os.environ.get("GMAIL_APP_PASSWORD")  
TO_EMAIL = "addreser@gmail.com"

parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": "MSFT",
    "apikey": API_KEY,
}

try:
    response = requests.get("https://www.alphavantage.co/query", params=parameters)
    response.raise_for_status()
    data = response.json()
except requests.exceptions.RequestException as err:
    print(f"Network error: {err}")
    data = {}

if "Time Series (Daily)" in data:
    time_series = data["Time Series (Daily)"]
    dates = list(time_series.keys())

    today_data = time_series[dates[0]]
    prev_data = time_series[dates[1]]

    today_open = float(today_data["1. open"])
    prev_close = float(prev_data["4. close"])

    diff = round(today_open - prev_close, 2)
    percentage = round((abs(diff) / prev_close) * 100, 5)

    status = "Growth" if diff >= 0 else "Loss"
    subject = f"MSFT Alert: {status} of {percentage}%"
    body = f"Subject: {subject}\n\nMSFT moved by ${diff} ({percentage}%) compared to previous close."

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=APP_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=TO_EMAIL, msg=body)
    print("Email sent successfully.")
else:
    print("Failed to fetch stock data. API response:", data
