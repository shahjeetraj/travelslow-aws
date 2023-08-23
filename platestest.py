numbers = ["1","2","3","4","5","6","7","8","9","0"]
alphabets = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','Z','X','Y']


s = input("Plate: ")
for i in range(len(s)-1):
    if s[i] in numbers:
        if s[i+1] in alphabets:
            print("fish0")
        else:
            print("fudget")
