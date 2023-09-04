from um import count

def main():
    test_valid()
    test_invalid()
    test_invalid1()

def test_valid():
    assert count("um?") == 1
    assert count("Um, thanks for the album.") == 1
    assert count("Um, thanks, um...") == 2

def test_invalid():
    assert count("yum") == 0
    assert count("Album") == 0
    assert count("Fryums!") == 0
    assert count("Dum Dum") == 0

def test_invalid1():
    assert count("Books") == 0
    assert count("Books and Guns") == 0