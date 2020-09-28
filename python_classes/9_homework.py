#Task_1

print("Task_1")
def new_list(my_list:list) -> list:
	'''
	Function that removes duplicate numbers from a list.

	Parameters:
		a is the new created list with no duplicates.

	Returns:
		a: the new created list.	
	'''
	a = []
	for i in my_list:
		if i not in a:
			a.append(i)
		else:
			pass
	return a
my_list = [0,4,4,2,1,2,5]	
print(new_list(my_list))
print(new_list.__doc__)	
print(new_list.__annotations__)

#Task_2

print("Task_2")
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

def new_list(a:list,b:list) -> list:
	'''
	Program returns only common digits between lists.

	Parameters:
		a and b: given lists.
		c: new list.

	Returns:
		c: new list, with common digits.	
	'''
	c = []
	for i in a:
		if i in b and i not in c:
			c.append(i)
		else:
			pass
	return c
print(new_list(a,b))
print(new_list.__doc__)		
print(new_list.__annotations__)	

#Task_3

print("Task_3")
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
def my_list(a: list) -> list:
	'''
	Program prints out only numbers less then 5:

	Parameters:
		a: the given list.
		b: new list.

	Returns:
		b: new list , with numbers less then 5	

	'''
	b = []
	for i in a:
		if  i < 5 :
			b.append(i)
		else:
			pass
	return b
print(my_list(a))
print(my_list.__doc__)
print(my_list.__annotations__)		

#Task_4

print("Task_4")
user = input("Print anythong you want, I\'ll print it in  backwards order! \n")		

user_list = user.split()
user_list.reverse()

def backwards(user_list:list) -> str:
	'''
	Program prints user's input in backwards order.

	Parameters:
		user_list: splits every word of user's input.
		user_list.reverse(): puts elements in reverse order.
		string.join(): converts list to string.

	Returns:
		string.		
	'''
	string = " "
	return string.join(user_list)

print(backwards(user_list))
print(backwards.__doc__)
print(backwards.__annotations__)

#Task_5

#1
print("Task_5\n 1st variation.")
tuple_1 = (10, 4, "name", 7, "value")
def reverse_(tuple_1:tuple) -> tuple:
	'''
	Function reverses the tuple.

	Parameters:
		tuple_1: The given tuple.
		new_tuple: The new tuple with reversed elements.

	Returns:
		new_tuple	
		'''
	new_tuple = tuple_1[::-1]
	return new_tuple

print(reverse_(tuple_1))
print(reverse_.__doc__)
print(reverse_.__annotations__)	

#2
print("Task_5\n 2nd variation.")
tuple_1 = (10, 4, "name", 7, "value")
def new_tuple(tuple_1:tuple) -> tuple:
	'''
	Function reverses the tuple.

	Parameters:
		tuple_1: The given tuple.
		tuple_2: The new tuple with reversed elements.

	Returns:
		tuple_2	
		'''
	tuple_2 = reversed(tuple_1)
	return tuple(tuple_2)

print(new_tuple(tuple_1))
print(new_tuple.__doc__)
print(new_tuple.__annotations__)



