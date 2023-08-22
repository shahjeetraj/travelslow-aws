import re

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):

    return re.search(r"[a-z]{2}[a-z1-9]*",s,re.IGNORECASE)


main()