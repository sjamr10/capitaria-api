from fastapi import status
from starlette.testclient import TestClient


def test_create(client: TestClient):
    request_payload = {"name": "programación 1"}
    response = client.post(
        "/courses",
        json=request_payload,
    )

    assert response.status_code == status.HTTP_201_CREATED, response.text
    response_data = response.json()
    assert "id" in response_data
    assert response_data["name"] == request_payload["name"]


def test_create_invalid_json(client: TestClient):
    response = client.post("/courses", json={"name": "1"})
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY, response.text


def test_get_one(client: TestClient):
    create_payload = {"name": "programación 1"}
    response = client.post(
        "/courses",
        json=create_payload,
    )
    create_response_data = response.json()

    response = client.get("/courses/" + str(create_response_data["id"]))
    response_data = response.json()

    assert response.status_code == status.HTTP_200_OK, response.text
    assert response_data["id"] == create_response_data["id"]
    assert response_data["name"] == create_payload["name"]


def test_update(client: TestClient):
    create_payload = {"name": "programación 1"}
    response = client.post(
        "/courses",
        json=create_payload,
    )
    response_data = response.json()

    request_payload = {
        "id": response_data["id"],
        "name": "programación 2",
    }
    response = client.put("/courses/" + str(response_data["id"]), json=request_payload)
    response_data = response.json()

    assert response.status_code == status.HTTP_200_OK, response.text
    assert response_data["id"] == request_payload["id"]
    assert response_data["name"] == request_payload["name"]


def test_delete(client: TestClient):
    create_payload = {"name": "programación 1"}
    response = client.post(
        "/courses",
        json=create_payload,
    )
    response_data = response.json()

    response = client.delete("/courses/" + str(response_data["id"]))

    assert response.status_code == status.HTTP_204_NO_CONTENT, response.text
