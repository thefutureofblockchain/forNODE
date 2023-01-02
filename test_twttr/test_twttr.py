from twttr import shorten
def test_def():
    assert shorten("ab") == "b"
def test_cap():
    assert shorten("Ab") == "b"
def test_num():
    assert shorten("1ab") == "1b"
def test_punct():
    assert shorten("..a..b") == "....b"