#Task_1

def triangle(b:int,h:int) -> int:
	'''
	Returns the area of the triangle.
	
	Parameters:
		b is the base and h is the height of the triangle.

	Returns:
		The area in int type.

	'''
	area = (b * h)/2
	print(int(area))

#Task_2


def reverse(user:str) -> str:
	
	''' Returns the reversed string.

	Parameters:
		user(str): The string which is to be reversed.

	Returns:
		Already reversed string.	


	'''
	user = user[::-1]
	print("The reverse is:",user)

 #Test_3


def upper_lower(user:str) -> int:
	# user = input("Say something and I\'ll calculate the number of\nupper case and lower case letters! \n")
	'''
	Calculates the number of upper and lower cases in the string.

	Parameters:
		upper: is for the upper cases.
		lower: is for lower cases. 	

	Returns:
		The sum of upper and lower cases.	
	'''
	upper = 0
	lower = 0
	for i in user:
		if i.isupper():
			upper += 1
		elif i.islower():
			lower += 1
		else:
			pass

	print("The number of upper case letters is :", upper)
	print("The number of lower case letters is :", lower)			

#Task_4


def palindrome(user:str) -> str:
	# user = input("Say somethong and I\'ll check if that\'s palindrome or not! \n")
	'''
	Checks whether the string is palindrome or not.

	Parameters:
		user(str): The string which is to be checked:

	Returns:
		"That is palindrime" if the user(str) is palindrome.
		"That's not palindrome" if the user(str) is not palindrome.	
	'''
	if user == user[::-1]:
		print("That is palindrome!")
	else:
		print("That\'s not palindrome!")	


