import re

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):

    return re.match("^[A-Z]{2}(^(?:(?=[A-Z0-9]{2,4}$)(?![A-Z]*[0-9][A-Z]*$)|[A-Z0-9]{2,4})$)",s)


main()