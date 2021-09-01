#  ----------------------- Day 16 ----------------------
#  ----- Modules  -------------------------
#  --- Date: 01.09.2021---------------------------------
#  Author: Muhammad Arslan Shahzad, 
#  ------------------------------------------------------

from calculation import sum
from calculation import subtraction
from calculation import pow
from calculation import mod

def main():
    a = int(input("Enter first number"))
    b = int(input("Enter first number"))

    print("SUM = ",sum(a,b))
    print("Difference = ",subtraction(a,b))
    print("a to power of b = ",pow(a,b))
    print("MOD = ",mod(a,b))
 

if __name__ == "__main__":
    main()


# Sample output
    # Enter first number10
    # Enter first number5
    # SUM =  15
    # Difference =  5
    # a to power of b =  100000
    # MOD =  0