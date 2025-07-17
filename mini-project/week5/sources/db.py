import psycopg2
import os 
from dotenv import load_dotenv

load_dotenv()

def get_connection():
    return psycopg2.connect(
        host = os.environ.get("POSTGRES_HOST"),
        database = os.environ.get("POSTGRES_DB"),
        user = os.environ.get("POSTGRES_USER"),
        password = os.environ.get("POSTGRES_PASSWORD"),
        port = os.environ.get("PORT")
    )