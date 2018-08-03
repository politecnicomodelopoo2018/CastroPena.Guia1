import pymysql
from BD import *

class Pais(object):

    id = None
    nombre = None
    IDOrgPertenecer = None

    def __init__(self):

        self.lista_ligas = []

    def crearPais(self,nom, org):

        self.nombre=nom
        self.OrgPertenecer=org


    def setPais(self):

        cursor=BD().run("Insert into Pais (idPais, Nombre, Organizacion_idOrganizacion) values (null, '" + self.nombre + "', '"+ str(self.IDOrgPertenecer) +"');")
        self.id = cursor.lastrowid

    def updatePais(self):

        BD().run("Update Pais set Nombre = '"+self.nombre+"' , Organizacion_idOrganizacion = "+str(self.IDOrgPertenecer)+" where idPais = "+str(self.id)+";")


    def deletePais(self):

        BD().run("Delete from Pais Where idPais ="+str(self.id)+";")



    @staticmethod
    def getPais(unID):

        d=BD().run("Select * from Pais where idPais = " + str(unID) + ";" )
        lista = d.fetchall()
        UnPais= Pais()
        UnPais.nombre = lista[0]["nombre"]
        UnPais.IDOrgPertenecer = lista[0]["IDOrgPertenecer"]

        return UnPais

    @staticmethod
    def getPaises():

        d=BD.run("Select * from Pais")

        lista_aux = []

        for item in d:

            lista_aux.append(item)

        return lista_aux