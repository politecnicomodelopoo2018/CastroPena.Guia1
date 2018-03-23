from Ejercicio4empleado import Empleado

class Empresa(object):
    nombre_enpresa = None

    def __init__(self):
        lista_empleados = []


    def agregarEmpleadoALista(self, unEmp):
        self.lista_empleados.append(unEmp)

    def porcentajeAsistenciaEmpresarial(self,año,mes):
        suma_porcentajes=0
        for item in self.lista_empleados:
            suma_porcentajes+=item.porcentajeAsistencia(año,mes)
        porcentajeEmpresarial=suma_porcentajes/len(self.lista_empleados) * 100
        return porcentajeEmpresarial





