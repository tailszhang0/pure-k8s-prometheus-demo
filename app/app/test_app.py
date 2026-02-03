import app
import pytest

def test_hello_endpoint():
    client = app.app.test_client()
    response = client.get('/')
    assert response.status_code == 200
    assert b'Hello pure-k8s-prometheus-demo World!' in response.data

def test_health_endpoint():
    client = app.app.test_client()
    response = client.get('/health')
    assert response.status_code == 200
    assert response.data == b'pure-k8s-prometheus-demo OK'