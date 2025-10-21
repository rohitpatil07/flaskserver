import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client
    
def test_dbstatus(client):
    res = client.get("/db/").get_json()
    assert res['status'] == 'success'
    assert res["code"] == 200

def test_dbdata(client):
    res = client.get("/db/data").get_json()
    assert res['status'] == 'success'
    assert res["code"] == 200

def test_dbusers(client):
    res = client.get("/db/users").get_json()
    users = res.get("users", [])
    assert isinstance(users, list), "users should be a list"

    #Validate users
    for user in users:
        assert isinstance(user, dict), "each user should be a dictionary"
        assert 'id' in user and isinstance(user['id'], int), f"User ID should be int, got {type(user.get('id'))}"
        assert 'name' in user and isinstance(user['name'], str), f"User Name should be string, got {type(user.get('name'))}"

    assert res['status'] == 'success'
    assert res["code"] == 200
