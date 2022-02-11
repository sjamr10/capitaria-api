from typing import List, Optional

from sqlalchemy.orm import Query

from app.lib import db
from app.models import Student
from app.schemas import StudentCreate


def create(student: StudentCreate) -> Student:
    session = db.get_session()
    db_student = Student(**student.dict())
    session.add(db_student)
    session.commit()
    session.refresh(db_student)
    return db_student


def get(sort: str, name: Optional[str]) -> List[Student]:
    session = db.get_session()
    query = session.query(Student)
    query = _filter(query, name)
    return _sort(query, sort)


def get_one(id: int) -> Optional[Student]:
    session = db.get_session()
    return session.query(Student).filter(Student.id == id).first()


def update(id: int, student: StudentCreate) -> Student:
    session = db.get_session()
    db_student = session.query(Student).filter(Student.id == id).first()
    db_student.name = student.name
    session.commit()
    session.refresh(db_student)
    return db_student


def delete(id: int) -> None:
    session = db.get_session()
    db_student = session.query(Student).filter(Student.id == id).first()
    session.delete(db_student)
    session.commit()


def _filter(query: Query, name: Optional[str]) -> Query:
    if name:
        query = query.filter(Student.name == name)
    return query


def _sort(query: Query, sort: str) -> List[Student]:
    order_by = sort_params[sort]
    return query.order_by(*(order_by,)).all()


sort_params = {
    "name:asc": Student.name.asc(),
    "name:desc": Student.name.desc(),
}
