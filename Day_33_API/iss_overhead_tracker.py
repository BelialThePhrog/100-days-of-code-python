import requests
from datetime import datetime
import smtplib
from apscheduler.schedulers.blocking import BlockingScheduler

MY_LAT = 51.507351 
MY_LONG = -0.127758 

def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    
    if abs(iss_latitude - MY_LAT) < 5 and abs(iss_longitude - MY_LONG) < 5:
        return True
    return False

def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    
    time_now = datetime.now().hour
    if time_now >= sunset or time_now <= sunrise:
        return True
    return False

def some_job():
    print(f"[{datetime.now().strftime('%H:%M:%S')}] Polling ISS position...")
    if is_iss_overhead() and is_night():
        print("ISS is overhead and visible! Triggering email sequence...")
        
        my_email = "example_of_an_email@gmail.com"
        password = "YOUR_APP_PASSWORD" # Use environment variables for security
        
        try:
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=my_email, password=password)
                connection.sendmail(
                    from_addr=my_email, 
                    to_addrs="addreser@gmail.com", 
                    msg="Subject:Look Up!\n\nThe ISS is directly above you."
                )
            print("Email sent successfully.")
        except Exception as e:
            print(f"SMTP Connection Error: {e}")
    else:
        print("ISS is not currently overhead or it is daytime.")

if __name__ == "__main__":
    print("Initializing ISS Background Tracker...")
    scheduler = BlockingScheduler()
    scheduler.add_job(some_job, 'interval', minutes=30)
    
    try:
        # scheduler.start() # Uncomment to run the loop
        print("Scheduler armed. Uncomment scheduler.start() to execute.")
    except (KeyboardInterrupt, SystemExit):
        print("Tracker terminated.")
