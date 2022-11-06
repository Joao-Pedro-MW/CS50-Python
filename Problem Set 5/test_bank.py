from bank import value
def test_value():
    assert value("Hi") == 20
    assert value("Sup!") == 100
    assert value("Hello") == 0
