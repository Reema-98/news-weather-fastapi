from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import Optional

from .. import schemas, database, oauth2
from ..services import weather_service

router = APIRouter(
    prefix="/weather",
    tags=["Weather"]
)

get_db = database.get_db

@router.get("/")
def get_weather(
    city: str = Query(..., description="City name, e.g., Delhi")):
    return weather_service.fetch_weather(city)