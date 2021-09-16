#  ----------------------- Day 31 ----------------------
#  ----- Encapsulation  -------------------------
#  --- Date: 16.09.2021---------------------------------
#  Author: Muhammad Arslan Shahzad, 
#  ------------------------------------------------------

# Creating a Base class
class Base:
	def __init__(self):
		self.a = "GeeksforGeeks"
		self.__c = "GeeksforGeeks"

# Creating a derived class
class Derived(Base):
	def __init__(self):
		
		# Calling constructor of
		# Base class
		Base.__init__(self)
		print("Calling private member of base class: ")
		print(self.__c)
# Driver code
obj1 = Base()
print(obj1.a)


# Sample output
    # GeeksforGeeks