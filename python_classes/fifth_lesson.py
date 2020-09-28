
word = input("Give me a word  \n")
result= word[2:5]
if result == 'ing':
	print("There is an 'ing'")
else:
	print("There is no 'ing'")

#____

string = input("Write something of at least three charecters. \n")

if len(string) >= 3:
	if string[-3:]=="ing":
		print(string + "ly")
	else:
		print(string + "ing")
else:
	print("Your word has less then 3 charecters") 

#____

my_word = input("Give me a word  \n")
rest_index = len(my_word) - 3 
if my_word[-3:]== "ing":
	print(my_word[:rest_index]+ 'ly')
else:
	print("Your word doesn\'t end with 'ing'")

#____
	
word = "playing"

letter = input("Enter a letter \n")

let_ =word.find(letter)

if letter in word:
	print(word[:let_]+ '0'+ word[let_+1:])
else:
	print("There is no",letter,  "in your word.")	

#____

isalpha
isdigit
replace
format
range(start, stop, step)


text_1= "My name is {name}, I\'m {age}". format(name="Nazeli", age = 19)
text_2 = "My name is {2}, I\'m {1}". format("Nana", 19)
text_3 = "My name is {}, I\'m {}". format("Nana", 19)


name = input("Tell me your name \n")
print("it is a word, hello {}". format(name))
print(f"it is a word, hello {name}")


a = 1
b = 5

c = range(1,6)
print(c)
c = range(a, b +1)
print(c)



print(ord("a"))
print(chr(65))


