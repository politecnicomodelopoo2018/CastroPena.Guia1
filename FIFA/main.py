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

#Org.deleteOrganizacion(2)


#print(Org.getOrganizacion(1))

Countraia = Pais()

Countraia.setPais("Mongolandia", 1)
#Countraia.setPais("DarioDownlandia",1)

#Countraia.modifPais(1,"Mogolicolandia",1)

#Countraia.selectPais(1)
#Countraia.selectPais(2)

Copa = Copa()

#Copa.setCopa("Libertadores",1)
#Copa.setCopa("Sudamericana",1)


Countraia.deletePais(7)

#Copa.deleteCopa(2)

Ligue = Liga()

Ligue.setLiga("Liga BBVA", 11)

Ligue.updateLiga(1, "Liga Santander", 12)


