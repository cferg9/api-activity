import pytest
from app import app

@pytest.fixture
def client():
        with app.test_client() as client:
                yield client
def test_hello(client):
        response = client.get('/')
        assert response.status_code == 200
        assert response.json == {"message": "Hello World:"}
def test_square(client):
    response = client.get('/square/3')

    assert response.status_code == 200

    assert response.json == {
        "Shape": "Square",
        "Area": 9
    }


def test_echo(client):
    response = client.get('/echo?arg1=hello&arg2=world')

    assert response.status_code == 200

    assert response.json == {
        "arg1": "hello",
        "arg2": "world"
    }