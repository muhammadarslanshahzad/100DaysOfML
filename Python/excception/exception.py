#  ----------------------- Day 17 ----------------------
#  ----- Exception  -------------------------
#  --- Date: 02.09.2021---------------------------------
#  Author: Muhammad Arslan Shahzad, 
#  ------------------------------------------------------

def main():
    try:
        a = int(input("Enter a : "))
        b = int(input("Enter b : "))
        c = a/b
        print("a/b = %d"%c)

    except:
        print("can't print by zero")


if __name__ == "__main__":
    main()


# Sample output
    # Enter a : 12
    # Enter b : 6
    # a/b = 2

    # Enter a : 12
    # Enter b : 0
    # can't print by zero