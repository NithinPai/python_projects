## Project 2: Joke API with FastAPI

### Overview
- Fetches at jokes from [JokeAPI](https://v2.jokeapi.dev/).
- Processes jokes to extract fields (handling both "single" and "twopart" types).
- Stores the jokes in a PostgreSQL database.
- Provides a FastAPI endpoint to trigger the fetch and store process.

### Files
- `joke_api_fastapi.py` – FastAPI application for fetching and storing jokes.

### How to Run
1. **Install Dependencies:**
- pip install -r requirements.txt
2. **Set Up PostgreSQL:**
- Create a database (e.g., `jokes_db`) in PostgreSQL.
- Update the connection string accordingly.
3. **Run the FastAPI App:**
- uvicorn app.main:app --reload
4. **Test the Endpoint:**
- Navigate to [http://127.0.0.1:8000/jokes] to trigger the joke fetching process.

