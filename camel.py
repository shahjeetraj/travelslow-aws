def main():
    text = input("camelCase: ")
    print(f"snake_case: {snake_case(text)}")

def snake_case(t):
    new_text = ''
    for i in range(len(t)):
        if t[i].isupper():
            t[i].replace(t[i],"_"+t[i].lower())
            new_text += ("_"+t[i].lower())
        else:
            new_text += (t[i])

    return new_text



main()