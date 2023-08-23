import re

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):

    return re.search(r"[A-Z]{2}[A-Z1-9]*\W$",s)


main()