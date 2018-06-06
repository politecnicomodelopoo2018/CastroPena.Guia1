import datetime
from PilotoH import Piloto

class Servicio(Piloto):

    def __init__(self):

        self.lista_idiomas = []

    def agregarAvionALista(self, UnAvion):

        if UnAvion.codigoUnico not in self.lista_aviones:

            self.lista_aviones.append(UnAvion)


    def crearServicio(self,nom,ape,dni2,fec):

        self.nombre = nom
        self.apellido = ape
        self.dni=dni2
        self.fecha_nacimiento=fec


    def agregarIdioma(self,UnIdioma):

        if UnIdioma not in self.lista_idiomas:

            self.lista_idiomas.append(UnIdioma)

