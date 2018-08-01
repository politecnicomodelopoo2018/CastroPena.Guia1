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
import datetime

query = "Insert into Organizacion(idOrganizacion, Nombre, Continente) values (Null, 'CONMEBOL', 'America del Sur'),(Null, 'UEFA', 'Europa');"

BD().setConnection("127.0.0.1","root","alumno","mydb", True, "utf8")
#BD().run(query)

Org = Organizacion()

#Org.setOrganizacion("CONCACAF", "No se donde es")

#Org.updateOrganizacion(5,"CONCACAF","Africa")

#Org.deleteOrganizacion(2)


#print(Org.getOrganizacion(1))

Countraia = Pais()

#Countraia.setPais("Mongolandia", 1)
#Countraia.setPais("DarioDownlandia",1)

#Countraia.modifPais(1,"Mogolicolandia",1)

#Countraia.selectPais(1)
#Countraia.selectPais(2)

Copa = Copa()

#Copa.setCopa("Libertadores",1)
#Copa.setCopa("Sudamericana",1)


#Countraia.deletePais(7)

#Copa.deleteCopa(2)

Ligue = Liga()

#Ligue.setLiga("Liga BBVA", 1)

#Ligue.updateLiga(1, "Liga Santander", 1)

#ArgJr = Equipo()


sasrasa=Organizacion.getOrganizaciones()
sasrasa[2].nombre="otra cosa"
sasrasa[2].updateOrganizacion()

d = datetime.datetime(2000,10,10)

print (d)

f = d.strftime('%Y/%m/%d')

b = d.strftime('%Y-%m-%d')

print(f)

print(b)


#ArgJr.setEquipo("Argentinos Juniors", 1, datetime.datetime(1999,10,10))

#ArgJr.setEquipo("FC Barcelona",2,datetime.datetime(1980,1,22))

#ArgJr.updateEquipo(2,"Real Madera", 1, datetime.datetime(2000,10,24))





