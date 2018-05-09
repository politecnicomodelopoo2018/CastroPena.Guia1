from EjPrueba2platos import Platos

class Personas(object):
    nombre=None
    fecha_nacimiento=None

    def __init__(self):
        self.lista_platos=[]

    def agregarPersona(self,nomper,fecha_nac):

        self.nombre = nomper
        self.fecha_nacimiento = fecha_nac


    def cantidadCalorias(self):

        total_calorias = 0

        for item in self.lista_platos:
            total_calorias += item.calorias

        return total_calorias

    def agregarPlatoALista(self, plato):

        self.lista_platos.append(plato)

