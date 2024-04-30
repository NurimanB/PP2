#Implement deleting data from tables by username of phone
import psycopg2

conn = psycopg2.connect(
	database="Phonebook",
	user='postgres',
	password='qwerty',
	host='localhost',
	#port='5432'
)
con = conn.cursor()
conn.autocommit = True


#looking with the first and last name
first_old = str(input("First_old: "))
last_old = str(input("Last_old: "))

sql = f"select * from phone_number where name =\'{first_old}\' and surname = \'{last_old}\' "
con.execute(sql)
info = con.fetchall()


if len(info) > 0:
    sql_update = f"Delete from phone_number where  name =\'{first_old}\' and surname = \'{last_old}\'; " 
    con.execute(sql_update)
    print("successfully !!");
else:
    print("this people name is not in phonebook")


conn.commit()

conn.close()