import datetime

class Registro(object):


    fecha_registro = None
    peso = None
    altura = None

    def agregarFechaRegistro(self,fecha_reg):

        self.fecha_registro=fecha_reg

    def agregarPeso(self,weight):

        self.peso=weight

    def agregarAltura(self,height):

        self.altura=height



