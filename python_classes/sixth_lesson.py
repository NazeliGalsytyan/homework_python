
for i in "Hello World":
	print(i)


a = int(input("Give me a number \n"))

for i in range (1,11):
	print("{} * {} == {}".format(a, i, a*i ))




a = input("Enter the current year \n")
b = 0
for i in a:
	b+= int(i)

print(b)



a = input("Enter somthing \n")
b = 0

for i in a:
	if i.isdigit():
		b += int(i)
print(b)



a = 0
for i in range(1,21):
	if i % 3 == 0:
		continue
	else:
		a += int(i)

print(a)



a = 0
for i in range (1,21):
	a += int(i)

b =0
for i in range(1,21):
	if i % 3 == 0:
		b += int(i)
	else:
		continue	

print ( a - b)



a = 0
for i in range (1,21):
	
	if a >= 15:
		break
	else:
		a += int(i)	
print(a)		


a = 0
for i in range (1,21):
	a += int(i)	
	if a > 15:
		break
	

if 15- a-i > a  -15:
	print(a)
else:
	print(a- i)	


	 

















