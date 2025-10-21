import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_hello(client):
    response = client.get('/')
    json_data = response.get_json()
    assert response.status_code == 200
    assert json_data['message'] == 'Hello World'
    assert json_data['status'] == 'success'

def test_health(client):
    response = client.get('/health')
    assert response.status_code == 200
    assert response.get_json()['message'] == 'Healthy'

def test_data(client):
    response = client.get('/data')
    assert response.status_code == 200
    assert response.get_json()['status'] == 'success'

def test_unauthorized(client):
    response = client.get('/unauthorized')
    assert response.status_code == 401  # NOTE: your route returns 200 with a 401 code in JSON
    assert response.get_json()['code'] == 401

def test_fail(client):
    response = client.get('/fail')
    assert response.status_code == 500  # Same here — 200 status but JSON says 500
    assert response.get_json()['code'] == 500