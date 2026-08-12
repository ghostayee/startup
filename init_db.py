import psycopg2

conn = psycopg2.connect(
    database="startup_db",
    host="localhost",
    port="5432",
    user="postgres",
    password="Ford6000$$$...",
)

cur = conn.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS courses (id serial PRIMARY KEY, name VARCHAR(100), fees integer, duration integer);''')

cur.execute(
    """INSERT INTO courses (name, fees, duration) values('python',6500,45), ('java',7000,60), ('javascript',6000,30);"""
)


conn.commit()
cur.close()
conn.close()