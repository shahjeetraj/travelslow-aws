menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

def main():
    try:
        bill = []
        while True:
            order = input("Item: ").title()
            if menu.get(order) == None:
                True
            else:
                bill.append(menu.get(order))
                print(f"Total: ${sum(bill):.2f}")

            #print(menu.get(order))


    except EOFError:
        exit()
main()
