import re

def main():
    fuel = ''
    while not re.match("^[0-4]/[124]$",fuel):
        fuel = input("Fraction: ").strip()
    else:
        print(get_fuelpc(fuel))

def get_fuelpc(f):
    x = int(f[0])
    y = int(f[2])
    if x == y == 4:
        return "F"
    elif x == 0:
        return "E"
    else:
        return str(int(x/y*100))+"%"

main()