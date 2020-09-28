from rates import dollar_rate
from datetime import datetime

#Task_1 

print("Python code to Convert kilometers to Miles.")
km = float(input("Enter in kilometers  \n"))
conv_factor = 0.621371
miles = km * float(conv_factor)
print(miles, "Miles")

#Task_2

print("Money exchange app.")
dram = float(input("Enter in Dram  "))
dollar = dram / dollar_rate
print(dollar, "Dollar")

#Task_3

print("Find out when you\'ll become 100 years old !")
current_time = datetime.now()

age = int(input("Tell me your age  "))
current_year= current_time.year
the_year = current_year - age + 100
print(the_year)

#Task_4

print("Find out what\'s your optimal weight.")
height = float(input("Enter your height in meters  "))

BMI = 22
weight = 2.2 * BMI + (3.5 * BMI) * (height - 1.5)
print("Your average optimal weight in kilograms", int(weight))

#OR

print("What\'s your optimal weight considering your sex.")
height = input("Enter your height in feet(please write with tenths)   ")
height = height[::-1]
height = float(height)
first_digit = height % 10
weight_male = 52 + 1.9 * first_digit
weight_female = 49 + 1.7 * first_digit
sex = input("Enter your sex (male/female)  ")
print(sex)
if sex == "male":
	print("Your optimal weight is ", int(weight_male) ,"kilograms" )
else:
	print("Your optional weight is ", int(weight_female), "kilograms")

#Task_5

print("Sum the value of the first symbols of the given dates.")
year = input("Year  \n ")
reverse_1 = year[::-1]
year = int(year)
reverse_1 = int(reverse_1)
first_digit_1 = reverse_1 % 10

month = input("Month  \n ")
reverse_2 = month[::-1]
month = int(month)
reverse_2 = int(reverse_2)
first_digit_2 = reverse_2 % 10

day = input("Day\n ")
reverse_3 = day[::-1]
day = int(day)
reverse_3 = int(reverse_3)
first_digit_3 = reverse_3 % 10

total = first_digit_1 + first_digit_2 + first_digit_3
print(total)




#Task_6

print("Find out how many minutes have you been alive !")
#one year in minutes
one_year = 525600
#one month in minutes
one_month = 43800
#one day in minutes
one_day = 1440

year = int(input("Enter the year of your birth. \tE.g. 2000  \n "))
month = int(input("Enter the month. \tE.g. 5  \n "))
day = int(input("Enter your birth day. \tE.g.25 \n "))
minutes = year * one_year + month * one_month + day * one_day

print("You have been alive", minutes, "minutes!")














