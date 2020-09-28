#Task_1

dict1 = {1:10, 2:20}
dict2 = {3:30, 4:40}
dict3 = {5:50, 6:60}
dict4 = {6:50, 7:60}
list_dict = [dict1, dict2, dict3, dict4]

for i in list_dict:
	dict1.update(i)

print(dict1)

#Task_2

user = int(input("please enter not negative number and I\'ll create a dictionary. \n"))
dict_1 = {}
for i in range(1,user +1):
	
	dict_1[i] = i * i

print(dict_1)	

#Task_3

dict_1 = {'c1': 'Red', 'c2': 'Green', 'c3': None}

dict_1 = {key:value for (key, value) in dict_1.items() if value is not None}

print(dict_1)






