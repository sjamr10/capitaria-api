from typing import List, Optional

from sqlalchemy.orm import Query

from app.lib import db
from app.models import Course
from app.schemas import CourseCreate


def create(course: CourseCreate) -> Course:
    session = db.get_session()
    db_course = Course(**course.dict())
    session.add(db_course)
    session.commit()
    session.refresh(db_course)
    return db_course


def get(sort: str, name: Optional[str]) -> List[Course]:
    session = db.get_session()
    query = session.query(Course)
    query = _filter(query, name)
    return _sort(query, sort)


def get_one(id: int) -> Optional[Course]:
    session = db.get_session()
    return session.query(Course).filter(Course.id == id).first()


def update(id: int, course: CourseCreate) -> Course:
    session = db.get_session()
    db_course = session.query(Course).filter(Course.id == id).first()
    db_course.name = course.name
    db_course.teacher_id = course.teacher_id
    session.commit()
    session.refresh(db_course)
    return db_course


def delete(id: int) -> None:
    session = db.get_session()
    db_course = session.query(Course).filter(Course.id == id).first()
    session.delete(db_course)
    session.commit()


def _filter(query: Query, name: Optional[str]) -> Query:
    if name:
        query = query.filter(Course.name == name)
    return query


def _sort(query: Query, sort: str) -> List[Course]:
    order_by = sort_params[sort]
    return query.order_by(*(order_by,)).all()


sort_params = {
    "name:asc": Course.name.asc(),
    "name:desc": Course.name.desc(),
}
