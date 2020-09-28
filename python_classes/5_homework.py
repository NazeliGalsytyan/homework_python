#Task_1

year = int(input("Enter a year and I\'l tell you if it\'s a leap year or not. \n"))

if year % 4 == 0:  
   if year % 100 == 0:  
       if year % 400 == 0:  
           print("{0} is a leap year!".format(year))  
       else:  
           print("{0} is not a leap year!".format(year))  
   else:  
       print("{0} is a leap year!".format(year))  
else:  
   print("{0} is not a leap year!".format(year))  

#Task_2

number = int(input("Enter a number and I\'ll tell you if it\'s divisible by 5 or 11 or not.\n"))

if number % 5 == 0:
	if number % 11 == 0:
		print("{0} is divisible both by 5 and 11!". format(number))
	else:
		print("{0} is divisible by 5!". format(number))
elif number % 11 == 0:
	print("{0} is divisible by 11!". format(number))
else:
	print("{0} isn\'t divisible by 5 or 11!". format(number))

#Task_3

number = int(input("Enter a number and I\'ll tell you if it\'s divisible by 3 or 5 or both, otherwise I\'ll return your number.' \n"))

if number % 3 == 0:
	if number % 5 == 0:
		print("FizzBuzz")
	else:	 
		print("Fizz")
elif number % 5 == 0:
	print("Buzz")
else:
	print(number)	

#Task_4

def not_poor(string):
  s_not = string.find('not')
  s_poor = string.find('poor')
  
  if s_poor > s_not and s_poor > 0 and s_not > 0:
    string = string.replace(string[s_not:(s_poor+4)], "good")
    return string
  else:
    return string

print(not_poor("The lyrics is not that poor!"))
print(not_poor("The lyrics is poor!"))

#Task_5

string = "restart"
save = string[0]
string = string.replace(save, '$')
string = save + string[1:]

print(string)



