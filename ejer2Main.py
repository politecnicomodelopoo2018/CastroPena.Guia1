import datetime

from EJPrueba2familia import Familia
from EjPrueba2personas import Personas
from EjPrueba2platos import Platos

Los_Andreatinis = Familia("Andreatinis")

D = Personas()
D.agregarPersona('Dario', datetime.date(2000,12,14))
J = Personas()
J.agregarPersona('Juliana', datetime.date(2004,5,23))
G = Personas()
G.agregarPersona('Gabriel', datetime.date(1970,10,14))
L = Personas()
L.agregarPersona('Lorena', datetime.date(1975,6,6))

Los_Andreatinis.agregarPersonaAFamilia(D)
Los_Andreatinis.agregarPersonaAFamilia(J)
Los_Andreatinis.agregarPersonaAFamilia(G)
Los_Andreatinis.agregarPersonaAFamilia(L)

PlatoUno = Platos()

PlatoDos = Platos()

PlatoTres = Platos()

PlatoUno.agregarPlato('Fideos', 100)

PlatoDos.agregarPlato('Milanga', 350)

PlatoTres.agregarPlato('Triple Mac', 600)

D.agregarPlatoALista(PlatoTres)
D.agregarPlatoALista(PlatoTres)
D.agregarPlatoALista(PlatoDos)
D.agregarPlatoALista(PlatoTres)


J.agregarPlatoALista(PlatoUno)
J.agregarPlatoALista(PlatoUno)
J.agregarPlatoALista(PlatoUno)
J.agregarPlatoALista(PlatoDos)


G.agregarPlatoALista(PlatoDos)
G.agregarPlatoALista(PlatoUno)
G.agregarPlatoALista(PlatoDos)
G.agregarPlatoALista(PlatoTres)

L.agregarPlatoALista(PlatoDos)
L.agregarPlatoALista(PlatoTres)
L.agregarPlatoALista(PlatoUno)
L.agregarPlatoALista(PlatoUno)


print(D.nombre, " consumio: ", D.cantidadCalorias(), " calorias")
print(J.nombre, " consumio: ",J.cantidadCalorias(), " calorias")
print(G.nombre, " consumio: ",G.cantidadCalorias(), " calorias")
print(L.nombre, " consumio: ",L.cantidadCalorias(), " calorias")



print("Promedio de calorias consumidas por la familia ", Los_Andreatinis.nomb_flia ,": ",Los_Andreatinis.promedioCaloriasFamilia())
print("El que consumio mas calorias ingirio: ",Los_Andreatinis.maxCalorias())
print("El que consumio menos calorias ingirio: ",Los_Andreatinis.minCalorias())






