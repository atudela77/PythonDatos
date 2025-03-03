import pymysql as bd

conn = bd.connect(
    host="localhost",
    port=3306,
    user="getafe",
    password="mysql",
    database="hospital"
)
sql = """
    select * from EMP
    where SALARIO >= %s
    order by SALARIO
"""
cursor = conn.cursor()
print("Introduzca un salario: ")
salario = int(input())
cursor.execute(sql, (salario,))
for row in cursor:
    print(f"Apellido:{row[1]}, Oficio: {row[2]}, Salario: {row[5]} ")
cursor.close()
conn.close()
