#  ----------------------- Day 16 ----------------------
#  ----- Classes  -------------------------
#  --- Date: 12.09.2021---------------------------------
#  Author: Muhammad Arslan Shahzad, 
#  ------------------------------------------------------


class Dog:
	
	attr1 = "mammal"
	attr2 = "dog"

	def fun(self):
		print("I'm a", self.attr1)
		print("I'm a", self.attr2)

Rodger = Dog()

print(Rodger.attr1)
Rodger.fun()


#Sample Output
    # mammal
    # I'm a mammal
    # I'm a dog