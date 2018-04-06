import datetime

from EjPrueba3llamadas import Llamadas

class Empleado(object):
    nombre = None
    apellido = None
    dni = None
    pais = None
    numero_telefono = None

    def __init__(self):

        self.lista_llamadas = []


    def agregarEmpleado(self,nombreemp,apellidoemp,dniemp,paisemp,numero_telefonoemp):

        self.nombre = nombreemp

        self.apellido = apellidoemp

        self.dni = dniemp

        self.pais = paisemp

        self.numero_telefono = numero_telefonoemp

    def realizarLlamada(self, origenEmpleado, destinoEmpleado, minutos):

        a = Llamadas()

        a.agregarLlamada(origenEmpleado, destinoEmpleado, datetime.now,minutos)


    def agregarLlamadaALista(self,unaLlam):

        self.lista_llamadas.append(unaLlam)


    def averiguarDuracionesAlExterior(self):





