import pymysql as bd

conn = bd.connect(
    host="localhost",
    port=3306,
    user="getafe",
    password="mysql",
    database="hospital"
)

cursor = conn.cursor()
sql = "select * from EMP"
cursor.execute(sql)
for row in cursor:
    print(f"Apellido: {row[1]}, Oficio: {row[2]}")
cursor.close()
conn.close()
