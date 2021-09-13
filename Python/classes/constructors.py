#  ----------------------- Day 28 ----------------------
#  ----- Constructors in python classes  -------------------------
#  --- Date: 13.09.2021---------------------------------
#  Author: Muhammad Arslan Shahzad, 
#  ------------------------------------------------------

class Addition:
	first = 0
	second = 0
	answer = 0
	
	def __init__(self, f, s):
		self.first = f
		self.second = s
	
	def display(self):
		print("First number = " + str(self.first))
		print("Second number = " + str(self.second))
		print("Addition of two numbers = " + str(self.answer))

	def calculate(self):
		self.answer = self.first + self.second

obj = Addition(1000, 2000)

obj.calculate()

obj.display()


#Sample Output
    # First number = 1000
    # Second number = 2000
    # Addition of two numbers = 3000