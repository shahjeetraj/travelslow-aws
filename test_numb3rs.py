from numb3rs import validate
def main():
    test_positive()
    test_negative()

def test_positive():
    assert validate("255.255.0.255") == True
    assert validate("2.2.0.2") == True
    assert validate("1.0.0.1") == True

def test_negative():
    assert validate("cat") == False
    assert validate("275.3.2.1") == False
    assert validate("2753.2.1") == False

if __name__ == "__main__":
    main()