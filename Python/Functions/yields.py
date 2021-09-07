#  ----------------------- Day 22 ----------------------
#  ----- Yield Fucntions  -------------------------
#  --- Date: 07.09.2021---------------------------------
#  Author: Muhammad Arslan Shahzad, 
#  ------------------------------------------------------


def nextSquare():
    i = 1
  
    while True:
        yield i*i                
        i += 1



def main():
    for num in nextSquare():
        if num > 100:
            break    
        print(num)


if __name__ == "__main__":
    main()


# Sample output
    # 1
    # 4
    # 9
    # 16
    # 25
    # 36
    # 49
    # 64
    # 81
    # 100