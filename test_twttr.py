from twttr import shorten

def main():
    test_lower_upper_cases()
    test_numeric_cases()
    test_punctuations()

def test_lower_upper_cases():
    assert shorten("What's your name? ") == "Wht's yr nm? "
    assert shorten("Twitter") == "Twttr"
    assert shorten("python") == "pythn"

def test_numeric_cases():
    assert shorten('1234') == '1234'

def test_punctuations():
    assert shorten(',.!&') == ',.!&'
# RUN MAIN FUNCTION
if __name__ == "__main__":
    main()