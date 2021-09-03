#  ----------------------- Day 18 ----------------------
#  ----- Date and Time  -------------------------
#  --- Date: 3.09.2021---------------------------------
#  Author: Muhammad Arslan Shahzad, 
#  ------------------------------------------------------

import time

def main():
    print(time.asctime(time.localtime(time.time())))
    
    for i in range(0,5):
        print(i)
        time.sleep(i)

if __name__ == "__main__":
    main()


# Sample output
    # Fri Sep  3 17:32:00 2021
    # 0
    # 1
    # 2
    # 3
    # 4