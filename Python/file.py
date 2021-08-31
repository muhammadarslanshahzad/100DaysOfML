#  ----------------------- Day 15 ----------------------
#  ----- File IO  -------------------------
#  --- Date: 31.08.2021---------------------------------
#  Author: Muhammad Arslan Shahzad, 
#  ------------------------------------------------------

from typing import Counter


def main():
    fileptr = open("file.txt", "w")
    fileptr.write("my file using python")
    fileptr.close()

    fileptr1 = open("file.txt", 'r')
    cont = fileptr1.read()
    fileptr1.close()
    print(type(cont))
    print(cont)

if __name__ == "__main__":
    main()


# Sample output
    # <class 'str'>
    # my file using python