from os import environ

POSTGRES_HOST = environ["POSTGRES_HOST"]
POSTGRES_DB = environ["POSTGRES_DB"]
POSTGRES_USER = environ["POSTGRES_USER"]
POSTGRES_PASSWORD = environ["POSTGRES_PASSWORD"]
POSTGRES_URL = (
    f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}/{POSTGRES_DB}"
)
