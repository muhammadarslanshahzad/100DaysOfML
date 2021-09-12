#  ----------------------- Day 16 ----------------------
#  ----- closures  -------------------------
#  --- Date: 01.09.2021---------------------------------
#  Author: Muhammad Arslan Shahzad, 
#  ------------------------------------------------------

import logging
logging.basicConfig(filename='example.log',
					level=logging.INFO)


def logger(func):
	def log_func(*args):
		logging.info(
			'Running "{}" with arguments {}'.format(func.__name__,
													args))
		print(func(*args))
		
	return log_func			

def add(x, y):
	return x+y

def sub(x, y):
	return x-y



def main():
	
	add_logger = logger(add)
	sub_logger = logger(sub)

	add_logger(3, 3)
	add_logger(4, 5)

	sub_logger(10, 5)
	sub_logger(20, 10)
 
if __name__ == "__main__":
    main()


# Sample output
	# 6
	# 9
	# 5
	# 10