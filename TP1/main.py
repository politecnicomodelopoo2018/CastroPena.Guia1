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


print("\n1) Nomina de personas por vuelo:\n")

for item in A.lista_vuelos:

    print(item.origen + "-" + item.destino + " :")

    for item2 in item.imprimirListaPasajeros():

        print(item2.nombre + " " + item2.apellido)

    print("\n")


print("\n--------------------------------")

print("\n2) Pasajero mas joven por vuelo:\n")

for item in A.lista_vuelos:

    print(item.origen + "-" + item.destino + " :")

    for item2 in item.PasajeroMasJoven():

        print(item2.nombre + " " + item2.apellido)

    print("\n")


print("\n--------------------------------")

print("\n3) Vuelos en los cuales no se alcance la tripulacion minima:\n")

for item in A.lista_vuelos:

    print(item.origen + "-" + item.destino + " :\n" + item.verificarTripulacion() + "\n")



print("\n--------------------------------")

print("\n4) Vuelos tripulados por personas no autorizadas:\n")

for item in A.VueloNoAutorizado():

    print(item.avion.codigoUnico + " " + item.destino)

print("\n--------------------------------")

print("\n5) Estableciendo la regla de que la tripulacion no puede volar mas de una vez al dia mostrar un listado de los tripulantes que rompen dicha regla:\n")

for item in A.TripulanteRepiteDias():

    for rompedores in item["rompedores"]:

        print(rompedores.dni + " " + rompedores.nombre + " " + rompedores.apellido)


print("\n--------------------------------")

print("\n6) Personas VIP o con necesidades especiales por vuelo:\n")

for item in A.lista_vuelos:

    print(item.origen + "-" + item.destino + " :\n")

    for item2 in item.PersonasVIPoEspeciales():

         print(item2.dni + " " + item2.nombre + " " + item2.apellido)

    print ("\n")

print("\n--------------------------------")

print("\n7) Idiomas hablados por la tripulacion en cada vuelo:")

for item in A.lista_vuelos:

    print(item.origen + "-" + item.destino + " :\n")

    for item2 in item.IdiomasHabladosPorVuelo():

        print(item2)

    print ("\n")

print("\n--------------------------------")
