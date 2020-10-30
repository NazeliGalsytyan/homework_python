import logging
import random
import time

logging.basicConfig(format = '%(asctime)s: %(levelname)s: %(message)s',filename = "num_gen_issiues.log", level = logging.DEBUG )

while True :
	number = random.randint(0,50)
	question = input("If you want to see warnings in a file print 0, if not, print 1(break)\n")
	try:

		if int(question) == 0:

			if number < 10:
				logging.debug(F"The number is between 0 and 10.({number})")
			
			elif 10 <= number <= 19:				
				logging.info(F"The number is between 10 and 20.({number})")
			
			elif 20 <= number <= 29:			
				logging.warning(F"The number is between 20 and 30.({number})")
			
			elif 30 <= number <= 39:				
				logging.error(F"The number is between 30 and 40.({number})")
			
			elif 40<= number <= 50:				
				logging.critical(F"The number is between 40 and 50.({number})")

		elif int(question) == 1:
			break

	except:
		print("Something went wrong.")
					
	

						