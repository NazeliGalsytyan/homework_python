from functions import triangle, reverse, upper_lower, palindrome 

#Task_1

triangle(10,14)	
print(triangle.__doc__)
print(triangle.__annotations__)

#Task_2

user = input("Print somethong and I\'ll print it in reverse! \n")
reverse(user)
print(reverse.__doc__)	
print(reverse.__annotations__)

#Task_3
user = input("Say something and I\'ll calculate the number of\nupper case and lower case letters! \n")
upper_lower(user)
print(upper_lower.__doc__)
print(upper_lower.__annotations__)

#Task_4
user = input("Say somethong and I\'ll check if that\'s palindrome or not! \n")
palindrome(user)
print(palindrome.__doc__)
print(palindrome.__annotations__)


