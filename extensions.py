import os

def main():
    file_name = input("File name: ")
    split_tup = os.path.splitext(file_name.lower().strip())
    file_ext = split_tup[1]
    getfile_type(file_ext)

def getfile_type(f):
    if f == ".gif":
        print("image/gif")
    elif f == ".jpg" or f == ".jpeg":
        print("image/jpeg")
    elif f == ".png":
        print("image/png")
    elif f == ".pdf":
        print("application/pdf")
    elif f == ".txt":
        print("text/plain")
    elif f == ".zip":
        print("application/zip")
    else: print("application/octet-stream")

main()