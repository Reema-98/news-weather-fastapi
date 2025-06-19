import requests
import os
from fastapi import HTTPException
from dotenv import load_dotenv
from ..schemas import NewsResponse, NewsArticle

load_dotenv()

NEWS_API_KEY = os.getenv("NEWS_API_KEY")
BASE_URL = "https://newsapi.org/v2/everything"

def fetch_news(search: str = None) -> NewsResponse:
    params = {
        "apiKey": NEWS_API_KEY,
    }

    if search:
        params["q"] = search
    else:
        params["country"] = "in"

    response = requests.get(BASE_URL, params=params)
    print("Request URL:", response.url)
    print("Response JSON:", response.json())

    if response.status_code != 200:
        raise HTTPException(status_code=502, detail="Failed to fetch news from NewsAPI")

    data = response.json()
    articles = data.get("articles", [])

    result = NewsResponse(
        count=len(articles),
        articles=[
            NewsArticle(
                source=article.get("source"),
                author=article.get("author"),
                title=article.get("title"),
                description=article.get("description"),
                url=article.get("url"),
                publishedAt=article.get("publishedAt"),
            )
            for article in articles
        ]
    )
    return result