from fastapi import FastAPI
from fastapi.middleware.gzip import GZipMiddleware

from app.database import engine
from app.models import Base
from app.routers import courses, enrollments, grades, health, students, tests

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(GZipMiddleware)

app.include_router(health.router, tags=["health"])
app.include_router(students.router, prefix="/students", tags=["students"])
app.include_router(courses.router, prefix="/courses", tags=["courses"])
app.include_router(enrollments.router, prefix="/enrollments", tags=["enrollments"])
app.include_router(tests.router, prefix="/tests", tags=["tests"])
app.include_router(grades.router, prefix="/grades", tags=["grades"])
