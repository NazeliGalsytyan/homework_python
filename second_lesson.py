class Fruit:
	def __init__(self,name, color, price):
		self.name = name
		self.color = color
		self.price_kg = price
		self.kg = 0

	def presentation(self):
		text = "this fruit is {} it's color is {} and price for kg is {}, kg is {}".format(self.name, self.color, self.price_kg, self.kg)
		print(text)

	def set_kg(self, kg):
		if kg > 0:
			self.kg = kg
		else:
			print(F"wrong kg, the kg remains {self.kg}")	
				
banana.kg = -5
Orange = Fruit("Orange","orange", "500")
print(type(Orange))
banana = Fruit("banana", "yellow", "700")

print(Orange.name, "is", Orange.price_kg)		
print(banana.name, banana.price_kg)

Orange.presentation()
banana.presentation()


# class Car:
# 	def __init__(self, brand, model, color, year):
# 		self.brand = brand
# 		self.model = model
# 		self.color = color
# 		self.year = year

# 	def presentation(self):
# 		text = "The car brand is {} \n Model is {} \n Color is {} \n Year {}".format(self.brand, self.model, self.color, self.year)	
# 		print(text)

# Mercedes = Car("Mercedes","C class", "black", "2010")
# BMW = Car("BMW","X5","gray","2008")
# Toyota = Car ("Toyota", "Vitz","white", "2018")	


# Mercedes.presentation()
# BMW.presentation()
# Toyota.presentation()	





