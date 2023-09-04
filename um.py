import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    return len(re.findall(r'\b\W*um\W',s.lower()))


if __name__ == "__main__":
    main()