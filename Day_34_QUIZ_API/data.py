import requests

parameters = {
    "amount":10,
    "difficulty":"medium",
    "type":"boolean"
}
try:
    response = requests.get(url="https://opentdb.com/api.php",params = parameters)
    print(response)
except requests.exceptions.HTTPError as errh:
  print("HTTP Error")
  print(errh.args[0])
except requests.exceptions.ReadTimeout as errrt:
  print("Time out")
except requests.exceptions.ConnectionError as conerr:
  print("Connection error")

response.raise_for_status()
question_data = response.json()["results"]
