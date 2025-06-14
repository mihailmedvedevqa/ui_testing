import os
from dotenv import load_dotenv

load_dotenv()


class Data:
    """Loads environment variables from .env file."""

    LOGIN = os.getenv("LOGIN")
    PASSWORD = os.getenv("PASSWORD")
