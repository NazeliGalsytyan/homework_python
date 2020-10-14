class Country:

	def __init__(self, continent,name_country):
		self.continent = continent
		self.name_country = name_country

	def country_presemtation(self):
		country_return = F"This prodact is made in {self.continent} in {self.name_country}."
		
		return country_return

class Brand:

	def __init__(self,name_brand,start_date):
		self.name_brand = name_brand
		self.start_date = start_date

	def brand_presentation(self):
		brand_return = F"The brand is {self.name_brand}, which has been founded on {self.start_date}."

		return brand_return

class Season:

	def __init__(self,name_season, average_temp):
		self.name_season = name_season
		self.average_temp = average_temp

	def season_presentation(self):
		season_return = F"In {self.name_season} the averege temperature is {self.average_temp} celcius."

		return season_return

class Product(Country,Brand,Season):

	def __init__(self, name,type_,quantity,price,continent,name_country,name_brand, start_date,name_season,average_temp):
		self.name = name
		self.type_ = type_	
		self.quantity = quantity
		self.price = price
		Country.__init__(self,continent,name_country)
		Brand.__init__(self,name_brand, start_date)
		Season.__init__(self,name_season, average_temp)				
					
	def product_presentation(self):
		print(F"{self.name} is a type of {self.type_}.\nThe price for {self.quantity} is {self.price} Euro")
		print(self.country_presemtation())
		print(self.brand_presentation())
		print(self.season_presentation())

	# def quantity_increase(self):
	# 	new_quantity = int(input("Please enter wanted quantity. \n"))

	# 	return new_quantity

	def discount(self):
		percent = 50
		#new_price = new_quantity * self.price * percent / 100
		print(int(2 * 100 * percent / 100))
		

prodact = Product("T-shirt", "clothing",1,100,"Europe","Italy","Prada",1913, "Spring", 24 )
prodact.product_presentation()
print("This clothing is the perfect purchase. \n\n\t And guess what? \n\nYes, we have a discount!!! \nGet 2 for 50%  off, in total for ")
#print(Product.quantity_increase())
prodact.discount()
	