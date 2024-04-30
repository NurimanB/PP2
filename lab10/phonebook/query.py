#Querying data from the tables (with different filters)
import psycopg2

conn = psycopg2.connect(
	database="Phonebook",
	user='postgres',
	password='qwerty',
	host='localhost',
	#port='5432'
)
cursor = conn.cursor()
conn.autocommit = True

#select all
#sql = f"select * from phonebook";

#select filter 
sql = f"select * from phone_number where name = \'Sasha\' ";


#select with sort filter decrease by first
#sql = f"select * from phone_number by order by name desc";


#select with sort filter increase by first
#sql = f"select * from phon_number by order by name asc";


cursor.execute(sql)
info = cursor.fetchall()
print(info)