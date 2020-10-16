class ArmenianCuisine:

	def __init__(self, dish_1, dish_2):
		self.dish_1 = dish_1
		self.dish_2 = dish_2
	

	def arm_presentation(self):
		print(f"This is Armenian cuisine, we can recomend you {self.dish_1}\n{self.dish_2}")	

class GreekCuisine:
	def __init__(self, dish1, dish2):
		self.dish1 = dish1
		self.dish2 = dish2
	
	def greek_presentation(self):
		print(f"This is Greek cuisine, we can recomend you {self.dish1}\n{self.dish2}")	


class MixedCuisine(ArmenianCuisine, GreekCuisine):

	def __init__(self ,dish_1, dish_2, dish1, dish2):
		ArmenianCuisine.__init__(self, dish_1, dish_2)
		GreekCuisine.__init__(self,dish1,dish2)

	def mixed_presentation(self):

		self.arm_presentation()
		self.greek_presentation()

mixed_manu = MixedCuisine("Dolma", "Xash", "Khachapuri", "Xinkali")
#MixedCuisine.mixed_presentation(mixed_manu)
mixed_manu.mixed_presentation()


