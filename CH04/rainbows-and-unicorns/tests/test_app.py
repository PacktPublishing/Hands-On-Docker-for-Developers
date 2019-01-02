import os
import pytest
import rainuni
from unittest.mock import patch

@pytest.fixture
def client():
    client = rainuni.app.test_client()
    yield client

def test_get_rainbow(client):
    """When it returns a Rainbow."""
    with patch.object(rainuni, 'give_me_a_rainbow_unicorn', return_value='Rainbow'):
        rv = client.get('/')
        assert b'Just a Rainbow. Try Again' in rv.data

def test_get_unicorn(client):
    """When it returns a Unicorn."""
    with patch.object(rainuni, 'give_me_a_rainbow_unicorn', return_value='Unicorn'):
        rv = client.get('/')
        assert b'Just a Unicorn. Try Again' in rv.data

def test_get_rainbowunicorn(client):
    """When it returns a Rainbow Unicorn."""
    with patch.object(rainuni, 'give_me_a_rainbow_unicorn', return_value='Rainbow Unicorn'):
        rv = client.get('/')
        assert b'A Rainbow Unicorn! You won in 3 retries!' in rv.data