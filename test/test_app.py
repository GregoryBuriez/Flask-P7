import pytest
from flask import Flask
from flask.testing import FlaskClient
from your_flask_app import app

@pytest.fixture
def client() -> FlaskClient:
    app.testing = True
    with app.test_client() as client:
        yield client

def test_prediction(client: FlaskClient):
    # Données de test pour l'identifiant du client
    client_id = 12345

    # Envoyer une requête POST à l'API
    response = client.post('/api/predict', data={'client_id': client_id})

    # Vérifier le code de statut de la réponse
    assert response.status_code == 200

    # Vérifier le type de contenu de la réponse
    assert response.headers['Content-Type'] == 'application/json'

    # Analyser la réponse JSON
    result = response.get_json()

    # Vérifier si la prédiction est présente dans la réponse
    assert 'prediction' in result

def test_invalid_client_id(client: FlaskClient):
    # Données de test pour un identifiant de client invalide
    invalid_client_id = 99999

    # Envoyer une requête POST à l'API avec un identifiant invalide
    response = client.post('/api/predict', data={'client_id': invalid_client_id})

    # Vérifier le code de statut de la réponse
    assert response.status_code == 200

    # Vérifier le type de contenu de la réponse
    assert response.headers['Content-Type'] == 'application/json'

    # Analyser la réponse JSON
    result = response.get_json()

    # Vérifier si l'erreur est présente dans la réponse
    assert 'error' in result
    assert result['error'] == 'Identifiant non reconnu'
    assert 'prediction' in result
    assert result['prediction'] is None

def test_invalid_http_method(client: FlaskClient):
    # Envoyer une requête GET à l'API au lieu d'une requête POST
    response = client.get('/api/predict')

    # Vérifier le code de statut de la réponse
    assert response.status_code == 200

    # Vérifier le type de contenu de la réponse
    assert response.headers['Content-Type'] == 'application/json'

    # Analyser la réponse JSON
    result = response.get_json()

    # Vérifier si l'erreur est présente dans la réponse
    assert 'error' in result
    assert result['error'] == 'Méthode non autorisée. Veuillez utiliser la méthode POST pour effectuer une prédiction.'