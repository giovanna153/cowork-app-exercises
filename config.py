import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DATABASE_PATH = BASE_DIR / "instance" / "coworking.sqlite3"


class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "chave-desenvolvimento-coworking")
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{DATABASE_PATH}"
