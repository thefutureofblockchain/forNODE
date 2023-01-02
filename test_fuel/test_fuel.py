from fuel import gauge
from fuel import convert
import pytest
def test_gauge():
    assert gauge(33) == "33%"
    assert gauge(35) == "35%"
    assert gauge(100) == "F"
    assert gauge(0) == "E"
    assert gauge(99) == "F"
    assert gauge(1) == "E"
def test_error():
    with pytest.raises(ZeroDivisionError):
        convert("5/0")
    with pytest.raises(ValueError):
        convert("b/1")

def test_convert():
    assert convert("1/4") == 25
    assert convert("2/8") == 25
    assert convert("3/4") == 75