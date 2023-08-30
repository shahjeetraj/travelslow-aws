import sys
import os

def main():
    if len(sys.argv) == 1:
        print("Too few command-line arguments")
        sys.exit()
    elif len(sys.argv) > 2:
        print("Too many command-line arguments")
        sys.exit()
    elif not os.path.exists(sys.argv[1]):
        print("File does not exist")
        sys.exit()
    elif not sys.argv[1].endswith(".py"):
        print("Not a Python file")
        sys.exit()
    else:
        print(cnt_lines(sys.argv[1]))

def cnt_lines(f_name):
    with open(f_name,'r') as file:
        cnt = 0
        for line in file:
            if line.lstrip().startswith("#") or len(line.lstrip()) == 0:
                cnt += 0
            else:
                cnt += 1
        return cnt

if __name__ == "__main__":
    main()