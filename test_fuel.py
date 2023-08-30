from fuel import convert,gauge
import pytest

def main():
    test_zerovalues()
    test_valueerror()
    test_positivesc()

def test_zerovalues():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")

def test_valueerror():
    with pytest.raises(ValueError):
        convert("3/2")

def test_positivesc():
    assert convert("1/4") == 25 and gauge(25) == "25%"
    assert convert("3/4") == 75 and gauge(75) == "75%"
    assert convert("1/100") == 1 and gauge(1) == "E"
    assert convert("0/100") == 0 and gauge(0) == "E"
    assert convert("99/100") == 99 and gauge(99) == "F"
    assert convert("10/10") == 100 and gauge(100) == "F"

if __name__ == "__main__":
    main()