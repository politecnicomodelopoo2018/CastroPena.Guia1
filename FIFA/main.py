from Organizacion import *
from Copa import *
from Pais import *
from Liga import *
from Equipo import *
from Persona import *
from Jugador import *
from DT import *
from BD import *
import pymysql

query = "Insert into Organizacion(idOrganizacion, Nombre, Continente) values (Null, 'CONMEBOL', 'America del Sur'),(Null, 'UEFA', 'Europa');"

BD().setConnection("127.0.0.1","root","alumno","mydb", True, "utf8")
#BD().run(query)

Org = Organizacion()

#Org.setOrganizacion("CONCACAF", "No se donde es")

#Org.updateOrganizacion(5,"CONCACAF","Africa")

#Org.deleteOrganizacion(13)


print(Org.getOrganizacion(1))