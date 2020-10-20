class HouseHeating:
	
	def __init__(self,current_temperature, goal_temperature): 
		self.current_temperature = current_temperature
		self.goal_temperature = goal_temperature

	def __str__(self):
		return F"The current temperature is {self.current_temperature} celsius."

	def set_temperature(self):
		self.current_temperature = self.goal_temperature
		return F"The goal temperature is {self.goal_temperature} celsius."

	def temperature_check(self):
		if self.current_temperature == self.goal_temperature:
			return "New sentting is done! \nThe current tempereture is {} celsius.".format(self.current_temperature)	
		else:
			self.current_temperature = 24
			return "There's been an error.\nThe tempereture is set to normal {} celsius.".format(self.current_temperature)

	def normal_temp_check(self):
		if 21 < self.current_temperature < 27:
			return "The current tempereture is in range of normal."	
		elif self.current_temperature > 27:
			return "The current tempereture is higher then recommended normal."
		elif self.current_temperature < 21:
			return "The current tempereture is lower then recommended normal."	
					

house_1 = HouseHeating(16,20)		
house_2 = HouseHeating(22,24)
house_3 = HouseHeating(18,26)
house_4 = HouseHeating(28,23)

print("\tHeat sistem settings for House 1\n",str(house_1))
print(house_1.set_temperature())
print(house_1.temperature_check())
print(house_1.normal_temp_check())

print("\tHeat sistem settings for House 2\n",str(house_2))
print(house_2.set_temperature())
print(house_2.temperature_check())
print(house_2.normal_temp_check())

print("\tHeat sistem settings for House 3\n",str(house_3))
print(house_3.set_temperature())
print(house_3.temperature_check())
print(house_3.normal_temp_check())

print("\tHeat sistem settings for House 4\n",str(house_4))
print(house_4.set_temperature())
print(house_4.temperature_check())
print(house_4.normal_temp_check())


