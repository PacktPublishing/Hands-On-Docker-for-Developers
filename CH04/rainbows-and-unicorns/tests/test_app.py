import datetime
import os
import pytest
import rainuni
from unittest.mock import patch

import locale

locale.setlocale(locale.LC_ALL, '')

@pytest.fixture
def client():
    client = rainuni.app.test_client()
    yield client

def test_get_rainbow(client):
    """When it returns a Rainbow."""
    with patch.object(rainuni, 'give_me_a_rainbow_unicorn', return_value='🌈'):
        rv = client.get('/')
        assert b'Just a Rainbow \xf0\x9f\x8c\x88. Try Again' in rv.data

def test_get_unicorn(client):
    """When it returns a Unicorn."""
    with patch.object(rainuni, 'give_me_a_rainbow_unicorn', return_value='🦄'):
        rv = client.get('/')
        assert b'Just a Unicorn \xf0\x9f\xa6\x84. Try Again' in rv.data

def test_get_rainbowunicorn(client):
    """When it returns a Rainbow Unicorn."""
    with patch.object(rainuni, 'give_me_a_rainbow_unicorn', return_value='🌈🦄'):
        rv = client.get('/')
        assert b'A Rainbow Unicorn \xf0\x9f\x8c\x88\xf0\x9f\xa6\x84! You won in 3 retries!' in rv.data

def test_get_rainbowunicorn_time(client):
    """It returns a Rainbow Unicorn in less than 2 seconds."""
    d = datetime.datetime.now().strftime('%X')
    print(d)
    begin = d[d.index('分')+1:d.index('秒')]
    client.get('/')
    d = datetime.datetime.now().strftime('%X')
    print(d)
    end = d[d.index('分')+1:d.index('秒')]
    assert int(end) - int(begin) < 2
