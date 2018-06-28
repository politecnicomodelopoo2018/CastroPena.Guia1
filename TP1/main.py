from Sistema import Sistema
from Persona import Persona
from Vuelo import Vuelo
from Avion import Avion
from PasajeroH import Pasajero
from PilotoH import Piloto
from ServicioH import Servicio


A = Sistema()
A.cargarArchivoAvion('datos.json')
A.cargarArchivoPersona('datos.json')
A.cargarArchivoVuelo('datos.json')



#print (A.lista_personas)
#print (A.lista_aviones)
#print (A.lista_vuelos)

print("\n--------------------------------")


print("\n1) Nomina de personas por vuelo:")

for item in A.lista_vuelos[2].imprimirListaPasajeros():

    print (item.nombre , item.fecha_nacimiento)

print("\n--------------------------------")

print("\n2) Pasajero mas joven por vuelo:")

for item in A.lista_vuelos[2].PasajeroMasJoven():

    print(item.nombre)

print("\n--------------------------------")

print("\n3) Vuelos en los cuales no se alcance la tripulacion minima:")

print(A.lista_vuelos[0].verificarTripulacion())

print("\n--------------------------------")

print("\n4) Vuelos tripulados por personas no autorizadas:")

for item in A.VueloNoAutorizado():

    print(item.avion.codigoUnico + " " + item.destino)

print("\n--------------------------------")

print("\n5) Estableciendo la regla de que la tripulación no puede volar mas de una vez al dia mostrar un listado de los tripulantes que rompen dicha regla:")

for item in A.TripulanteRepiteDias():

    print(item.dni)

print("\n--------------------------------")

print("\n6) Personas VIP o con necesidades especiales por vuelo:")

for item in A.lista_vuelos[1].PersonasVIPoEspeciales():

     print(item.nombre + " " + item.dni)

print("\n--------------------------------")

print("\n7) Idiomas hablados por la tripulacion en cada vuelo:")

for item in A.lista_vuelos[3].IdiomasHabladosPorVuelo():

    print(item)

print("\n--------------------------------")
