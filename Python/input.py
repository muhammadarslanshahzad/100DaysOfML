#  ----------------------- Day 8 ----------------------
#  ----- Inputs  -------------------------
#  --- Date: 24.08.2021---------------------------------
#  Author: Muhammad Arslan Shahzad, 
#  ------------------------------------------------------

def main():
    name = input("Enter your name here : ")
    print(name)
    age = int(input("Enter age : "))
    if(age >= 18):
        print("you can cast vote.")
    else:
        print("You can't case vote.");
if __name__ == "__main__":
    main()


# Sample output
# Enter your name here : name 123
# name 123
# Enter age : 50
# you can cast vote.