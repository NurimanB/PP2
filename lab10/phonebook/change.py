import psycopg2
import csv


conn = psycopg2.connect(
    host='localhost',
    database='Phonebook',
    user='postgres',
    password='qwerty')

con = conn.cursor()
conn.autocommit = True

pre_name = str(input("Previous name: "))
pre_surname = str(input("Previous surname: "))
pre_phone = str(input("Previous phone number: "))

smt = f"select * from Phonebook where name =\'{pre_name}\' and surname = \'{pre_surname}\' and phone_value = \'{pre_phone}\' "
con.execute(smt)
info = con.fetchall()

if len(info) > 0:
    new_name = str(input("new_name: "))
    new_surname = str(input("new_surname: "))
    new_phone = int(input("new_number: "))
    sql_update = f"Update Phonebook set phone_num =\'{new_phone}\', first_name =\'{new_name}\', last_name =\'{new_surname}\' where first_name =\'{pre_name}\' and last_name = \'{pre_surname}\'; " 
    con.execute(sql_update)
    print("successfully !!");
else:
    print("this people name is not in phonebook")


conn.commit()

conn.close()
