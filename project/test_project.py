import pytest
from project import ques1
def test_ques1(monkeypatch):
    ques1()
    monkeypatch.setattr('builtins.input',lambda _: "y")
    assert ques1() == 1
def test_ques10():
    pass
def test_ques2():
    pass
