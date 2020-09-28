# my_input = input("Tell me something  ")
# print(my_input)
#import math
from datetime import datetime


#p = 3.14

# the_r = float(input("Enter the r  "))
# area = math.pi * the_r**2
# print(area)

# my_name = input("Enter your name  \n")
# my_surename = input("Enter your surename  \n")

# print("Hi",my_surename,my_name)

#import variables
#print("today's date is", variables.year, variables.month, variables.day, sep ="\n")
#if the file is in another folder.
# from (folder_name).variables import (the_file)

current_time = datetime.now()
#print("today's date is", current_time)

age = int(input("Tell me your age  "))
# the_answer = 100 - age
# print(the_answer)
current_year= current_time.year
# the_year = int(current_year) + int(the_answer)
# print(the_year)

the_year = current_year - age + 100
print(the_year)







