from seasons import check_date

def main():
    test_valid()
    test_invalid()

def test_valid():
    assert check_date("1997-03-03") == ("1997","03","03")
    assert check_date("1979-03-23") == ("1979","03","23")

def test_invalid():
    assert check_date("1st July, 1979") == None
    assert check_date("1979-1-1") == None
    #assert check_date("2011-13-01") == None
    #assert check_date("2011-11-41") == None

if __name__ == "__main__":
    main()