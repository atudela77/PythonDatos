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

    def buscarHospital(self, idHospital):
        sql = """
            select hospital_cod, nombre, direccion, telefono, num_cama
            from hospital
            where hospital_cod = :p1
        """
        cursor = self.conn.cursor()
        cursor.execute(sql, (idHospital,))
        hospital = model.Hospital()
        hosp = cursor.fetchone()
        if hosp is not None:
            hospital.idHospital = hosp[0]
            hospital.nombre = hosp[1]
            hospital.direccion = hosp[2]
            hospital.telefono = hosp[3]
            hospital.numeroCamas = hosp[4]
            cursor.close()
            return hospital
        else:
            return None

    def insertarHospital(self, idHospital, nombre, direccion,
                         telefono, numCamas):
        sql = """
            insert into hospital
            (hospital_cod, nombre, direccion, telefono, num_cama)
            values
            (:p1, :p2, :p3, :p4, :p5)
        """
        cursor = self.conn.cursor()
        cursor.execute(sql,
                       (idHospital, nombre, direccion, telefono, numCamas))
        insertados = cursor.rowcount
        self.conn.commit()
        cursor.close()
        return insertados

    def modificarHospital(self, idHospital, nombre, direccion,
                          telefono, numCamas):
        sql = """
            update hospital
            set
                nombre = :p1,
                direccion = :p2,
                telefono = :p3,
                num_cama = :p4
            where hospital_cod = :p5
        """
        cursor = self.conn.cursor()
        cursor.execute(sql, (nombre, direccion, telefono,
                             numCamas, idHospital))
        modificados = cursor.rowcount
        self.conn.commit()
        cursor.close()
        return modificados

    def eliminarHospital(self, idHospital):
        sql = """
            delete from hospital
            where hospital_cod = :p1
        """
        cursor = self.conn.cursor()
        cursor.execute(sql, (idHospital,))
        eliminados = cursor.rowcount
        self.conn.commit()
        cursor.close()
        return eliminados
