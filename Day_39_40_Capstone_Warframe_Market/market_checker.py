import requests
from typing import Dict, Optional, Tuple

class WarframeMarketChecker:
    BASE_URL = "https://api.warframe.market/v1"

    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({"Language": "en", "Accept": "application/json"})

    def format_item_slug(self, raw_item_name: str) -> str:
        """Converts user input like 'Nidus Prime Chassis' into 'nidus_prime_chassis'."""
        cleaned = raw_item_name.strip().lower()
        return "_".join(cleaned.split())

    def get_best_order(self, item_slug: str) -> Optional[Dict]:
        """
        Fetches active sell orders for given item slug and returns the cheapest ingame offer.
        """
        endpoint = f"{self.BASE_URL}/items/{item_slug}/orders"
        try:
            response = self.session.get(endpoint, timeout=10)
            response.raise_for_status()
            orders = response.json().get("payload", {}).get("orders", [])
        except requests.RequestException as e:
            print(f"[ERROR] Failed to fetch orders for {item_slug}: {e}")
            return None

        # Filter: sell orders, only sellers currently in-game
        sell_orders = [
            order for order in orders
            if order.get("order_type") == "sell"
            and order.get("user", {}).get("status") == "ingame"
        ]

        if not sell_orders:
            return None

        # Find minimum price offer
        cheapest_order = min(sell_orders, key=lambda x: x.get("platinum", float("inf")))
        return cheapest_order

    def generate_chat_command(self, ign: str, item_name: str, price: int) -> str:
        """
        Generates standard Warframe whisper command for in-game paste.
        """
        return f'/w {ign} Hi! I want to buy: "{item_name}" for {price} platinum. (warframe.market)'