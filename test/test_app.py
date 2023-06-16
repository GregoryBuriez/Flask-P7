import pytest
from flask import Flask
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_route(client):
    response = client.get('/')
    assert response.status_code == 200
    assert "modèle".encode('utf-8') in response.data

def test_predict_route_with_valid_id(client):
    response = client.post('/api/predict', data={'client_id': 123})
    assert response.status_code == 200
    data = response.get_json()
    assert 'prediction' in data

def test_predict_route_with_invalid_id(client):
    response = client.post('/api/predict', data={'client_id': 999})
    assert response.status_code == 200
    data = response.get_json()
    assert 'error' in data
    assert data['prediction'] is None

if __name__ == '__main__':
    pytest.main()
