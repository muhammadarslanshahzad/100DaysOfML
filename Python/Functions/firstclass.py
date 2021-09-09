#  ----------------------- Day 24 ----------------------
#  ----- First Class Functions  -------------------------
#  --- Date: 09.09.2021---------------------------------
#  Author: Muhammad Arslan Shahzad, 
#  ------------------------------------------------------


def create_adder(x):
	def adder(y):
		return x+y

	return adder


def main():
    add_15 = create_adder(15)

    print (add_15(10))


if __name__ == "__main__":
    main()


# Sample output
    # 25