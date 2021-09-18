#  ----------------------- Day 32 ----------------------
#  ----- Polymorphism  -------------------------
#  --- Date: 17.09.2021---------------------------------
#  Author: Muhammad Arslan Shahzad, 
#  ------------------------------------------------------


class Country():
	def capital(self):
		print("IslamAbad is the capital of Pakistan.")

	def language(self):
		print("Urdu is the most widely spoken language of Pakistan.")

	def type(self):
		print("Pakistan is a developing country.")

class USA():
	def capital(self):
		print("Washington, D.C. is the capital of USA.")

	def language(self):
		print("English is the primary language of USA.")

	def type(self):
		print("USA is a developed country.")

obj_pak = Country()
obj_usa = USA()
for country in (obj_pak, obj_usa):
	country.capital()
	country.language()
	country.type()


# Sample Output
	# IslamAbad is the capital of Pakistan.
	# Urdu is the most widely spoken language of Pakistan.
	# Pakistan is a developing country.
	# Washington, D.C. is the capital of USA.
	# English is the primary language of USA.
	# USA is a developed country.