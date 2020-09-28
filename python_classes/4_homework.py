#Task_1

print(" Our manu, pizza - 2000, kebab-1000,\n and we have additions: ketchup-100, mayonez-200")
main = input("Choose your main dish (enter 1 for pizza , 2 for kebab).\n")
addition = input("Choose an addition (1 for ketchup or 2 for mayonez).\n")
#we can suppose that user will input 1 or 2

pizza = "1"
pizza_p = 2000
kebab = "2"
kebab_p = 1000
ketchup = "1"
ketchup_p = 100
mayonez = "2"
mayonez_p = 200
var_1 = pizza + ketchup
var_1_p = pizza_p + ketchup_p
var_2 = pizza + mayonez
var_2_p = pizza_p + mayonez_p
var_3 = kebab + ketchup
var_3_p = kebab_p + ketchup_p
var_4 = kebab + mayonez
var_4_p = kebab_p + mayonez_p

#new changes, you should assaign the value of comparison to the variable
var_1 = var_1 == main + addition
var_2 = var_2 == main + addition
var_3 = var_3 == main + addition
var_4 = var_4 == main + addition
print("You have ordered pizza with ketchup and your price is ", var_1_p, var_1)
print("You have ordered pizza with mayonez and your price is ", var_2_p, var_2)
print("You have ordered kebab with ketchup and your price is ", var_3_p, var_3)
print("You have ordered kebab with mayonez and your price is ", var_4_p, var_4)


#Task_2

day = input("Give me a number from 0 to 6 and I\'ll tell you the matching weekday. \n")
if day == "0":
	print("Monday!")
elif day == "1":
	print("Tuesday!")
elif day =="2":
	print("Wednesday!")
elif day == "3":
	print("Thursday!")
elif day == "4":
	print("Friday!")
elif day == "5":
	print("Saturday!")
else:
	print("Sunday!")

#Task_3

talk = input("Write something and I\'ll tell you if it is a word or a word combination! \n")
if " " in talk:
	print("It\'s' a word combination.")
else:
	print("It\'s a word.")

#Task_4

string = input("Write something of at least three charecters. \n")
result = string.endswith("ing")

if len(string) < 3:
	print("It\'s less then three charecters.")
elif result:
	print(string + "ly")
else:
	print(string + "ing")









