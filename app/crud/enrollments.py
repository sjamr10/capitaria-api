from typing import List, Optional

from sqlalchemy.orm import Query

from app.lib import db
from app.models import Enrollment
from app.schemas import EnrollmentCreate


def create(enrollment: EnrollmentCreate) -> Enrollment:
    session = db.get_session()
    db_enrollment = Enrollment(**enrollment.dict())
    session.add(db_enrollment)
    session.commit()
    session.refresh(db_enrollment)
    return db_enrollment


def get(sort: str) -> List[Enrollment]:
    session = db.get_session()
    query = session.query(Enrollment)
    return _sort(query, sort)


def get_one(id: int) -> Optional[Enrollment]:
    session = db.get_session()
    return session.query(Enrollment).filter(Enrollment.id == id).first()


def update(id: int, enrollment: EnrollmentCreate) -> Enrollment:
    session = db.get_session()
    db_enrollment = session.query(Enrollment).filter(Enrollment.id == id).first()
    db_enrollment.student_id = enrollment.student_id
    db_enrollment.course_id = enrollment.course_id
    session.commit()
    session.refresh(db_enrollment)
    return db_enrollment


def delete(id: int) -> None:
    session = db.get_session()
    db_enrollment = session.query(Enrollment).filter(Enrollment.id == id).first()
    session.delete(db_enrollment)
    session.commit()


def _sort(query: Query, sort: str) -> List[Enrollment]:
    order_by = sort_params[sort]
    return query.order_by(*(order_by,)).all()


sort_params = {
    "course_id:asc": Enrollment.course_id.asc(),
    "course_id:desc": Enrollment.course_id.desc(),
    "student_id:asc": Enrollment.student_id.asc(),
    "student_id:desc": Enrollment.student_id.desc(),
}
