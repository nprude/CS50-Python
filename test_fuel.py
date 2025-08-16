import pytest
from fuel import gauge, convert

def test_gauge():
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(100) == "F"
    assert gauge(75) == "75%"
    assert gauge(50) == "50%"

def test_convert_valid():
    assert convert("0/3") == 0
    assert convert("5/5") == 100
    assert convert("2/3") == 67

def test_convert_value_error():
    with pytest.raises(ValueError):
        convert("x/y")
    with pytest.raises(ValueError):
        convert("10/y")
    with pytest.raises(ValueError):
        convert("2/1")
    with pytest.raises(ValueError):
        convert("-2/3")
    with pytest.raises(ValueError):
        convert("2/-3")


def test_convert_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")

