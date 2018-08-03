from BD import *
class Liga(object):

    id = None
    nombre = None
    IDPaisPertenecer = None

    def __init__(self):

        self.lista_equipos=[]

    def crearLiga(self,nom,idPais):

        self.nombre=nom
        self.IDPaisPertenecer=idPais




    def setLiga(self):

        cursor=BD().run("Insert into Liga(idLiga, Nombre, Pais_idPais) values (null, '"+self.nombre+"',"+str(self.IDPaisPertenecer)+");")
        self.id = cursor.lastrowid

    def updateLiga(self):

        BD().run("Update Liga Set Nombre = '"+self.nombre+"', Pais_idPais = " +str(self.IDPaisPertenecer)+" where idLiga = "+str(self.id)+";")

    def deleteLiga(self):

        BD().run("Delete from Liga where idLiga = '"+str(self.id)+"';")


    @staticmethod
    def getLiga(unID):
        d = BD().run("Select * from Liga where idLiga = " + str(unID) + ";")
        lista = d.fetchall()
        UnLiga = Liga()
        UnLiga.nombre = lista[0]["nombre"]
        UnLiga.IDPaisPertenecer = lista[0]["IDPaisPertenecer"]

        return UnLiga

    @staticmethod
    def getLigas():

        d=BD.run("select * from Liga;")

        lista_aux=[]

        for item in d:

            lista_aux.append(item)

        return lista_aux