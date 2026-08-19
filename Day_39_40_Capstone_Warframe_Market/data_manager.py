import os
import requests
from typing import List, Dict
from dotenv import load_dotenv

load_dotenv()

class DataManager:
    def __init__(self):
        self.users_endpoint = os.getenv("SHEETY_USERS_ENDPOINT")
        self.items_endpoint = os.getenv("SHEETY_TRACKED_ITEMS_ENDPOINT")
        self.token = os.getenv("SHEETY_BEARER_TOKEN")
        self.headers = {"Authorization": f"Bearer {self.token}"} if self.token else {}

    def add_user(self, first_name: str, last_name: str, email: str) -> bool:
        payload = {
            "user": {
                "firstName": first_name,
                "lastName": last_name,
                "email": email
            }
        }
        res = requests.post(self.users_endpoint, json=payload, headers=self.headers)
        return res.status_code in (200, 201)

    def add_tracked_item(self, email: str, item_name: str, target_price: int, item_slug: str) -> bool:
        payload = {
            "trackedItem": {
                "userEmail": email,
                "itemName": item_name,
                "targetPrice": target_price,
                "itemUrlSlug": item_slug
            }
        }
        res = requests.post(self.items_endpoint, json=payload, headers=self.headers)
        return res.status_code in (200, 201)

    def get_users(self) -> List[Dict]:
        res = requests.get(self.users_endpoint, headers=self.headers)
        res.raise_for_status()
        return res.json().get("users", [])

    def get_tracked_items(self) -> List[Dict]:
        res = requests.get(self.items_endpoint, headers=self.headers)
        res.raise_for_status()
        return res.json().get("trackedItems", [])