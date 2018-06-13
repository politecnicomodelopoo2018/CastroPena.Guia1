from Avion import Avion
from Vuelo import Vuelo
from Persona import Persona

class Sistema(object):

    def __init__(self):

        self.lista_personas = []
        self.lista_aviones = []
        self.lista_vuelos = []



    def agregarPersonaALista(self,UnaPers):

        if UnaPers.dni not in self.lista_personas:

            self.lista_personas.append(UnaPers)

    def agregarAvionALista(self,UnAvion):

        if UnAvion.codigoUnico not in self.lista_aviones:

            self.lista_aviones.append(UnAvion)

    def agregarVueloALista(self,UnVuelo):

        if UnVuelo.avion and UnVuelo.fecha not in self.lista_vuelos:

            self.lista_vuelos.append(UnVuelo)


    def VueloNoAutorizado(self):

        lista_aux=[]

        for item in self.lista_vuelos:

            if item.verificarPersonasNoAutorizadas() == 1:

                lista_aux.append(item)

        return lista_aux

    def FechasAux(self):

        lista_aux=[]

        for item in self.lista_vuelos:

            lista_aux.append(item.fecha)

        return lista_aux

    def TripulanteRepiteDias(self):

        lista_fechas = self.FechasAux()

        lista_aux = []

        lista_rompedoresDeLey = []

        for fecha in lista_fechas:

            for vuelo in self.lista_vuelos:

                if vuelo.fecha == fecha:

                    for tripu in vuelo.lista_tripulacion:

                        if tripu in lista_aux:

                                lista_rompedoresDeLey.append(tripu)
                        else:

                            lista_aux.append(tripu)


            lista_aux.clear()


        return lista_rompedoresDeLey

