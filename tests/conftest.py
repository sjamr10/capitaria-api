import pytest
from starlette.testclient import TestClient

from app.main import app


@pytest.fixture(scope="module", autouse=True)
def client() -> TestClient:
    return TestClient(app)
