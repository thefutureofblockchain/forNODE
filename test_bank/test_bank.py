from bank import value
def test_values():
    assert value("What's up") == 100
    assert value("Hello") == 0
    assert value("hello") == 0
    assert value("heyyy") == 20