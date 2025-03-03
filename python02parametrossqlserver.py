import pyodbc

conn = pyodbc.connect('DRIVER={ODBC Driver 18 for SQL Server};'
                      'SERVER=localhost;'
                      'DATABASE=hospital;UID=sa;PWD=Getafe12345@@;'
                      'TrustServerCertificate=yes')

sql = """
    select * from EMP
    where SALARIO >= ?
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
