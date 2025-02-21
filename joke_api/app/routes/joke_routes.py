from fastapi import APIRouter
from app.services.joke_service import fetch_and_store_jokes

router = APIRouter()

@router.post("/jokes")
def fetch_jokes():
    return fetch_and_store_jokes()