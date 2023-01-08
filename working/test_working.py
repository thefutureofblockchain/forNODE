from working import convert
import pytest
def test_1():
    with pytest.raises(ValueError):
        convert("abc")
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
def test_2():
    assert convert("10 PM to 8 AM") == "22:00 to 08:00"
    assert convert("10:30 PM to 8:50 AM") == "22:30 to 08:50"

def test_3():
        with pytest.raises(ValueError):
            convert("13:00 to 15:00")
        with pytest.raises(ValueError):
            convert("1:00 AM through 1:00 PM")y
        with pytest.raises(ValueError):
            convert("1:00 AM through 1:00 PM")
        with pytest.raises(ValueError):
            convert("1:00 AM through 100:00 PM")
        with pytest.raises(ValueError):
            convert("28:00 AM through 1:00 PM")
        with pytest.raises(ValueError):
            convert("9:60 PM to 2:15 AM")
def test_4():
    pass