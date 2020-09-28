# #Task_1

# the_list = [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
# def lists(the_list:list) -> list:
# 	'''
# 	Program removes duplicates for a list of lists.

# 	Parameters:
# 		the_list: The given list with lists in it.
# 		new_list: The new list with no duplicates.

# 	Returns:
# 		new_list	
# 	'''
# 	new_list = []
# 	for i in the_list:
# 		if i not in new_list:
# 			new_list.append(i)
# 		else:
# 			pass
# 	return new_list
	
# print(lists(the_list))	
# print(lists.__annotations__)
# print(lists.__doc__)	


# #Task_2

# original_list = [0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]]
# def lists(original_list:list)-> list:
# 	'''
# 	Function flattens a given nested list structure.

# 	Parameters:
# 		original_list: The given list with nested lists.
# 		new_list: new list, without nested lists in it.

# 	Returns:
# 		new_list	
# 	'''
# 	new_list = []
# 	for i in original_list:
# 		if type(i) != list:
# 			new_list.append(i)
# 		else:	
# 			new_list += i
			
# 	return new_list
# print(lists(original_list))	
# print(lists.__doc__)
# print(lists.__annotations__)

# #Task_3

# original_list = [1,1,2,3,4,4,5,1]
# first_list_len = 3	
# def new_list(original_list:list, a:int) -> list:
# 	'''
# 	Function that splits a given list into two parts.

# 	Parameters:
# 		original_list: The given list.
# 		first_list_len: Lenght of the first part of the list.

# 	Returns:
# 		original_list split into 2 parts.	

# 	'''
# 	return original_list[0:a], original_list[a:]

# print(new_list(original_list, first_list_len))	
# print(new_list.__annotations__)
# print(new_list.__doc__)

#Task_4

check = True
while check:
	try:
		number = input("Enter an even number and I\'ll give you the reciprocal. \n")
		
		# if not number.isdigit():
		# 	raise TypeError ("Wrong type, you should enter a number.")
		
		if number == 0:
			raise ZeroDivisionError ("Your number could not be 0.")


		if int(number) % 2 == 0:
			reciprocal = 1 / int(number)
			print(f"The reciprocal of {number} is {reciprocal}!!")
		
		if int(number) % 2 != 0:
			print("The number is not even.")
			

			
		check = False		
	except TypeError as t:
		print(t)
	except ZeroDivisionError as zero:
		print(zero)	

# print(f"The reciprocal of {number} is {reciprocal}!!")

#Task_5

# print("Task, to have this on terminal.")

# b = '''
# 	 --- --- --- 
# 	|   |   |   | 
# 	 --- --- ---  
# 	|   |   |   | 
# 	 --- --- ---  
# 	|   |   |   | 
# 	 --- --- ---
# 	'''	
# print(b)

