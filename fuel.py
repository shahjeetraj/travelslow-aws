import re

def main():
    fuel = ''
    while not re.match("^([0-9]+)/{1}([1-9]{1}[0-9]*)$",fuel):
        fuel = input("Fraction: ").strip()
    else:
        print(get_fuelpc(fuel))

def get_fuelpc(f):
    f = f.split('/')
    x = int(f[0])
    y = int(f[1])
    if x > y:
        main()
    elif x == y or x / y >= 0.99:
        return "F"
    elif x == 0 or x / y <= 0.01:
        return "E"
    else:
        return str(round(x/y*100))+"%"

main()