from twttr import shorten
import pytest
#Then, in a file called test_twttr.py, implement one or more functions
# that collectively test your implementation of shorten thoroughly, each
# of whose names should begin with test_ so that you can execute
# your tests with pytest test_twttr.py
#Take care to return, not print, a str in shorten. Only main should call print.


def test_return_constants():
    test = "Hey Noel How are you"
    result = shorten(test)
    assert result == "Hy Nl Hw r y"
def test_novowels():
    test = "whr y gng?"
    result = shorten(test)
    assert result == "whr y gng?"
def test_allcaps():
    test = "MY NAME IS YOLANDA"
    result = shorten(test)
    assert result == "MY NM S YLND"
def test_alllower():
    test = "what are you doing"
    result = shorten(test)
    assert result == "wht r y dng"
def test_allnumbers():
    test = "h8a41"
    result = shorten(test)
    assert result == "h841"

