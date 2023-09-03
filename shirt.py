import os
import sys
from PIL import Image, ImageOps

# CREATE A MAIN FUNCTION THAT WILL CHECK INPUT AND THEN PASTE FILES
def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif not os.path.exists(sys.argv[1]):
        sys.exit("Input does not exist")
    elif os.path.splitext(sys.argv[2].lower())[1] not in ['.jpg','.jpeg','.png']:
        #print(os.path.splitext(sys.argv[2].lower())[1])
        sys.exit("Invalid output")
    elif os.path.splitext(sys.argv[1].lower())[1] != os.path.splitext(sys.argv[2].lower())[1]:
        sys.exit("Input and output have different extensions")
    else:
        size = paste_image(sys.argv[1],sys.argv[2])
        sys.exit()

def paste_image(before,after):
    image_file = Image.open(before)
    shirt = Image.open("shirt.png")
    size = shirt.size
    before1 = ImageOps.fit(image_file,size)
    before1.paste(shirt, shirt)
    before1.save(after)

if __name__ == "__main__":
    main()