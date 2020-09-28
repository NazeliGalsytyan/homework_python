# number = input("tell me a number and I\'ll return the half of it. \n")

# try:
# 	half = int(number)/ 2
# 	print(half)
# except ValueError:
# 	print("your input should contain only numbers.")		


# num_1 = int(input("tell me a number to devide 4 with \n"))
# try:
# 	new_value = 4/ num_1
# 	print(new_value)
# except ZeroDivisionError:	
# 	print("your input should not be zerro.")	

# try:
# 	print(hello)
# except NameError:
# 	print("hello is not defined")		

# input_ = input("tell me a number \n")

# try:
# 	input_ = int(input)
# except ValueError:
# 	input_ = (input("tell me a number \n"))

# 	try:
# 		input_ = int(input_)
# 	except:
# 		print("OK your value will be 1 by defaulf ! " )
# 		input_1 = 1
# summery = input_ + 5 



#############Pasword#############

check = True
while check:
	try:
		password = input("Tell me your Password.")
		
		if len(password) < 8:
			raise ValueError("It should be greather than 8.")
		
		check_ = False
		for i in password:
			if  i.isdigit():
				check_ = True
			if not i.isalpha():
				if i != " ":
					break
				else:
					raise NameError("The password could not contain a space.")
			
		if not check_:
			raise TypeError("Should contain at least one number.")
		if password[0].islower():
			raise Exception("Should start with a capital letter.")
		check = False
	except ValueError as e:
		print(e)
	except NameError as n:
		print(n)
	except TypeError as t:
		print(t)
	except Exception as ex:
		print(ex)
print(F"{password} is a strong one, thanks!!!")










