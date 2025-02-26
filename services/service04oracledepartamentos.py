# Importamos la librería oracledb
import oracledb
from models import departamento


class ServiceOracleDepartamentos:
    def __init__(self):
        self.conn = oracledb.connect(
                user="system",
                password="oracle",
                dsn="localhost:1521/xe"
            )

    def insertarDepartamento(self, numero, nombre, localidad):
        sql = """
            insert into dept
                (dept_no, dnombre, loc)
            values
                (:p1, :p2, :p3)
        """
        cursor = self.conn.cursor()
        cursor.execute(sql, (numero, nombre, localidad))
        registros = cursor.rowcount
        self.conn.commit()
        cursor.close()
        return registros

    def buscarDepartamento(self, numero):
        sql = """
            select dept_no, dnombre, loc
            from dept
            where dept_no = :p1
        """
        cursor = self.conn.cursor()
        cursor.execute(sql, (numero,))
        row = cursor.fetchone()
        cursor.close()
        depto = departamento.Departamento()
        depto.numero = row[0]
        depto.nombre = row[1]
        depto.localidad = row[2]
        return depto

    def eliminarDepartamento(self, numero):
        sql = """
            delete from dept 
            where dept_no = :p1
        """
        cursor = self.conn.cursor()
        cursor.execute(sql, (numero,))
        registros = cursor.rowcount
        cursor.close()
        self.conn.commit()
        return registros
