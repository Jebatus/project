from fastapi import FastAPI
from presentation.routes import users, orders, filters
from di import create_container

app = FastAPI(
    title="Magazin",
    version="1.0.0"
)

app.include_router(users.router, prefix="/users", tags=["Users"])