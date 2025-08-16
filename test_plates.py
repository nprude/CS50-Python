from plates import is_valid


def test_numberlen():
    test = "1"
    test2 = "QFDANKO"
    test3 = "JK"
    test4 = "GHJ"
    test5 = "ABCD"
    test6 = "RTYUI"
    test7 = "ABCDEF"
    test8 = "H"
    assert is_valid (test) == False
    assert is_valid (test2) == False
    assert is_valid (test3) == True
    assert is_valid (test4) == True
    assert is_valid (test5) == True
    assert is_valid (test6) == True
    assert is_valid (test7) == True
    assert is_valid (test8) == False
def test_plates_two():
    test = "AZ"
    test2 = "2G"
    test3 = "B5"
    assert is_valid(test) == True
    assert is_valid(test2) == False
    assert is_valid(test3) == False
def test_plates_three():
    test = "ABC"
    test2 = "AB0"
    assert is_valid(test) == True
    assert is_valid(test2) == False
def test_plates_four():
    test = "MNPY"
    test2 = "MNL0"
    test3 = "AB0D"
    test4 = "AB5T"
    test5 = "ABT5"
    test6 = "AB76"
    assert is_valid(test) == True
    assert is_valid(test2) == False
    assert is_valid(test3) == False
    assert is_valid(test4) == False
    assert is_valid(test5) == True
    assert is_valid(test6) == True
def test_punctuation():
    test = "AB!"
    assert is_valid(test) == False
def test_plates_five():
    test = "ABCDE"
    assert is_valid(test) == True
def test_plates_six():
    test = "ABCDEF"
    test2 = "ABC11K"
    assert is_valid(test) == True
    assert is_valid(test2) == False






