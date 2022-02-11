from fastapi import status
from starlette.testclient import TestClient


def test_create(client: TestClient):
    request_payload = {"student_id": 1, "course_id": 1}
    response = client.post(
        "/enrollments",
        json=request_payload,
    )

    assert response.status_code == status.HTTP_201_CREATED, response.text
    response_data = response.json()
    assert "id" in response_data
    assert response_data["student_id"] == request_payload["student_id"]
    assert response_data["course_id"] == request_payload["course_id"]


def test_create_invalid_json(client: TestClient):
    response = client.post("/enrollments", json={"student_id": 1})
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY, response.text


def test_get_one(client: TestClient):
    create_payload = {"student_id": 1, "course_id": 1}
    response = client.post(
        "/enrollments",
        json=create_payload,
    )
    create_response_data = response.json()

    response = client.get("/enrollments/" + str(create_response_data["id"]))
    response_data = response.json()

    assert response.status_code == status.HTTP_200_OK, response.text
    assert response_data["id"] == create_response_data["id"]
    assert response_data["student_id"] == create_payload["student_id"]
    assert response_data["course_id"] == create_payload["course_id"]


def test_update(client: TestClient):
    create_payload = {"student_id": 1, "course_id": 1}
    response = client.post(
        "/enrollments",
        json=create_payload,
    )
    response_data = response.json()

    request_payload = {"id": response_data["id"], "student_id": 1, "course_id": 2}
    response = client.put(
        "/enrollments/" + str(response_data["id"]), json=request_payload
    )
    response_data = response.json()

    assert response.status_code == status.HTTP_200_OK, response.text
    assert response_data["id"] == request_payload["id"]
    assert response_data["student_id"] == request_payload["student_id"]
    assert response_data["course_id"] == request_payload["course_id"]


def test_delete(client: TestClient):
    create_payload = {"student_id": 3, "course_id": 3}
    response = client.post(
        "/enrollments",
        json=create_payload,
    )
    response_data = response.json()

    response = client.delete("/enrollments/" + str(response_data["id"]))

    assert response.status_code == status.HTTP_204_NO_CONTENT, response.text
