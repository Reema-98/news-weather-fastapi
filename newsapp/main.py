from fastapi import FastAPI
from . import models
from .database import engine
from .routers import news, weather, user, authentication


#initialize app
app = FastAPI()

#create all tables
models.Base.metadata.create_all(engine)

app.include_router(weather.router)
app.include_router(news.router)
app.include_router(user.router)
app.include_router(authentication.router)




