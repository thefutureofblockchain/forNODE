from working import convert
import pytest
def test_1():
    with pytest.raises(ValueError):
        convert("cat")
    #assert convert("9 AM to 5 PM") == "09:00 to 17:00"
def test_2():
    pass
def test_3():
    pass
def test_4():
    pass