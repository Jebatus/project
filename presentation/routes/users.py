from fastapi import FastAPI
from schemas import UserCreate
from application.interfaces.user_service import UserServiceInterface
from fastapi import APIRouter, FastAPI

router = APIRouter()

@router.post("/register")
def register(user: UserCreate):
    return {"message": "succeed"}


