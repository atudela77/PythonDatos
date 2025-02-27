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
        if (row is not None):
            depto = departamento.Departamento()
            depto.numero = row[0]
            depto.nombre = row[1]
            depto.localidad = row[2]
            return depto
        return None

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

    def modificarDepartamento(self, numero, nombre, localidad):
        sql = """
            update dept
            set dnombre = :p1,
                loc = :p2
            where dept_no = :p3
        """
        cursor = self.conn.cursor()
        cursor.execute(sql, (nombre, localidad, numero))
        registros = cursor.rowcount
        self.conn.commit()
        cursor.close()
        return registros

    def getAllDepartamentos(self):
        sql = """
            select dept_no, dnombre, loc
            from dept
            order by dept_no
        """
        cursor = self.conn.cursor()
        cursor.execute(sql)
        # Creamos una lista vacía para guardar los distintos objetos
        datos = []
        # Recorremos el cursor con el resultado de la consulta
        for row in cursor:
            # Creamos un objeto por cada "vuelta" en la misma variable
            dept = departamento.Departamento()
            # Asignamos los valores recogidos a las variables del objeto
            dept.numero = row[0]
            dept.nombre = row[1]
            dept.localidad = row[2]
            # Añadimos el objeto a la lista
            datos.append(dept)
        cursor.close()
        return datos
