#  ----------------------- Day 13 ----------------------
#  ----- Functions  -------------------------
#  --- Date: 29.08.2021---------------------------------
#  Author: Muhammad Arslan Shahzad, 
#  ------------------------------------------------------

def greet():
    print("Hello World")

def add(a,b):
    c=a+b
    return c



def main():
    greet()
    a=int(input("Enter first digit : "))
    b=int(input("Enter first digit : "))
    print(add(a,b))



if __name__ == "__main__":
    main()


# Sample output
    # Hello World
    # Enter first digit : 10
    # Enter first digit : 12
    # 22