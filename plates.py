import re

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):

    return re.match(r"^(?=[A-Za-z]{2,6}$)(?!.*[0-9]{2})(?!.*[. ])[A-Za-z0-9]*[1-9]?[A-Za-z]*$"
,s)


main()