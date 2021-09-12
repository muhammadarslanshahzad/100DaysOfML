#  ----------------------- Day 26 ----------------------
#  ----- Memoization  -------------------------
#  --- Date: 011.09.2021---------------------------------
#  Author: Muhammad Arslan Shahzad, 
#  ------------------------------------------------------

def memoize_factorial(f):
	memory = {}

	def inner(num):
		if num not in memory:		
			memory[num] = f(num)
		return memory[num]

	return inner
	
@memoize_factorial
def facto(num):
	if num == 1:
		return 1
	else:
		return num * facto(num-1)



def main():
    print(facto(5))
    print(facto(4))
    print(facto(3))
    print(facto(2))
 
if __name__ == "__main__":
    main()


# Sample output
    # 120
    # 24
    # 6
    # 2