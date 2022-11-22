from calculator import square


def test_positive():
    assert square(2) == 4


def test_negative():
    assert square(-2) == 4


def test_zero():
    assert square(0) == 0
