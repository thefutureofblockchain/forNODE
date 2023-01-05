from numb3rs import validate
def test_range():
    assert validate("265.3.3.2") == False
    assert validate("255.3.3.2") == True
def test_validity():
    assert validate("@22.ss.abc.s") == False
    assert validate("12.2.2") == False
    assert validate("Abs")== False