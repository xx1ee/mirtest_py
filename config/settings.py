from pydantic import BaseSettings

class Settings(BaseSettings):
    base_url_ui: str = "https://example.com"
    base_url_api: str = "https://api.example.com"
    headless: bool = False
    timeout: int = 10000

    class Config:
        env_file = ".env"

settings = Settings()
