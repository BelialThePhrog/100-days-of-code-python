import requests

try:
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    
    data = response.json()
    longitude = data["iss_position"]["longitude"]
    latitude = data["iss_position"]["latitude"]
    
    iss_position = (longitude, latitude)
    print("ISS Position:", iss_position)
    
except requests.exceptions.HTTPError as errh:
    print("HTTP Error:", errh.args[0])
except requests.exceptions.ReadTimeout as errrt:
    print("Time out")
except requests.exceptions.ConnectionError as conerr:
    print("Connection error")
