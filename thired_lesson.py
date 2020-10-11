#1

# class Text(object):

# 	def __init__(self,age):
# 		self.name = input("tell me something \n")
# 		self.age = age

# 	def printing(self):
# 		print(self.name)
# 		print(self.age)

# my_object = Text(19)
# my_object2 = Text(20)

# my_object.printing()
# my_object2.printing()			 

#2

# class Rectangle:

# 	def __init__(self):
# 		self.side_1 = int(input("give side_1's value"))
# 		self.side_2 = int(input("give side_2's value"))
# 		self.side_3 = int(input("give side_3's value"))

# 	def summing(self):
# 		print(self.side_1 + self.side_2 + self.side_3)	

# my_answer = Rectangle()
# my_answer.summing()

#3

class Vehicle:

	def __init__(self, seats):
		self.seats = seats

	# def print_seats(self):
	# 	print(self.seats)	


class Car(Vehicle):

	def __init__(self, name, color, seats):
		self.name = name
		self.color = color
		Vehicle.__init__(self,seats)

		#self.real_seats = self.seats

# bmw = Car("BMW", "red", 8)
# print(bmw.name, bmw.color, bmw.seats, bmw.real_seats)		

# bmw.print_seats()

# print(bmw)
# print(bmw.__dict__)

class Bicycle(Vehicle):

	def __init__(self, color, brand, wheel, seats):
		self.color = color
		self.brand = brand
		self.wheel = wheel
		Vehicle.__init__(self,seats)

bicycle = Bicycle("yellow", "kawasaki", 2, 1)	
print(bicycle.color, bicycle.brand, bicycle.wheel,bicycle.seats)
print(bicycle.__dict__)	












