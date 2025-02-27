import oracledb
from models import hospital as model


class ServiceOracleHospitales:
    def __init__(self):
        self.conn = oracledb.connect(
            user="system",
            password="oracle",
            dsn="localhost:1521/xe"
        )

    def getAllHospitales(self):
        sql = """
            select hospital_cod, nombre, direccion, telefono, num_cama
            from hospital
            order by 1
        """
        cursor = self.conn.cursor()
        cursor.execute(sql)
        datos = []
        for idHospital, nombre, direccion, telefono, numCamas in cursor:
            hospital = model.Hospital()
            hospital.idHospital = idHospital
            hospital.nombre = nombre
            hospital.direccion = direccion
            hospital.telefono = telefono
            hospital.numeroCamas = numCamas
            datos.append(hospital)
        cursor.close()
        return datos
