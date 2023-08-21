def main():
    inp = input("What time is it? ")
    inp = inp.strip()
    inp_time = convert(inp)
    #print(inp_time)
    if inp_time >= 7.00 and inp_time <=8.00:
        print("breakfast time")
    elif inp_time >= 12.00 and inp_time <= 13.00:
        print("lunch time")
    elif inp_time >= 18.00 and inp_time <= 19.00:
        print("dinner time")
    else: print("",end="")


def convert(time):
    timef = time.split(":")
    h = int(timef[0])
    m = int(timef[1])/60
    return float(h+m)


if __name__ == "__main__":
    main()