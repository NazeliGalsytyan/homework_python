#Task_1

for i in range(10):
	print(str(i) * i)

#Task_2

string = input("Enter something and I\'ll give you the number of digits in it. \n")
b = 0
for i in string:
	if i.isdigit():
		b += 1
print("The number of digits is ", b)		
		
#Task_3

for i in range(10):
	if i == 0:
		print(i) 
	else:
		i += i -1
		print(i)

#Task_4

string = input("Enter something and I\'ll print only even index number characters. \n")
for i in range(len(string)):
	if i % 2 == 0:
		print(string [i], end="")


#Task_5	

the_list = []
number = int(input("\nEnter any number and I\'ll tell your all the divisors. \n"))
for i in range(1, number + 1):
	if number % i == 0:
		divide = number / i 
		the_list.append(i)
print("These are all the divisors. ",the_list)		

