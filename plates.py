import re
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")
numbers = ["1","2","3","4","5","6","7","8","9","0"]
alphabets = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','Z','X','Y']


def is_valid(s):

    while re.match("[A-Z0-9]{2,6}$",s):
        if s[0].isalpha() and s[1].isalpha() and s[2] != '0':
            for i in range(2,len(s)-1):
                if s[i] in numbers:
                    if s[i+1] in alphabets:
                        return False

            return True

        else:
            return False
    #return re.match("^[A-Z]{2}((([A-Z1-9]{1})([A-Z0-9]{1,3}$)(?!(?:[A-Z]*[0-9]){2,}))|[A-Z0-9]{1,4})$",s)


main()