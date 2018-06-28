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


print("\nEJERCICIO 1:")

for item in A.lista_vuelos[2].imprimirListaPasajeros():

    print (item.nombre , item.fecha_nacimiento)

print("\n--------------------------------")

print("\nEJERCICIO 2:")

for item in A.lista_vuelos[2].PasajeroMasJoven():

    print(item.nombre)

print("\n--------------------------------")

print("\nEJERCICIO 3:")

print(A.lista_vuelos[0].verificarTripulacion())

print("\n--------------------------------")

print("\nEJERCICIO 4:")

for item in A.VueloNoAutorizado():

    print(item.avion.codigoUnico + " " + item.destino)

print("\n--------------------------------")

print("\nEJERCICIO 5:")

for item in A.TripulanteRepiteDias():

    print(item.dni)

print("\n--------------------------------")

print("\nEJERCICIO 6:")

for item in A.lista_vuelos[1].PersonasVIPoEspeciales():

     print(item.nombre + " " + item.dni)

print("\n--------------------------------")

print("\nEJERCICIO 7:")

for item in A.lista_vuelos[3].IdiomasHabladosPorVuelo():

    print(item)

print("\n--------------------------------")
