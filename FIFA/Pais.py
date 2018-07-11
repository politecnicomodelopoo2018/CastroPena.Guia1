import pymysql
from BD import *

class Pais(object):

    id = None
    nombre = None

    def __init__(self):

        self.lista_ligas = []


    def selectPais(self, unID):

        BD().run("Select * from Pais where idPais = " + str(unID) + ";" )


    def setPais(self, nom, idOrg):

        BD().run("Insert into Pais (idPais, Nombre, Organizacion_idOrganizacion) values (null, '" + nom + "', '"+ str(idOrg) +"');")

    def modifPais(self, unID, nom, idOrg):

        BD().run("Update Pais set Nombre = '"+nom+"' , Organizacion_idOrganizacion = "+str(idOrg)+" where idPais = "+str(unID)+";")


    def deletePais(self, unID):

        BD().run("Delete from Pais Where idPais ="+str(unID)+";" )

