import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_home(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"Welcome to the Calculator API!" in response.data

def test_add(client):
    response = client.get("/add?a=5&b=3")
    assert response.status_code == 200
    assert response.json["result"] == 8.0

def test_subtract(client):
    response = client.get("/subtract?a=10&b=4")
    assert response.status_code == 200
    assert response.json["result"] == 6.0

def test_multiply(client):
    response = client.get("/multiply?a=7&b=6")
    assert response.status_code == 200
    assert response.json["result"] == 42.0

def test_divide_by_zero(client):
    response = client.get("/divide?a=8&b=0")
    assert response.status_code == 400
    assert "Cannot divide by zero" in response.json["error"]

def test_divide_by_zero(client):
    response = client.get("/divide?a=8&b=0")
    assert response.status_code == 400
    assert "Cannot divide by zero" in response.json["error"]
