from fastapi import FastAPI
from contextlib import asynccontextmanager
from typing import AsyncGenerator
from fastapi_azure_auth import SingleTenantAzureAuthorizationCodeBearer
from core.settings import settings

azure_scheme = SingleTenantAzureAuthorizationCodeBearer(
    app_client_id=settings.APP_CLIENT_ID,
    tenant_id=settings.TENANT_ID,
    scopes=settings.SCOPES,
)

@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    await azure_scheme.openid_config.load_config()
    yield