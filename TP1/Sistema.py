from Avion import Avion
from Vuelo import Vuelo
from Persona import Persona
from PasajeroH import Pasajero
from PilotoH import Piloto
from ServicioH import Servicio

from datetime import datetime
import json

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


    # EJERCICIO 4 (Parte 1) Bien
    def VueloNoAutorizado(self):

        lista_aux=[]

        for item in self.lista_vuelos:

            if item.verificarPersonasNoAutorizadas() == 0:

                lista_aux.append(item)

        return lista_aux

    # EJERCICIO 5 (Parte 1) Bien
    def FechasAux(self):

        lista_aux=[]

        for item in self.lista_vuelos:

            lista_aux.append(item.fecha)

        return lista_aux

    # EJERCICIO 5 (Parte 2) Bien
    def TripulanteRepiteDias(self):

        lista_fechas = self.FechasAux() #lista_fechas almacena todas las fechas en la q hay vuelos

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
            break

            del lista_aux[:]

        return lista_rompedoresDeLey



    def cargarArchivoAvion(self, archivo):

        f = open(archivo, 'r')

        diccionario = json.loads(f.read())

        for avion in diccionario['Aviones']:

            Av = Avion()

            Av.crearAvion(avion['codigoUnico'], avion['cantidadDePasajerosMaxima'], avion['cantidadDeTripulacionNecesaria'])

            self.agregarAvionALista(Av)

    def cargarArchivoVuelo(self, archivo):

        f = open(archivo, 'r')

        diccionario = json.loads(f.read())

        avioncitoAux = None

        for vuelo in diccionario['Vuelos']:

            Vue = Vuelo()

            for aviones in self.lista_aviones:

                if aviones.codigoUnico == vuelo['avion']:

                    avioncitoAux = aviones



            Vue.crearVuelo(avioncitoAux, datetime.strptime(vuelo['fecha'], '%Y-%m-%d').date(), vuelo['hora'], vuelo['origen'], vuelo['destino'])




            for tripu in vuelo['tripulacion']:

                for tripu2 in self.lista_personas:

                    if tripu2.__class__.__name__ == 'Piloto' or tripu2.__class__.__name__ == 'Servicio':

                        if tripu == tripu2.dni:

                            Vue.agregarTripulacionALista(tripu2)

            for pasajer in vuelo['pasajeros']:

                for persona in self.lista_personas:

                    if persona.__class__.__name__ == 'Pasajero':

                        if pasajer == persona.dni:

                            Vue.argegarPasajeroALista(persona)

            self.agregarVueloALista(Vue)

    def cargarArchivoPersona(self, archivo):


        f = open(archivo, 'r')

        diccionario = json.loads(f.read())

        for persona in diccionario['Personas']:

            if persona['tipo'] == 'Pasajero':

                Pasaj = Pasajero()

                if persona['vip'] == 1:

                    vipAux = True

                elif persona['vip'] == 0:

                    vipAux = False

                solicitudAux= ''

                try:

                    solicitudAux = persona['solicitudesEspeciales']

                except:

                    pass

                Pasaj.crearPasajero(persona['dni'],persona['nombre'],persona['apellido'], datetime.strptime(persona['fechaNacimiento'], '%Y-%m-%d').date(), vipAux, solicitudAux)

                self.agregarPersonaALista(Pasaj)

            if persona['tipo'] == 'Piloto':

                Pilot = Piloto()

                Pilot.crearPiloto(persona['dni'],persona['nombre'],persona['apellido'],datetime.strptime(persona['fechaNacimiento'],'%Y-%m-%d').date())

                for codAv in persona['avionesHabilitados']:

                    for aviones in self.lista_aviones:

                        if codAv == aviones.codigoUnico:

                            Pilot.agregarAvionALista(aviones)

                self.agregarPersonaALista(Pilot)


            if persona['tipo'] == 'Servicio':

                Service = Servicio()

                Service.crearServicio(persona['nombre'], persona['apellido'], persona['dni'], datetime.strptime(persona['fechaNacimiento'], '%Y-%m-%d').date())

                for codAv in persona['avionesHabilitados']:

                    for aviones in self.lista_aviones:

                        if codAv == aviones.codigoUnico:

                            Service.agregarAvionALista(aviones)


                for idiom in persona['idiomas']:

                    Service.agregarIdioma(idiom)


                self.agregarPersonaALista(Service)
