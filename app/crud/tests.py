from typing import List, Optional

from sqlalchemy.orm import Query

from app.lib import db
from app.models import Test
from app.schemas import TestCreate


def create(test: TestCreate) -> Test:
    session = db.get_session()
    db_test = Test(**test.dict())
    session.add(db_test)
    session.commit()
    session.refresh(db_test)
    return db_test


def get(sort: str, name: Optional[str]) -> List[Test]:
    session = db.get_session()
    query = session.query(Test)
    query = _filter(query, name)
    return _sort(query, sort)


def get_one(id: int) -> Optional[Test]:
    session = db.get_session()
    return session.query(Test).filter(Test.id == id).first()


def update(id: int, test: TestCreate) -> Test:
    session = db.get_session()
    db_test = session.query(Test).filter(Test.id == id).first()
    db_test.name = test.name
    db_test.course_id = test.course_id
    session.commit()
    session.refresh(db_test)
    return db_test


def delete(id: int) -> None:
    session = db.get_session()
    db_test = session.query(Test).filter(Test.id == id).first()
    session.delete(db_test)
    session.commit()


def _filter(query: Query, name: Optional[str]) -> Query:
    if name:
        query = query.filter(Test.name == name)
    return query


def _sort(query: Query, sort: str) -> List[Test]:
    order_by = sort_params[sort]
    return query.order_by(*(order_by,)).all()


sort_params = {
    "name:asc": Test.name.asc(),
    "name:desc": Test.name.desc(),
}
