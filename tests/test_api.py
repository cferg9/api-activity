import base64
import uuid
import pytest

from api_activity.app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.testing = True
    with app.test_client() as client:
        yield client
def test_hello(client):
        response = client.get('/')
        assert response.status_code == 200
        assert response.json == {"message": "Hello World:"}
def test_square(client):
    response = client.get('/square/3')
    assert response.status_code == 200
    assert response.json == {"Shape": "Square", "Area": 9}
    assert response.json == {
            "Shape": "Square",
            "Area": 9
        }

def test_profile_requires_auth(client):
    response = client.get('/profile')
    assert response.status_code == 401

def test_profile_with_valid_auth(client):
    client.put(
        '/register',
        json={"username": "testuser", "password": "testpass123"}
    )
    response = client.get(
    '/profile',
    auth=("testuser", "testpass123")
    )
    assert response.status_code == 200
    assert "testuser" in response.json["message"]   

def test_activity_without_auth(client):
    response = client.get('/activity')
    assert response.status_code == 401


def test_activity_with_valid_auth(client):
    client.put(
        '/register',
        json={"username": "activityuser", "password": "testpass123"}
    )

    response = client.get(
        '/activity',
        auth=("activityuser", "testpass123")
    )

    assert response.status_code == 200
    
def test_echo(client):
    response = client.get('/echo?arg1=hello&arg2=world')

    assert response.status_code == 200

    assert response.json == {
        "arg1": "hello",
        "arg2": "world"
   } 
