from Persona import Persona
from BD import *

class Jugador(Persona):


    patrocinador = None
    numero = None
    posicion = None


    def crearDT(self,nom,idn,ape,fec_nac,sal,clau,pat,num,poc):

        self.nombre=nom
        self.dni=idn
        self.apellido=ape
        self.fecha_nacimiento=fec_nac
        self.salario=sal
        self.clausula=clau
        self.patrocinador = pat
        self.numero = num
        self.posicion = poc
