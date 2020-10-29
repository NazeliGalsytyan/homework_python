import threading
import requests
import json

with open("images.json", "r") as file:
	data = json.load(file)

image_names = ["image_1", "image_2", "image_3", "image_4", "image_5", "image_6", "image_7", "image_8", "image_9", "image_10"]	

def threading_image():

	for image in data["items"]:	
		image_url = requests.get(image["url"])
		#print(image_url.url)
		for i in range(len(image_names)):
			img = image_names[i]

			if image_url.url.endswith("jpg"):
				with open(img + ".jpg", "wb") as file_1:
					file_1.write(image_url.content)

			elif image_url.url.endswith("png"):
				with open(img + ".png", "wb") as file_2:
					file_2.write(image_url.content)

			else:
				pass		


threading_image()

# thread_list = []	
# for i in range(9):
# 	x = threading.Thread(target = threading_image)
# 	thread_list.append(x)
# 	x.start()






