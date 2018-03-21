from Ejercicio4empleado import Empleado

class Empresa(object):
    nombre_enpresa = None

    def __init__(self):
        lista_empleados = []
        lista_porcent_empleados = []


    def agregarEmpleadoALista(self, unEmp):
        self.lista_empleados.append(unEmp)
    def agregarPorcentajEmp(self,año,mes):
        x = Empleado()
        self.lista_porcent_empleados.append(x.porcentajeAsistencia(año,mes))
        sum(self.lista_porcent_empleados) / len(self.lista_porcent_empleados)

    def porcentajeAsistenciaEmpresarial(self,año,mes):
        suma_porcentajes=0
        for item in self.lista_empleados:
            suma_porcentajes+=item.porcentajeAsistencia(año,mes)
        porcentajeEmpresarial=suma_porcentajes/len(self.lista_empleados) * 100
        return porcentajeEmpresarial





