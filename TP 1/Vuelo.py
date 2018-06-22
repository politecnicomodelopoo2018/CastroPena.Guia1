import datetime

class Vuelo(object):

    avion = None
    fecha = None
    hora = None
    origen = None
    destino = None

    def __init__(self):

        self.lista_tripulacion = []
        self.lista_pasajeros = []

    def crearVuelo(self,UnAvion,date,hour,origin,destiny):

        self.avion=UnAvion
        self.fecha=date
        self.hora=hour
        self.origen=origin
        self.destino=destiny

    def argegarPasajeroALista(self,UnPasaj):

        if self.avion.cantidadPasajerosMaximos > len(self.lista_pasajeros):

            if UnPasaj.dni not in self.lista_pasajeros:

                self.lista_pasajeros.append(UnPasaj)

    def imprimirListaPasajeros(self):

        return self.lista_pasajeros

    def PasajeroMasJoven(self):
        print(self.lista_pasajeros)
        fecha_aux_actual = self.lista_pasajeros[0].fecha_nacimiento

        persona_aux = []

        for item in self.lista_pasajeros:

            if fecha_aux_actual == item.fecha_nacimiento:

                persona_aux.append(item)

            if fecha_aux_actual < item.fecha_nacimiento:

                persona_aux.removeall()

                persona_aux.append(item)

        return persona_aux

    def agregarTripulacionALista(self,UnTripulante):

        if UnTripulante.dni not in self.lista_tripulacion:

            self.lista_tripulacion.append(UnTripulante)


    def verificarTripulacion(self):

        if len(self.lista_tripulacion) < self.avion.cantidadTripulacionNecesaria:

            return "El vuelo no alcanza la tripulacion minima"

        if len(self.lista_tripulacion) >= self.avion.cantidadTripulacionNecesaria:

            return "El vuelo si alcanza la tripulacion minima"


    def verificarPersonasNoAutorizadas(self):

        for item in self.lista_tripulacion:

            if self.avion.codigoUnico not in item.lista_aviones:

                return '1'


        return '0'



    def PersonasVIPoEspeciales(self):

        lista_personasVoE = []

        for item in self.lista_pasajeros:

            if item.vip == 1 or item.solicitudesEspeciales != None:

                lista_personasVoE.append(item)



    def IdiomasHabladosPorVuelo(self):

        lista_idiomaPorVuelo = []

        for item in self.lista_tripulacion:

            if item.__name__ == 'Servicio':

                for idioma in item.lista_idiomas:

                    if idioma not in lista_idiomaPorVuelo:

                        lista_idiomaPorVuelo.append(idioma)


        return lista_idiomaPorVuelo