from fuel import gauge, convert
import pytest

def test_convert():
    assert convert("1/8") == 12
    assert convert("1/2") == 50
    assert convert("1/4") == 25
    with pytest.raises(ZeroDivisionError):
        convert("0/0")
    with pytest.raises(ValueError):
        convert("a/b")
    with pytest.raises(ValueError):
        convert("8/2")
def test_gauge():
    assert gauge(99) == "F"
    assert gauge(2) == "2%"
    assert gauge(1) == "E"