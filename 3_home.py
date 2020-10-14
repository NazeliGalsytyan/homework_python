#Task_1

class Circle:

	def __init__ (self, radius):
		self.radius = input("Enter circle radius value!\n")

	def area(self):	
		print("The area of the circle equals:")
		print(int(self.radius) **2 * 3.14)

	def perimeter(self):
		print("The perimeter of the circle equals:")
		print(int(self.radius) *2 * 3.14)

circle_area = Circle(1)	
circle_area.area()
circle_area.perimeter()		

#Task_2

# class PairIndices:

# 	def __init__(self, array, target):
# 		self.array = array
# 		self.target = target

# 	def pairing(self):	
# 		set_array = set()

# 		for i in self.array:
# 			num_1 = self.target - i
# 			if num_1 in set_array:
# 				print([num_1],array[i])
# 			else:
# 				set_array.add(array[i])

# #the_array = ([10,20,10,40,50,60,70])
# indices = PairIndices(([10,20,10,40,50,60,70]), 50)

# indices.pairing()

#Task_3

class Person:

	def __init__(self,name, surname, age):
		self.name = name
		self.surname = surname
		self.age = age

class Student(Person):		

	def  __init__(self,name, surname, age, university, faculty, course):
		Person.__init__(self,name, surname, age)
		self.university = university
		self.faculty = faculty
		self.course = course

class Worker(Person):
	
	def __init__(self,name, surname, age, profession, experience):
		Person.__init__(self,name,surname, age)
		self.profession = profession
		self.experience = experience 

student_1 = Student("Armen","Petrosyan",22, "YSMU", "Farmacology", 5 )
worker_1 = Worker("Alice","Shelunc", 40, "Manager", "15 years")

print(student_1.name, student_1.surname, student_1.age, student_1.university, student_1.faculty, student_1.course)
print(student_1.__dict__)

print(worker_1.name, worker_1.surname, worker_1.age, worker_1.profession, worker_1.experience)
print(worker_1.__dict__)




