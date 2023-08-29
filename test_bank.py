from bank import value

def main():
    test_for_100()
    test_for_20()
    test_for_0()

def test_for_100():
    assert value("Whats up?") == "$100"

def test_for_20():
    assert value("Hey, there") == "$20"

def test_for_0():
    assert value("Hello, Kramer!") == "$0"

if __name__ == "__main__":
    main()