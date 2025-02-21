import os
from dotenv import load_dotenv

load_dotenv()

def get_db_url():
    user = os.getenv("DB_USER")
    password = os.getenv("DB_PASSWORD")
    host = os.getenv("DB_HOST")
    port = os.getenv("DB_PORT")
    db_name = os.getenv("JOKES_DB_NAME")
    return f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{db_name}"