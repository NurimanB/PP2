import csv 
import psycopg2

conn = psycopg2.connect(
    host='localhost',
    database='Phonebook',
    user='postgres',
    password='qwerty')

con = conn.cursor()
arr=[]

'''
# CSV to TABLE
with open('names.csv') as f:
    f_read = csv.reader(f, delimiter=',')

    for row in f_read:
        row[0] = int(row[0].strip(','))
        arr.append(row)


postgres_insert_query = """ INSERT INTO  phone_number VALUES (%s,%s,%s,%s) RETURNING *;"""

for i in arr:
    con.execute(postgres_insert_query, i)

conn.commit()
print("successfully !!")
conn.close()
'''


#insert entering user name, phone from console
first = str(input("Name: "))
last = str(input("Surname: "))
num = int(input("Number: "))


postgres_insert_query = """ INSERT INTO  phone_number(name, surname, number_value) VALUES (%s,%s,%s)"""
record_to_insert = (first, last, num)
con.execute(postgres_insert_query, record_to_insert)


conn.commit()
print("successfully !!");
conn.close()