import pytest
from project import get_wrong,more,pdf_ize
def test_get_wrong():
    assert get_wrong() == "The input you entered was incorrect"
def test_more():
    assert more(10,1,1,1) == 10
def test_pdf_ize():
    assert pdf_ize(format = "British Parliamentary") == "British Parliamentary"
