# SETUP MAIN FUNCTION THAT TAKES TEXT INPUT
def main():
    text = input("Input: ")
    print(f"Output: {twttrze(text)}")


# SETUP TWTTRZE FUNCTION TO REMOVE VOWELS
def twttrze(t):
    new_text = ''
    for i in range(len(t)):
        if t[i] not in ['a','e','i','o','u']:
            new_text += t[i]
        else:
            pass
    return new_text


# RUN MAIN FUNCTION
main()