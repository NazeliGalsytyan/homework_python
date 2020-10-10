import random
#Task_1

class NewDict:
	def __init__(self,string_):
		self.dict_1 = {}

		for key in string_:
			self.dict_1[key] = random.randint(1,2)

	def rem_dub(self):
		d = {}
		for i in self.dict_1:
			if self.dict_1[i] not in d.values():
				d[i] = self.dict_1[i]

		self.dict_1 = d	

	def max_3(self):
		
		list_1 = list(self.dict_1.values())
		list_1.sort(reverse = True)

		return list_1[:3]

dict_new = NewDict("python")

print(dict_new.dict_1)
print(dict_new.max_3())

print("after removing dublcates")
dict_new.rem_dub()
print(dict_new.max_3())





