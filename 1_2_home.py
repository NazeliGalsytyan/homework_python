import random

print("Let\'s play 'cows and bulls' !!!")
num_1 = str(random.randint(1000,9999))
cows = 0
guesses = 0

while cows < 4:
	user_num = str(input("Try to guess the number between 1000 and 9999. \n"))
	if int(user_num) < 1000 or int(user_num)> 9999:
		print("You are not playing by the rules!")
	else:
		cows = 0
		bulls = 0

		for i in user_num:
			if num_1.find(i):
				if user_num.find(i) == num_1.find(i):
					cows += 1
				else:
					cows += 1	
		print(f"Your score is cows: {cows},bulls: {bulls}")	
		guesses += 1
	
print(f"your score is cows: {cows},bulls: {bulls}, and you have tried to guess {guesses} times!")	