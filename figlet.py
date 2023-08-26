import sys
import random
from pyfiglet import Figlet
figlet = Figlet()

def main():
    # UNDERSTAND IF THE COMMAND HAD FONT PROVIDED
    # STORE A VARIABLE BASIS IF FONT PROVIDED OR NOT
    # EXIT IF WRONG SYNTAX OR FONT USED
    if len(sys.argv) == 1:
        random_font = True
    elif len(sys.argv) == 3 and sys.argv[1] in ['-f','--font'] and sys.argv[2] in figlet.getFonts():
        random_font = False
    else:
        print("Invalid usage")
        sys.exit(1)

    # GET AND STORE INPUT
    text = input("Input: ")

    if not random_font:
        figlet.setFont(font = sys.argv[2])
    print(figlet.renderText(text))

main()