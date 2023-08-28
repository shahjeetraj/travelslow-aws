def main():
    # TAKE INPUT IN TRY + WHILE LOOP FOR EOF ERROR
    # CREATE LIST VARIABLE AND GET INPUTS IN WHILE LOOP
    family = []
    take_input = True
    while take_input == True:
        try:
            family.append(input("Name: ").strip().title())

        except EOFError:
            take_input = False
            #print(len(family))
            # CREATE OUTPUT STRING
            out=''
            if len(family) > 2:
                for i in range(len(family)-2):
                    out = "".join(out+family[i]+", ")
                out = ''.join(out+family[-2]+" and "+ family[-1])
            elif len(family) == 2:
                out = "".join(family[0]+" and "+family[1])
            else:
                out = family[0]

            # PROVIDE OUTPUT
            print()
            print(f"Adiue, adieu, to {out}")

main()