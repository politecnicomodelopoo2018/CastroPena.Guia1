from Sistema import Sistema
from Persona import Persona
from Vuelo import Vuelo
from Avion import Avion
from PasajeroH import Pasajero
from PilotoH import Piloto
from ServicioH import Servicio


A = Sistema()

A.cargarArchivoPersona('datos.json')
A.cargarArchivoAvion('datos.json')
A.cargarArchivoVuelo('datos.json')

#print (A.lista_personas)
#print (A.lista_aviones)
#print (A.lista_vuelos)

A.VueloNoAutorizado()

A.TripulanteRepiteDias()