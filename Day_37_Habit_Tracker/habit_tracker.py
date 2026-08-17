import requests
import datetime

pixela_endpoint = "https://pixe.la/v1/users"
TOKEN = "YOUR_PIXELA_TOKEN" # Security: Hidden token
USERNAME = "YOUR_USERNAME" # Security: Hidden username
graphID = "graph12"

headers = {
    "X-USER-TOKEN": TOKEN
}

print("1. Add Pixel")
print("2. Update Pixel")
print("3. Delete Pixel")
choice = input("Choose option (1/2/3): ").strip()

year = int(input("Year: "))
month = int(input("Month: "))
day = int(input("Day: "))

date_obj = datetime.datetime(year, month, day)
formatted_date = date_obj.strftime("%Y%m%d")

# 1. Add Pixel
if choice == "1":
    quantity = input("How many hours?: ")
    graph_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graphID}"
    graph_pixel_config = {
        "date": formatted_date,
        "quantity": str(quantity)
    }
    response = requests.post(url=graph_pixel_endpoint, json=graph_pixel_config, headers=headers)
    print(response.text)

# 2. Update Pixel
elif choice == "2":
    quantity = input("How many hours (new value)?: ")
    graph_pixel_update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graphID}/{formatted_date}"
    graph_pixel_update_config = {
        "quantity": str(quantity)
    }
    response = requests.put(url=graph_pixel_update_endpoint, json=graph_pixel_update_config, headers=headers)
    print(response.text)

# 3. Delete Pixel
elif choice == "3":
    graph_pixel_delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graphID}/{formatted_date}"
    response = requests.delete(url=graph_pixel_delete_endpoint, headers=headers)
    print(response.text)

else:
    print("Invalid choice!")
