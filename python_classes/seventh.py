import random

# for i in range(1,11):
# 	print(f"this is for {i}")
# 	for j in range(1,11):
# 		print("{} x {} = {}".format(i, j, i * j))


#1
# for i in range(10):
# 	print(str(i) * i)
# for j in range(10 - 1, 0, -1):
# 	print(str(j) * j)

# #2
# for i in range(1,12):
# 	print(str(i) * i)
# 	if i == 6: 
# 		for j in range(5, 0, -1):
# 			print(str(j) * j)
# 		break	

# a = 7
# b = 5
# while a > b:
# 	print(f"{a} > {b}")
# 	a -= 1


# password =input("Enter your password. \n")
# while len(password) < 8:
# 	print("Your password should contain at least 8 characters.")
# 	password = input("Enter your password. \n")
	
#1
# password =input("Enter your password. \n")
# while len(password) < 8:
# 	print("Your password should contain at least 8 characters.")
# 	password = input("Enter your password. \n")
# 	while "." not in password:
# 		print("Your password should contain a dot.")
# 		password = input("Enter your password. \n")

#2
# while True:
# 	password = input("Enter your password \n")
# 	if len(password) > 8:
# 		if "." in password:
# 			break

# a = random.randint(4,6)
# user = int(input("Can your guess the number between 4-6? \n"))
# while user != a:
# 	print("Try again!")
# 	user = int(input("Guess the number between 4-6? \n"))
# print("Good job!")	


#1
# score = 0
# i = 0
# while i < 5:	
# 	user_answer = int(input("Guess the number \n"))
# 	random_number = random.randint(1,5)

# 	if user_answer == random_number:
# 		score += 1
# 	i += 1	 	

# print("Your score is ", score)
	
#2
# score = 0
# user_check= "y"
# rounds = 0
# while user_check == "y":	
# 	user_answer = int(input("Guess the number \n"))
# 	random_number = random.randint(1,5)

# 	if user_answer == random_number:
# 		score += 1 	

# 	user_check = input("Do you want to play again: y for yes !")
# 	rounds += 1

# print(f"Your score is {score} you have played {rounds} time!")
	











