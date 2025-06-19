from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from typing import Optional

from .. import schemas, database, oauth2
from ..services import news_service

router = APIRouter(
    prefix="/news",
    tags=["News"]
)

get_db = database.get_db

@router.get("/", response_model=schemas.NewsResponse)
def get_news(
    search: Optional[str] = Query(None, description="Search term for news articles"),
    db: Session = Depends(get_db),
    current_user: schemas.User = Depends(oauth2.get_current_user)  # JWT required
):

    return news_service.fetch_news(search)