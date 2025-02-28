import pyodbc

conn = pyodbc.connect('DRIVER={ODBC Driver 18 for SQL Server};SERVER=localhost;DATABASE=hospital;UID=sa;PWD=Getafe12345@@;TrustServerCertificate=yes')
cursor = conn.cursor()
sql = "select * from DEPT"
cursor.execute(sql)
for row in cursor:
    print(row)
cursor.close()
conn.close()
