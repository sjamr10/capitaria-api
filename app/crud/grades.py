from typing import List, Optional

from sqlalchemy.orm import Query

from app.lib import db
from app.models import Grade
from app.schemas import GradeCreate


def create(grade: GradeCreate) -> Grade:
    session = db.get_session()
    db_grade = Grade(**grade.dict())
    session.add(db_grade)
    session.commit()
    session.refresh(db_grade)
    return db_grade


def get(sort: str, student_id: Optional[int]) -> List[Grade]:
    session = db.get_session()
    query = session.query(Grade)
    query = _filter(query, student_id)
    return _sort(query, sort)


def get_one(id: int) -> Optional[Grade]:
    session = db.get_session()
    return session.query(Grade).filter(Grade.id == id).first()


def update(id: int, grade: GradeCreate) -> Grade:
    session = db.get_session()
    db_grade = session.query(Grade).filter(Grade.id == id).first()
    db_grade.student_id = grade.student_id
    db_grade.test_id = grade.test_id
    db_grade.value = grade.value
    session.commit()
    session.refresh(db_grade)
    return db_grade


def delete(id: int) -> None:
    session = db.get_session()
    db_grade = session.query(Grade).filter(Grade.id == id).first()
    session.delete(db_grade)
    session.commit()


def _filter(query: Query, student_id: Optional[int]) -> Query:
    if student_id:
        query = query.filter(Grade.student_id == student_id)
    return query


def _sort(query: Query, sort: str) -> List[Grade]:
    order_by = sort_params[sort]
    return query.order_by(*(order_by,)).all()


sort_params = {
    "student_id:asc": Grade.student_id.asc(),
    "student_id:desc": Grade.student_id.desc(),
}
