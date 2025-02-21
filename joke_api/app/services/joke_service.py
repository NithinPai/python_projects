import requests
from app.db.db_config import get_db_url
from sqlalchemy import create_engine, text
from fastapi import HTTPException

def insert_jokes(jokes):
    """Insert multiple jokes into the database with processed fields."""
    from sqlalchemy import create_engine, text
    import json

    engine = create_engine(get_db_url())

    if isinstance(jokes, dict):
        jokes = [jokes] 

    with engine.begin() as connection:
        for joke in jokes:
            if isinstance(joke, str):
                # Convert JSON string to dict
                try:
                    joke = json.loads(joke)
                except json.JSONDecodeError:
                    raise ValueError("Invalid JSON format in joke object")

            joke_type = joke.get('type')
            joke_text = joke.get('joke') if joke_type == 'single' else None
            setup = joke.get('setup') if joke_type == 'twopart' else None
            delivery = joke.get('delivery') if joke_type == 'twopart' else None
            flags = joke.get('flags', {})
            nsfw = flags.get('nsfw', False)
            political = flags.get('political', False)
            sexist = flags.get('sexist', False)

            try:
                connection.execute(text('''
                    INSERT INTO jokes (category, type, joke, setup, delivery, nsfw, political, sexist, safe, lang)
                    VALUES (:category, :type, :joke, :setup, :delivery, :nsfw, :political, :sexist, :safe, :lang)
                '''), {
                    'category': joke.get('category', 'Unknown'),
                    'type': joke_type,
                    'joke': joke_text,
                    'setup': setup,
                    'delivery': delivery,
                    'nsfw': nsfw,
                    'political': political,
                    'sexist': sexist,
                    'safe': joke.get('safe', True),
                    'lang': joke.get('lang', 'en')
                })
            except Exception as e:
                print(f"Error inserting joke: {e}")

    engine.dispose()

def fetch_and_store_jokes():
    jokes_collected = 0
    while jokes_collected < 10:
        try:
            response = requests.get(
                'https://v2.jokeapi.dev/joke/Any'
            )
            if response.status_code == 200:
                joke = response.json()
                print(joke)
                insert_jokes(joke)
                jokes_collected += 1
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error fetching joke: {e}")
    return {"status": "Success", "message": f"{jokes_collected} jokes stored in the database."}