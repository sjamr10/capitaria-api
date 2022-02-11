from sqlalchemy import Column, Integer, String

from app.database import Base


class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
