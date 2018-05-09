from Ejercicio4empresa import Empresa


emp = Empresa()
a = Empleado()
a.nombre = 'Pepe'
a.apellido = 'Snow'
a.fecha_nacimiento = datetime(1995,10,24)
a.telefono = '1234-1234'

emp.agregarEmpleadoALista(a)


