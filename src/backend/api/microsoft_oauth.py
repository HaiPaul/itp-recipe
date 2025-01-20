from fastapi import APIRouter, HTTPException, status
from fastapi.responses import RedirectResponse
from fastapi.security import OAuth2PasswordBearer
from jose import jwt
import requests
import os
from urllib.parse import urlencode
from dotenv import load_dotenv
import secrets

load_dotenv()

router = APIRouter(prefix="/auth", tags=["auth"])

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/auth/login")

client_id = os.getenv("MICROSOFT_CLIENT_ID")
client_secret = os.getenv("MICROSOFT_CLIENT_SECRET")
redirect_uri = os.getenv("MICROSOFT_REDIRECT_URI")
authority = os.getenv("MICROSOFT_AUTHORITY")
scope = os.getenv("MICROSOFT_SCOPE")
tenant = os.getenv("MICROSOFT_TENANT")

@router.get("/login")
async def login():
    state = secrets.token_urlsafe(16)
    params = {
        "client_id": client_id,
        "response_type": "code",
        "redirect_uri": redirect_uri,
        "response_mode": "query",
        "scope": scope,
        "state": state
    }
    login_url = f"{authority}/{tenant}/oauth2/v2.0/authorize?{urlencode(params)}"
    return RedirectResponse(login_url)

@router.get("/callback")
async def callback(code: str, state: str):
    token_url = f"{authority}/oauth2/v2.0/token"
    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {
        "client_id": client_id,
        "client_secret": client_secret,
        "grant_type": "authorization_code",
        "code": code,
        "redirect_uri": redirect_uri,
        "scope": scope
    }
    response = requests.post(token_url, headers=headers, data=data)
    if response.status_code != 200:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Failed to obtain token")

    token_data = response.json()
    id_token = token_data.get("id_token")
    if not id_token:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="No id_token in response")

    user_info = jwt.decode(id_token, options={"verify_signature": False})
    return user_info
