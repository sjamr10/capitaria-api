from fastapi import status
from starlette.testclient import TestClient


def test_health_check(client: TestClient):
    response = client.get("/")

    assert response.status_code == status.HTTP_200_OK, response.text
    assert response.json() == {}
