import pymysql as bd

conn = bd.connect(
    host="localhost",
    port=3306,
    user="getafe",
    password="mysql",
    database="hospital"
)

cursor = conn.cursor()
sql = "select * from DEPT"
cursor.execute(sql)
for row in cursor:
    print(row)
cursor.close()
conn.close()
