from plates import is_valid

def main():
    test_alphain7()
    test_alphanotin7()
    test_alnucorr()
    test_alnumwrng()

def test_alphain7():
    assert is_valid("PYTHON") == True
    assert is_valid("python") == False
    assert is_valid("VANITY") == True
    assert is_valid("CRYPTO") == True

def test_alphanotin7():
    assert is_valid("PYTHONABLE") == False
    assert is_valid("FASHIONISTA") == False
    assert is_valid("wrong answer") == False
    assert is_valid("AWESOMENESS") == False


def test_alnucorr():
    assert is_valid("CS50") == True
    assert is_valid("CS500") == True
    assert is_valid("PY5000") == True
    assert is_valid("PY1110") == True

def test_alnumwrng():
    assert is_valid("CS50P2") == False
    assert is_valid("CS500A") == False
    assert is_valid("PY0400") == False
    assert is_valid("PY1110N") == False


if __name__ == "__main__":
    main()