from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from app.config import POSTGRES_URL

engine = create_engine(
    POSTGRES_URL,
    connect_args={},
    pool_size=70,
    max_overflow=30,
    pool_timeout=15,
)
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
