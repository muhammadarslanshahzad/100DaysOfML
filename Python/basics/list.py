#  ----------------------- Day 9 ----------------------
#  ----- List  -------------------------
#  --- Date: 25.08.2021---------------------------------
#  Author: Muhammad Arslan Shahzad, 
#  ------------------------------------------------------

def main():
    fruits = ['apple', 'mango','orange']
    print(fruits[0])
    print(fruits[1].title())
    print(fruits[-1])
    print(fruits)

    fruits[0] = 'banana'
    print(fruits)



if __name__ == "__main__":
    main()


# Sample output
# apple
# Mango
# orange
# ['apple', 'mango', 'orange']
# ['banana', 'mango', 'orange']