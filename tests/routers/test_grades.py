from fastapi import status
from starlette.testclient import TestClient


def test_create(client: TestClient):
    request_payload = {"value": 1, "student_id": 1, "test_id": 1}
    response = client.post(
        "/grades",
        json=request_payload,
    )

    assert response.status_code == status.HTTP_201_CREATED, response.text
    response_data = response.json()
    assert "id" in response_data
    assert response_data["value"] == request_payload["value"]
    assert response_data["student_id"] == request_payload["student_id"]
    assert response_data["test_id"] == request_payload["test_id"]


def test_create_invalid_json(client: TestClient):
    response = client.post("/grades", json={"value": "1"})
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY, response.text

    response = client.post("/grades", json={"value": 8, "student_id": 1, "test_id": 1})
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY, response.text


def test_get_one(client: TestClient):
    create_payload = {"value": 1, "student_id": 1, "test_id": 1}
    response = client.post(
        "/grades",
        json=create_payload,
    )
    create_response_data = response.json()

    response = client.get("/grades/" + str(create_response_data["id"]))
    response_data = response.json()

    assert response.status_code == status.HTTP_200_OK, response.text
    assert response_data["id"] == create_response_data["id"]
    assert response_data["value"] == create_payload["value"]
    assert response_data["student_id"] == create_payload["student_id"]
    assert response_data["test_id"] == create_payload["test_id"]


def test_update(client: TestClient):
    create_payload = {"value": 1, "student_id": 1, "test_id": 1}
    response = client.post(
        "/grades",
        json=create_payload,
    )
    response_data = response.json()

    request_payload = {
        "id": response_data["id"],
        "value": 4,
        "student_id": 1,
        "test_id": 1,
    }
    response = client.put("/grades/" + str(response_data["id"]), json=request_payload)
    response_data = response.json()

    assert response.status_code == status.HTTP_200_OK, response.text
    assert response_data["id"] == request_payload["id"]
    assert response_data["value"] == request_payload["value"]
    assert response_data["student_id"] == request_payload["student_id"]
    assert response_data["test_id"] == request_payload["test_id"]


def test_delete(client: TestClient):
    create_payload = {"value": 1, "student_id": 1, "test_id": 1}
    response = client.post(
        "/grades",
        json=create_payload,
    )
    response_data = response.json()

    response = client.delete("/grades/" + str(response_data["id"]))

    assert response.status_code == status.HTTP_204_NO_CONTENT, response.text
