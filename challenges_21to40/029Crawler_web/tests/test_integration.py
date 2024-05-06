import pytest
from flask import json

from views.index import app


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_index(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Bem vindo ao Web Crawler App!' in response.data

