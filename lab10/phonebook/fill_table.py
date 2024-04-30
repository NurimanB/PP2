import csv 
import psycopg2

conn = psycopg2.connect(
    host='localhost',
    database='Phonebook',
    user='postgres',
    password='qwerty')

con = conn.cursor()
arr=[]


'''# CSV to TABLE
with open('names.csv') as f:
    f_read = csv.reader(f, delimiter=',')

    for row in f_read:
        row[0] = int(row[0].strip(','))
        arr.append(row)'''




#insert entering user name, phone from console
phone_number_id = str(input("id: "))
surname = str(input("surname: "))
name = str(input("name: "))
number_value = int(input("number:"))
#(phone_number_id, name, surname, number_value)

#postgres_insert_query = """ INSERT INTO  phone_number VALUES (%s,%s,%s,%s) RETURNING *;"""
postgres_insert_query = """ INSERT INTO  phone_number(phone_number_id, name, surname, number_value) VALUES (%s,%s,%s,%s)"""
record_to_insert = (phone_number_id, name, surname, number_value)
'''for i in arr:
    con.execute(postgres_insert_query, i)
'''
for i in arr:
    con.execute(postgres_insert_query, record_to_insert)

conn.commit()
print("successfully !!")
conn.close()