from models.plantilla import Plantilla
import oracledb as bd

class ServicePlantilla:
    def __init__(self):
        self.conn = bd.connect(
            user="system",
            password="oracle",
            dsn="localhost:1521/xe"
        )
    
    def getPlantilla(self):
        sql = """
            select empleado_no,
                   apellido,
                   funcion,
                   salario,
                   hospital_cod
            from PLANTILLA
            order by empleado_no
        """
        cursor = self.conn.cursor()
        cursor.execute(sql)
        data: list[Plantilla] = []
        for numEmpleado, apellido, funcion, salario, hospital in cursor:
            empleado = Plantilla()
            empleado.idPlantilla = numEmpleado
            empleado.apellido = apellido
            empleado.funcion = funcion
            empleado.salario = salario
            empleado.hospital = hospital
            data.append(empleado)
        cursor.close()
        return data

    def updateSalarioPlantilla(self, incremento, hospital):
        sql = """
            update PLANTILLA
               set salario = salario + :p1
             where hospital_cod = :p2
        """
        cursor = self.conn.cursor()
        cursor.execute(sql, (incremento, hospital))
        actualizados = cursor.rowcount
        self.conn.commit()
        cursor.close()
        return actualizados
