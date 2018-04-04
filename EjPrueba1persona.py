from EjPrueba1registro import Registro

import datetime

class Persona(object):
    nombre=None
    apellido=None
    fecha_nacimiento=None

    def __init__(self):
        self.lista_registros=[]

    def agregarNombre(self,nom):

        self.nombre=nom

    def agregarApellido(self,ape):

        self.apellido=ape

    def agregarFechaNacimiento(self, fecha_nac):

        self.fecha_nacimiento=fecha_nac

    def agregarRegistro(self,unReg):

        self.lista_registros.append(unReg)


    def averiguarRegistro(self,day):

        for item in self.lista_registros:
            if item.fecha_registro == day:
                return item.peso, item.altura, day


    def PromedioPesoAlturaEnAño(self, year):
        cont_peso = 0
        cont_alt = 0
        cantidad = 0

        for item in self.lista_registros:
            if item.fecha_registro.year() == year:
                cont_peso += item.peso
                cont_alt +=  item.altura
                cantidad += 1

        cont_peso = cont_peso / cantidad
        cont_alt = cont_alt / cantidad

        return cont_peso, cont_peso



    def PorcentajeCrecimiento(self,year):

        altura1=0
        altura2=0

        for item in self.lista_registros:
            if item.fecha_registro.year() == year:
                altura1=item.altura
                break
        for item2 in self.lista_registros:
            if item2.fecha_registro.year() == year+1:
                altura2= item2.altura
                break

        return altura1 * 100 / altura2













