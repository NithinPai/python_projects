from fastapi import FastAPI
from app.routes import joke_routes

app = FastAPI()
app.include_router(joke_routes.router)

@app.get("/")
def read_root():
    return {"message": "Joke API is running"}