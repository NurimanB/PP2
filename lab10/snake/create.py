import psycopg2
conn = psycopg2.connect(
	database="postgres",
	user='postgres',
	password='qwerty',
	host='localhost',
	#port= '5432'
)

conn.autocommit = True
con = conn.cursor()

sql = '''CREATE TABLE Snakedata(
   user_login VARCHAR(255) NOT NULL,
   last_score INT,
   last_level INT,
   last_FPS INT,
   snake_len INT,
   wall_len INT,
   snake_x INT,
   snake_y INT,
   record INT
);'''


con.execute(sql)
print("Database has been created successfully !!");
conn.close()