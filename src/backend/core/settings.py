from pydantic_settings import BaseSettings
from pydantic import computed_field
import os

class Settings(BaseSettings):
    BACKEND_CORS_ORIGINS: list[str] = ['http://localhost:5173']
    OPENAPI_CLIENT_ID: str = ""
    APP_CLIENT_ID: str = ""
    TENANT_ID: str = ""
    SCOPE_DESCRIPTION: str = "user_impersonation"
    REDIRECT_URI: str = ""

    def __init__(self) -> None:
        super().__init__()
        self.OPENAPI_CLIENT_ID = os.environ.get("OPENAPI_CLIENT_ID")
        self.APP_CLIENT_ID = os.environ.get("APP_CLIENT_ID")
        self.TENANT_ID = os.environ.get("TENANT_ID")
        self.REDIRECT_URI = os.environ.get("REDIRECT_URL")

    @computed_field
    @property
    def SCOPE_NAME(self) -> str:
        return f"api://{self.APP_CLIENT_ID}/{self.SCOPE_DESCRIPTION}"

    @computed_field
    @property
    def SCOPES(self) -> dict:
        return {
            self.SCOPE_NAME: self.SCOPE_DESCRIPTION,
        }

settings = Settings()