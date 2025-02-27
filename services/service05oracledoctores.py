from models import doctor as model
import oracledb


class ServiceOracleDoctores:
    def __init__(self):
        self.conn = oracledb.connect(
            user="system",
            password="oracle",
            dsn="localhost:1521/xe"
        )

    def getAllDoctores(self):
        sql = """
            select hospital_cod, doctor_no, apellido, especialidad, salario
            from doctor
            order by doctor_no
        """
        cursor = self.conn.cursor()
        cursor.execute(sql)
        datos = []
        for hospId, docId, apel, espec, sal in cursor:
            doc = model.Doctor()
            doc.hospital = hospId
            doc.idDoctor = docId
            doc.apellido = apel
            doc.especialidad = espec
            doc.salario = sal
            datos.append(doc)
        cursor.close()
        return datos

    def insertarDoctor(self, idDoctor, apellido, especialidad, salario,
                       hospital):
        sql = """
            insert into doctor
                (doctor_no, apellido, especialidad, salario, hospital_cod)
            values (:p1, :p2, :p3, :p4, :p5)
        """
        cursor = self.conn.cursor()
        cursor.execute(sql,
                       (idDoctor, apellido, especialidad, salario, hospital))
        insertados = cursor.rowcount
        self.conn.commit()
        cursor.close()
        return insertados

    def eliminarDoctor(self, idDoctor):
        sql = """
            delete from doctor
            where doctor_no = :p1
        """
        cursor = self.conn.cursor()
        cursor.execute(sql, (idDoctor,))
        eliminados = cursor.rowcount
        self.conn.commit()
        cursor.close()
        return eliminados

    def modificarDoctor(self, idDoctor, apellido, especialidad,
                        salario, hospital):
        sql = """
            update doctor
            set
                apellido = :p1,
                especialidad = :p2,
                salario = :p3,
                hospital_cod = :p4
            where doctor_no = :p5
        """
        cursor = self.conn.cursor()
        cursor.execute(sql, (apellido, especialidad, salario,
                             hospital, idDoctor))
        modificados = cursor.rowcount
        self.conn.commit()
        cursor.close()
        return modificados

    def buscarDoctor(self, idDoctor):
        sql = """
            select doctor_no, apellido, especialidad, salario, 
                   hospital_cod
            from doctor
            where doctor_no = :p1
        """
        cursor = self.conn.cursor()
        cursor.execute(sql, (idDoctor,))
        doctor = model.Doctor()
        doc = cursor.fetchone()
        if doc is not None:
            doctor.idDoctor = doc[0]
            doctor.apellido = doc[1]
            doctor.especialidad = doc[2]
            doctor.salario = doc[3]
            doctor.hospital = doc[4]
            cursor.close()
            return doctor
        else:
            cursor.close()
            return None