from app.database import Session


def get_session() -> Session:
    session = Session()
    try:
        return session
    finally:
        session.close()
