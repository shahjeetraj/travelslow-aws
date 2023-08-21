def main():
    inp = input("What time is it? ")
    inp = inp.strip()
    inp_time = convert(inp)
    if inp_time >= 7.00 and inp_time <=8.00:
        print("breakfast time")
    elif inp_time >= 12.00 and inp_time <= 13.00:
        print("lunch time")
    elif inp_time >= 18.00 and inp_time <= 13.00:
        print("dinner time")
    else: print("",end="")


def convert(time):
    timef = float(time.replace(":","."))
    return timef


if __name__ == "__main__":
    main()