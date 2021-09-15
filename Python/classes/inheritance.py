#  ----------------------- Day 30 ----------------------
#  ----- Inheritance in python classes  -------------------------
#  --- Date: 15.09.2021---------------------------------
#  Author: Muhammad Arslan Shahzad, 
#  ------------------------------------------------------

# parent class
class Person( object ):	

		# __init__ is known as the constructor		
		def __init__(self, name, idnumber):
				self.name = name
				self.idnumber = idnumber
		def display(self):
				print(self.name)
				print(self.idnumber)

# child class
class Employee( Person ):		
		def __init__(self, name, idnumber, salary, post):
				self.salary = salary
				self.post = post

				Person.__init__(self, name, idnumber)

				
a = Employee('Arslan', 886012, 200000, "Intern")	

a.display()


# Sample Output
    # Arslan
    # 886012