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

    def agregarTripulacionALista(self, UnTripulante):

        if UnTripulante.dni not in self.lista_tripulacion:
            self.lista_tripulacion.append(UnTripulante)

    # EJERCICIO 1 Bien
    def imprimirListaPasajeros(self):

        return self.lista_pasajeros


    # EJERCICIO 2 Bien
    def PasajeroMasJoven(self):

        fecha_aux_actual = self.lista_pasajeros[0].fecha_nacimiento

        persona_aux = []

        for item in self.lista_pasajeros:

            if fecha_aux_actual == item.fecha_nacimiento:

                persona_aux.append(item)

            elif fecha_aux_actual < item.fecha_nacimiento:

                fecha_aux_actual = item.fecha_nacimiento

                del persona_aux[:]

                persona_aux.append(item)

        return persona_aux


    # EJERCICIO 3 Bien
    def verificarTripulacion(self):

        if len(self.lista_tripulacion) < self.avion.cantidadTripulacionNecesaria:

            return "El vuelo no alcanza la tripulacion minima"

        if len(self.lista_tripulacion) >= self.avion.cantidadTripulacionNecesaria:

            return "El vuelo si alcanza la tripulacion minima"

    # EJERCICIO 4 (parte 1)
    def verificarPersonasNoAutorizadas(self):

        for tripulante in self.lista_tripulacion:

                if self.avion not in tripulante.lista_aviones:

                    return 0

        return 1

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