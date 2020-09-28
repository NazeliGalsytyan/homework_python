import random
#from file import my_func
#Task_1

#1
# num = int(input("Enter a number and I\'ll tell you the factiorial : "))	
# def fac(num):
#     if num <= 0:
#         return 1
#     else:
#         return num * fac(num-1)
# print(fac(num))

 #2
# num = int(input("Give me a number \n"))
# factorial = 1
# if num > 0:
# 	for i in range(1,num +1):
# 		factorial = factorial * i
# 	print(factorial)	

#3


#Task_2

# print("Welcome to Magic 8 Ball!!! \n Answer these questions and I\'ll tell you what I think about it.\n If your answer is yes, print 0, if no, print 1.")

# question_1 = int(input("Will we get more snow this year than last year? " ))
# random_1 = random.randint(0,1)
# if random_1 == question_1 == 0:
# 	print("Oh, then you should buy a new coat!")
# else:
# 	print("Oh, I don\'t think so.")

# question_2 = int(input("Don\'t you want to order pizza tonight?"))
# random_2 = random.randint(0,1)
# if random_2 == question_2 == 0:
# 	print("Oh, I don\'t think so, cook for yourself!")
# else:
# 	print("Good for you!")

# question_3 = int(input("Don\'t you want a vacation?"))
# random_3 = random.randint(0,1)
# if random_3 == question_3 == 0:
# 	print("You should work harder for now !")
# else:
# 	print("Think about it.")
  
# #Task_3

# a = 0
# b = 1
# while b < 50:
# 	print(b, end=" ")
# 	a,b = b, a + b

# #Task_4

#1
# random = random.randint(0,2)
# player = False
# while player == False:
# 	player = int(input("Let\'s play Rock, Paper, Scissors! \nFor rock: 0, paper: 1, scissors: 2 \n"))
	
# 	if player == random:
# 		print("Tie!")
# 	elif player == 0:
# 		if random == 1:
# 			print("You lose, paper covers rock!")	
# 		else:
# 			print("You win, rock smashes scissors!")
# 	elif player == 1:
# 		if random == 0:
# 			print("You win, paper covers rock!")
# 		else:
# 			print("You lose, scissors cut paper!")
# 	elif player == 2:
# 		if random == 0:
# 			print("You lose, rock smashes scissors!")
# 		else:
# 			print("You win, scissors cut paper!")
# 	else:
# 		print("Please write 0,1 or 2 only.")

#2
check= "yes"
score_user = 0
score_computer = 0
round_ = 0
while check == "yes":
	user_choice = int(input("Tell me, 1 for Scissors, 2 for Paper, 3 for Rock \n"))
	computer_choice = random.randint(1,3)

	if (user_choice == 1 and computer_choice == 2) or \
	 (user_choice == 2 and computer_choice == 3) or \
	 (user_choice == 3 and computer_choice == 1 ):
	 	score_user += 1
	elif user_choice == computer_choice:
	 	print("Tie!")
	else:
	 	score_computer += 1

	round_ += 1
    check = ""
	while check != "no" :
		check = input("Do you want to play a game? yes for playing, no for ending \n")
		#print
	print("Hope you enjoyed the game \n" \
		f"your scor in {score_user}\n" \
		f"computer score is {score_computer}"\
		f"rounds {round_}")

# #Task_5

# rows = 11
# for i in range(rows):
# 	print(" "*(rows - i - 1)+ "* " * (i+1))
# for a in range(rows -1,0,-1):
# 	print(" "*(rows - a)+ "* "* a)	


