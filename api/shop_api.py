import requests

from api.client import APIClient


class ShopAPI:
    def __init__(self):
        self.client = APIClient("https://dummyjson.com")

    def create_cart(self, user_id: int, products: list):
        if not products:
            raise ValueError("Products list cannot be empty")

        return self.client.post(
            "/carts/add",
            json={
                "userId": user_id,
                "products": products
            }
        )

    def login(self, username: str, password: str):
        """Логинимся через API и получаем токен"""
        return self.client.post(
            "/auth/login",
            json={"username": username, "password": password}
        )