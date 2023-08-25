# MAIN FUNCTION TO CAPTURE VALUES
def main():
    grocery_list = []
    grocery_dict = {}
    try:
        while True:

            grocery = input("").strip()
            grocery_list.append(grocery)
            if grocery in grocery_dict.keys():
                #print("Yes")
                grocery_dict[grocery] = grocery_dict[grocery] + 1
            else:
                #print("No")
                grocery_dict[grocery] = 1

    except EOFError:
        sorted_grocery_dict = sorted(grocery_dict)
        print()
        for i in range(len(grocery_dict)):
            print(f"{grocery_dict.get(sorted_grocery_dict[i])} {sorted_grocery_dict[i].upper()}")

        exit()

main()