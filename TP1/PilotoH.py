from Persona import Persona

class Piloto(Persona):

    def __init__(self):

        self.lista_aviones = []


    def crearPiloto(self,dni2,nom,ape,fec):

        self.nombre = nom
        self.apellido = ape
        self.fecha_nacimiento = fec
        self.dni = dni2

    def agregarAvionALista(self,UnAvion):

        if UnAvion not in self.lista_aviones:

            self.lista_aviones.append(UnAvion)