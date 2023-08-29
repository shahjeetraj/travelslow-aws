from bank import value

def main():
    test_bank_for_100()
    test_for_20()
    test_for_0()
    #test_int()
    #test_punct()
    #test_100()
    #test_20()
    #test_0()

def test_bank_for_100():
    assert value("Whats up?") == 100
    assert value("What's up") == 100

def test_for_20():
    assert value("Hey") == 20
    assert value("Hi") == 20
    assert value("HEY") == 20

def test_for_0():
    assert value("Hello, Kramer!") == 0
    assert value("HeLLo") == 0
    assert value("HELLO") == 0

#def test_int():
#    assert value('1') == 100

#def test_0():
#    assert value('Hello, how"s going?') == 0
#    assert value('HELLO') == 0

#def test_20():
#    assert value('h') == 20
#    assert value('hey, good') == 20
#    assert value('HOLA ') == 20

#def test_100():
#    assert value('wow, hello') == 100
#    assert value('LalhalHa') == 100

#def test_punct():
#    assert value(' .,;: "') == 100

if __name__ == "__main__":
    main()
