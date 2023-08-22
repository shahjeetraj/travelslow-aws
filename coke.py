# DEFINE MAIN WHERE INPUT IS TAKEN WITH WHILE LOOP
# ALSO IN MAIN, THERE IS A VARIABLES CALLED COINS INSERTED, PRICE & CHANGE DUE.
# WHILE LOOP WILL CHECK THAT UNLESS THE CHANGE DUE IS 0, INSERT COIN NEEDS TO BE RUN
def main():
    price = 50
    change_due = 50
    while change_due != 0:
        ins_coins = int(input(f"Amount Due: {change_due}\nInsert Coin: "))
        if ins_coins in [5,10,25]:
            change_due = change_due - ins_coins
        else:
            pass
    print("Change Owed: 0")


# CALL MAIN FUNCTION
main()