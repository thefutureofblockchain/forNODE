import pytest
from project import ques1,more,pdf_ize
def test_ques1(monkeypatch):
    ques1()
    monkeypatch.setattr('builtins.input',lambda _: "y")
    assert ques1() == 1
def test_more():
    assert more(10,1,1,1) == 10
def test_pdf_ize():
    assert pdf_ize(format = "British Parliamentary") == "British Parliamentary"
