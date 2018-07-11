from BD import *
class Copa(object):

    id = None
    nombre = None


    def selectCopa(self, unID):

        BD().run("Select * from Copa Where idCopa = "+ str(unID)+";")

    def setCopa(self, nom, idOrg):

        BD().run("Insert into Copa(idCopa, Nombre, Organizacion_idOrganizacion) values (null, '"+nom+"',"+ str(idOrg)+")")

    def updateCopa(self, unID, nom, idOrg):

        BD().run("Update Copa Set Nombre = '"+nom+"', Organizacion_idOrganizacion = " +str(idOrg)+" where idCopa = "+str(unID)+";")

    def deleteCopa(self, unID):

        BD().run("Delete from Copa where idCopa = '"+str(unID)+"';")
