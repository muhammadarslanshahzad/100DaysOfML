#  ----------------------- Day 29 ----------------------
#  ----- Destructors in python classes  -------------------------
#  --- Date: 14.09.2021---------------------------------
#  Author: Muhammad Arslan Shahzad, 
#  ------------------------------------------------------

class Employee:

	def __init__(self):
		print('Employee created')

	def __del__(self):
		print("Destructor called")

def Create_obj():
	print('Making Object...')
	obj = Employee()
	print('function end...')
	return obj

print('Calling Create_obj() function...')
obj = Create_obj()
print('Program End...')


# Sample Output
    # Calling Create_obj() function...
    # Making Object...
    # Employee created
    # function end...
    # Program End...
    # Destructor called