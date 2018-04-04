import datetime

from EJPrueba2familia import Familia
from EjPrueba2personas import Personas

Los_Andreatinis = Familia()

D = Personas()
D.agregarPersona('Dario', datetime(2000,12,14))
J = Personas()
J.agregarPersona('Juliana', datetime(2004,05,23))
G = Personas()
G.agregarPersona('Gabriel', datetime(1970,10,14))
L = Personas()
L.agregarPersona('Lorena', datetime(1975,06,06))

Los_Andreatinis.agregarPersonaAFamilia(D)
Los_Andreatinis.agregarPersonaAFamilia(J)
Los_Andreatinis.agregarPersonaAFamilia(G)
Los_Andreatinis.agregarPersonaAFamilia(L)


