import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if re.search(r'(https?://)?(www\.)?'
                '(youtube|youtu|youtube-nocookie)\.(com|be)/'
                '(watch\?.*?(?=v=)v=|embed/|v/|.+\?v=)?([^&=%\?]{11})',s) != None and re.search('iframe',s) != None:
        x = re.search(r'(https?://)?(www\.)?'
                '(youtube|youtu|youtube-nocookie)\.(com|be)/'
                '(watch\?.*?(?=v=)v=|embed/|v/|.+\?v=)?([^&=%\?]{11})',s)
        #print(x.group())
        found_list = re.split("\/",x.group())
        return "".join("https://youtu.be/"+found_list[-1])
    else:
        return None


if __name__ == "__main__":
    main()