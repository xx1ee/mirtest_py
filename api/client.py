import requests

class APIClient:
    def __init__(self, base_url: str):
        self.base_url = base_url

    def post(self, path: str, json: dict):
        response = requests.post(f"{self.base_url}{path}", json=json)
        response.raise_for_status()
        return response

    def get(self, path: str, headers: dict = None):
        response = requests.get(f"{self.base_url}{path}", headers=headers)
        response.raise_for_status()
        return response
