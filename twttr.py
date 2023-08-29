# SETUP MAIN FUNCTION THAT TAKES TEXT INPUT
def main():
    text = input("Input: ")
    print(f"Output: {shorten(text)}")


# SETUP TWTTRZE FUNCTION TO REMOVE VOWELS
def shorten(word):
    new_text = ''
    for i in range(len(word)):
        if word[i].lower() not in ['a','e','i','o','u']:
            new_text += word[i]
        else:
            pass
    return new_text


# RUN MAIN FUNCTION
if __name__ == "__main__":
    main()