import pytest
from backendApp.app import create_app
from backendApp.extensions import db
from backendApp.models import Note


@pytest.fixture
def client():
    app = create_app()
    app.config.update(
        {"TESTING": True,
         "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:"}
    )

    with app.app_context():
        db.create_all()
        yield app.test_client()
        db.session.remove()
        db.drop_all()


def test_add_note(client):
    res = client.post(
        "/api/notes/", json={"title": "Test", "content": "Hello"})
    assert res.status_code == 201
    data = res.get_json()
    assert data["title"] == "Test"
    assert data["content"] == "Hello"


def test_list_notes(client):
    client.post("/api/notes/", json={"title": "Note 1", "content": "content"})
    res = client.get("/api/notes/")
    assert res.status_code == 200

    data = res.get_json()
    assert len(data) == 1
    assert data[0]["title"] == "Note 1"
    assert data[0]["content"] == "content"


def test_delete_note(client):
    res = client.post(
        "/api/notes/", json={"title": "To Delete", "content": "Delete it"})
    id = res.get_json()["id"]

    delete = client.delete(f"/api/notes/{id}")
    assert delete.status_code == 200

    get_res = client.get("/api/notes/")
    assert len(get_res.get_json()) == 0
