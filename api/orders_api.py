from api.client import APIClient


class OrdersAPI:
    def __init__(self, base_url: str):
        self.client = APIClient(base_url)

    def create_order(self, user_id: int):
        return self.client.post("/orders", json={"user_id": user_id})

    def add_item(self, order_id: int, product_id: int, quantity: int):
        return self.client.post(
            f"/orders/{order_id}/items",
            json={
                "product_id": product_id,
                "quantity": quantity
            }
        )

    def confirm_order(self, order_id: int):
        return self.client.post(f"/orders/{order_id}/confirm", json={})

    def get_order(self, order_id: int):
        return self.client.get(f"/orders/{order_id}")
