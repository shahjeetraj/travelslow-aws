import re

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    while re.match("[A-Z0-9]{2,6}$",s):
        if s[0].isalpha() and s[1].isalpha():
            if int(s[2]) == 0:
                return False
            else:
                for i in range(2,len(s)-1):
                    if int(s[i]).isnumeric():
                        #print(s[i])
                        if s[i+1].isalpha():
                            return False

                    else:
                        pass
                return True
        else:
            return False
    #return re.match("^[A-Z]{2}((([A-Z1-9]{1})([A-Z0-9]{1,3}$)(?!(?:[A-Z]*[0-9]){2,}))|[A-Z0-9]{1,4})$",s)


main()