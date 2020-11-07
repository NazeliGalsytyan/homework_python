import sqlite3
from sqlite3 import Error
import os
import json

datebase = os.path.join(os.getcwd(), "film.db")
try:
	conn = sqlite3.connect(datebase)
except Error as e:
	print(e)

curs = conn.cursor()

##------------------------------------------
select_title_query = """ SELECT title
					FROM film
					WHERE title LIKE 'B%'
					
					"""

curs.execute(select_title_query)
print(curs.fetchall())
conn.commit()					

##-------------------------------------------

select_length_query = """SELECT MAX(length)
						 FROM film
					 
						 """

curs.execute(select_length_query)
print(curs.fetchall())
conn.commit()

##--------------------------------------------
## DO RESEARCH

def get_all_films(json_str = False):
	conn.row_factory = sqlite3.Row

	rows = curs.execute( """ SELECT * FROM film

						""").fetchall()

	conn.commit()

	if json_str:
		with open ("sqlite.json", "w") as json_file:
			json.dump(rows, json_file)	

	return rows	

get_all_films(json_str= True)

##--------------------------------------------
new_table = """CREATE TABLE IF NOT EXISTS filtered_film (
			film_id int,
			title text,
			description text,
			release_year smallint,
			rate real,
			length smallint,
			special_features text

			);
			"""

curs.execute(new_table)
conn.commit()
conn.close()

new_query = """ INSERT INTO filtered_film (film_id, title, description, release_year, rate, length, special_features)
				SELECT *
				FROM film
				WHERE release_year > 2010
				AND  (rate >= 3)
				"""

curs.execute(new_query)
print(curs.fetchall())
conn.commit()	
conn.close()			




