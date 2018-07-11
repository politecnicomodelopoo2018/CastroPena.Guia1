from BD import *
class Liga(object):

    id = None
    nombre = None

    def __init__(self):

        self.lista_equipos=[]


    def selectLiga(self, unID):

        BD().run("Select * from Liga Where idLiga = "+ str(unID)+";")

    def setLiga(self, nom, idPa):

        BD().run("Insert into Liga(idLiga, Nombre, Pais_idPais) values (null, '"+nom+"',"+str(idPa)+");")

    def updateLiga(self, unID, nom, idPa):

        BD().run("Update Liga Set Nombre = '"+nom+"', Pais_idPais = " +str(idPa)+" where idCopa = "+str(unID)+";")

    def deleteLiga(self, unID):

        BD().run("Delete from Liga where idLiga = '"+str(unID)+"';")