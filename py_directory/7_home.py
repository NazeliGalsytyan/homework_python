import os

base_dir = os.getcwd()

print("Now we are here {}!".format(base_dir))
print(os.listdir())

os.makedirs("/Users/Apple/Desktop/homework_python/py_directory/Dir1/Dir2")
print("We have created folder 'Dir1' and folder 'Dir2' in it.")
os.chdir("/Users/Apple/Desktop/homework_python/py_directory/Dir1")
print(os.listdir())

os.makedirs("/Users/Apple/Desktop/homework_python/py_directory/Dir1/Dir3/Dir4")
print("Now we have created 'Dir3' in 'Dir1'")
os.chdir("/Users/Apple/Desktop/homework_python/py_directory/Dir1")
print(os.listdir())

print("And 'Dir4' in 'Dir3'.")
os.chdir("/Users/Apple/Desktop/homework_python/py_directory/Dir1/Dir3")
print(os.listdir())

question = int(input("Do you want to delete all this folers?(if yes, print 0).\n"))

if question == 0:
	os.rmdir("/Users/Apple/Desktop/homework_python/py_directory/Dir1/Dir3/Dir4")
	os.rmdir("/Users/Apple/Desktop/homework_python/py_directory/Dir1/Dir3")
	os.rmdir("/Users/Apple/Desktop/homework_python/py_directory/Dir1/Dir2")
	os.remove("/Users/Apple/Desktop/homework_python/py_directory/Dir1")

	if os.path.exists("config.txt"):
		os.remove("config.txt")

else:
	pass

os.chdir("/Users/Apple/Desktop/homework_python/py_directory")
print(os.listdir())

