#  ----------------------- Day 11 ----------------------
#  ----- If statements  -------------------------
#  --- Date: 27.08.2021---------------------------------
#  Author: Muhammad Arslan Shahzad, 
#  ------------------------------------------------------

def main():
    age = int(input("Enter your age"))
    if(age>=18):
        print("Eligible for casting vote")
    else:
        print("Not eligible")
    
    car = 'subaru'
    print( "True." if car == 'subaru' else "False")



if __name__ == "__main__":
    main()


# Sample output
    # Enter your age18
    # Eligible for casting vote
    # True.