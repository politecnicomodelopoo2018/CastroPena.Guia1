from Persona import Persona
import json


class Pasajero(Persona):

    vip = None
    solicitudesEspeciales = None


    def crearPasajero(self, dni2, nom, ape, fec_nac, vip2, solesp):

        self.nombre=nom
        self.apellido=ape
        self.dni=dni2
        self.fecha_nacimiento=fec_nac
        self.vip=vip2
        self.solicitudesEspeciales=solesp








