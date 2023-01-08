from um import count
def test_1():
    assert count("yummy") == 0
def test_2():
    assert count(",um, im dumb") == 1
def test_3():
    assert count("UM SO") == 1