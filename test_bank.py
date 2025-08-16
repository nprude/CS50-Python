import pytest
from bank import value

def test_hello():
    a = "Hello"
    assert value(a) == 0

def test_not_startswith_h():
    a = "Whats up"
    assert value(a) == 100

def test_startswith_h():
    a = "Hola How are ya"
    assert value(a) == 20

