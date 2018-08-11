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
        self.IDOrgPertenecer=org


    def setPais(self):

        cursor=BD().run("Insert into Pais (idPais, Nombre, Organizacion_idOrganizacion) values (null, '" + self.nombre + "', '"+ str(self.IDOrgPertenecer) +"');")
        self.id = cursor.lastrowid

    def updatePais(self):

        BD().run("Update Pais set Nombre = '"+self.nombre+"' , Organizacion_idOrganizacion = '"+str(self.IDOrgPertenecer)+"' where idPais = '"+str(self.id)+"';")


    def deletePais(self):

        contLigas = BD().run("Select count(*) from Liga where Pais_idPais = '"+str(self.id)+"';")

        cont1 = None

        for item in contLigas:

            cont1 = item["count(*)"]

        if(cont1 == 0):

            BD().run("Delete from Pais Where idPais ='"+str(self.id)+"';")

        else:

            print("No se puede eliminar porque tiene Ligas asociados al Pais")

    @staticmethod
    def getPais(unID):

        d=BD().run("Select * from Pais where idPais = '" + str(unID) + "';" )
        lista = d.fetchall()
        UnPais= Pais()

        UnPais.id=lista[0]["idPais"]
        UnPais.nombre = lista[0]["Nombre"]
        UnPais.IDOrgPertenecer = lista[0]["Organizacion_idOrganizacion"]

        return UnPais

    @staticmethod
    def getPaises():

        d=BD().run("Select * from Pais;")

        lista_aux = []

        for item in d:

            lista_aux.append(item)

        return lista_aux