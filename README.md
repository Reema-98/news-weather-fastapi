
# NewsWeatherAPI
A FastAPI application that delivers real-time news headlines and weather updates using NewsAPI and OpenWeatherMap. The app supports user authentication (JWT-based), organized using clean architecture with separate routers, services, and repository layers.

## Features

- User signup and login using JWT
- Fetch top headlines via NewsAPI (AUTHENTCATED ACCESS)
- Get current weather from OpenWeatherMap (NOT AUTHENTICATED)

## Tech Stack

- FastAPI
- SQLAlchemy
- PostgreSQL or SQLite
- JWT (OAuth2PasswordBearer)

## Getting Started

### 1. Clone the Repo
```bash
git clone https://github.com/your-username/news-weather-fastapi.git
cd news-weather-fastapi
```
### 2. Create Virtual Environment
```bash
python3 -m venv virtual-env
source virtual-env/bin/activate
```
### 3.Install Dependencies
```bash
pip install -r requirements.txt
```
### 4. Setup .env File
```bash
NEWS_API_KEY=your_news_api_key
WEATHER_API_KEY=your_weather_api_key
```
### 5. Run the App
```bash
uvicorn newsweather.main:app --reload
```

## API Endpoints

### Auth
- `POST /user/signup`
- `POST /login`
- `POST /logout`

### News (requires JWT)
- `GET /news?search=searchparamenter`

### Weather (public)
- `GET /weather?city=cityname`





