import requests

class APIClient:
    def __init__(self, base_url: str):
        self.base_url = base_url

    def get(self, path: str):
        return requests.get(f"{self.base_url}{path}")

    def post(self, path: str, json: dict):
        return requests.post(f"{self.base_url}{path}", json=json)
