from fastapi.testclient import TestClient
from main import app
from uuid import UUID, uuid4
from models import StudentModel

client = TestClient(app)


def test_create_student():
    student_data = {
        "age": 20,
        "name": "John",
        "surname": "Doe",
        "group": "A123",
        "course": 2
    }
    response = client.post("/students/", json=student_data)
    assert response.status_code == 200
    created_student = StudentModel(**response.json())
    assert created_student.age == student_data["age"]
    assert created_student.name == student_data["name"]
    assert created_student.surname == student_data["surname"]
    assert created_student.group == student_data["group"]
    assert created_student.course == student_data["course"]
    assert isinstance(created_student.id, UUID)


def test_read_student():
    student_data = {
        "age": 22,
        "name": "Alice",
        "surname": "Smith",
        "group": "B456",
        "course": 3
    }
    response = client.post("/students/", json=student_data)
    created_student = StudentModel(**response.json())

    response_read = client.get(f"/students/{created_student.id}")
    assert response_read.status_code == 200
    assert created_student.age == student_data["age"]
    assert created_student.name == student_data["name"]
    assert created_student.surname == student_data["surname"]
    assert created_student.group == student_data["group"]
    assert created_student.course == student_data["course"]


def test_update_student():
    student_data = {
        "age": 25,
        "name": "Bob",
        "surname": "Johnson",
        "group": "C789",
        "course": 4
    }
    response = client.post("/students/", json=student_data)
    created_student = StudentModel(**response.json())

    updated_student_data = {
        "age": 26,
        "name": "Updated Name",
        "surname": "Updated Surname",
        "group": "Updated Group",
        "course": 5
    }

    response_update = client.put(f"/students/{created_student.id}", json=updated_student_data)
    assert response_update.status_code == 200
    updated_student = StudentModel(**response_update.json())
    assert updated_student.id == created_student.id
    assert updated_student.age == updated_student_data["age"]
    assert updated_student.name == updated_student_data["name"]
    assert updated_student.surname == updated_student_data["surname"]
    assert updated_student.group == updated_student_data["group"]
    assert updated_student.course == updated_student_data["course"]


def test_delete_student():
    student_data = {
        "age": 30,
        "name": "Eve",
        "surname": "Williams",
        "group": "D012",
        "course": 6
    }
    response = client.post("/students/", json=student_data)
    created_student = StudentModel(**response.json())

    response_delete = client.delete(f"/students/{created_student.id}")
    assert response_delete.status_code == 200
    deleted_student = StudentModel(**response_delete.json())
    assert deleted_student.id == created_student.id

    response_read_deleted = client.get(f"/students/{created_student.id}")
    assert response_read_deleted.status_code == 404


if __name__ == "__main__":
    import pytest

    pytest.main(["-v", __file__])
