from BD import *

class Organizacion(object):

    id = None
    nombre = None
    continente = None

    def __init__(self):

        self.lista_paises = []
        self.lista_copas = []


    def setOrganizacion(self, nom, cont):

        BD().run("Insert into Organizacion (idOrganizacion, Nombre, Continente) values (null, '"+nom+"', '"+cont+"');")

    def updateOrganizacion(self,unID, nuevoNom, nuevoCont):

        BD().run("Update Organizacion Set Nombre = '"+nuevoNom+"', Continente = '"+nuevoCont+"' Where idOrganizacion = "+str(unID)+";")


    def deleteOrganizacion(self,unID):

        BD().run("Delete from Organizacion Where idOrganizacion = "+str(unID)+";")

    def getOrganizacion(self, unID):

        d=BD().run("select * from Organizacion Where idOrganizacion = "+str(unID)+";")

        unaOrg=Organizacion()

        unaOrg.nombre= d[0]["nombre"]
        unaOrg.continente=d[0]["continente"]







