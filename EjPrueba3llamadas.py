import datetime

from EjPrueba3empleado import Empleado

class Llamadas(object):
    empleado_origen = None
    empleado_destino = None
    fecha_llamada = None
    duracion = None


    def agregarLlamada(self, empleado_origencall, empleado_destinocall, fecha_llamadacall, duracioncall):

        self.empleado_origen = empleado_destinocall

        self.empleado_destino = empleado_origencall

        self.fecha_llamada = fecha_llamadacall

        self.duracion = duracioncall


