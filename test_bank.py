from bank import value

def test_for_100():
    assert value("Whats up?") == "$100"
    assert value("What's up") == "$100"

def test_for_20():
    assert value("Hey, there") == "$20"
    assert value("hey") == "$20"
    assert value("HEY") == "$20"

def test_for_0():
    assert value("Hello, Kramer!") == "$0"
    assert value("Hello") == "$0"
    assert value("HELLO") == "$0"

test_for_100()
test_for_20()
test_for_0()