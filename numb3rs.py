import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))

def validate(ip):
    pattern = "^(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)$"
    if re.match(pattern,ip):
        return True
    else:
        return False

if __name__ == "__main__":
    main()