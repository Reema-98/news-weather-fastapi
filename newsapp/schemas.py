from pydantic import BaseModel
from typing import List,Optional
from datetime import datetime

#User schemas
class User(BaseModel):
    name: str
    email: str
    password: str

class ShowUser(BaseModel):
    name: str
    email: str

    class Config():
        from_attributes = True




#Auth schemas
class Login(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: str | None = None


#News schemas
class NewsArticle(BaseModel):
    source: Optional[dict]
    author: Optional[str]
    title: str
    description: Optional[str]
    url: str
    publishedAt: datetime

class NewsResponse(BaseModel):
    count: int
    articles: List[NewsArticle]



#WeatherSchemas
class WeatherEntry(BaseModel):
    date: str
    main: str
    temp: float


class WeatherResponse(BaseModel):
    location: str
    unit: str
    data: List[WeatherEntry]





