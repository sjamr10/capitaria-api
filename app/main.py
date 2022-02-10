from fastapi import FastAPI
from fastapi.middleware.gzip import GZipMiddleware

from app.database import engine
from app.models import Base
from app.routers import health

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(GZipMiddleware)

app.include_router(health.router, tags=["health"])
