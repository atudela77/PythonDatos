import pymysql as bd
from models.empleado import Empleado


class ServiceBBDDEmpleados:
    def __init__(self):
        self.conn = bd.connect(
            host="localhost",
            port=3306,
            user="getafe",
            password="mysql",
            database="hospital"
        )

    def getAllEmpleados(self):
        sql = """
            select emp_no, apellido, oficio, salario
            from EMP
            order by salario
        """
        cursor = self.conn.cursor()
        cursor.execute(sql)
        # Debemos indicar el tipo de lista que estamos devolviendo
        # variable: list[TIPO DE CLASE]
        data: list[Empleado] = []
        for numEmpleado, apellido, oficio, salario in cursor:
            emp = Empleado()
            emp.idEmpleado = numEmpleado
            emp.apellido = apellido
            emp.oficio = oficio
            emp.salario = salario
            data.append(emp)
        cursor.close()
        return data

    def getAllEmpleadosSalario(self, salario):
        sql = """
            select emp_no, apellido, oficio, salario
            from EMP
            where salario >= %s
            order by salario
        """
        cursor = self.conn.cursor()
        cursor.execute(sql, (salario,))
        data: list[Empleado] = []
        for numEmpleado, apellido, oficio, salario in cursor:
            emp = Empleado()
            emp.idEmpleado = numEmpleado
            emp.apellido = apellido
            emp.oficio = oficio
            emp.salario = salario
            data.append(emp)
        cursor.close()
        print(f"desde dentro: {type(data)}")
        return data
