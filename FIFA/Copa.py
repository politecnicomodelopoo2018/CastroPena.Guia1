from BD import *
class Copa(object):

    id = None
    nombre = None
    IDOrgPertenecer= None


    def crearCopa(self,nom,org):

        self.nombre=nom
        self.OrgPertenecer=org


    def setCopa(self):

        cursor=BD().run("Insert into Copa(idCopa, Nombre, Organizacion_idOrganizacion) values (null, '"+self.nombre+"',"+ str(self.IDOrgPertenecer)+")")
        self.id = cursor.lastrowid


    def updateCopa(self):

        BD().run("Update Copa Set Nombre = '"+self.nombre+"', Organizacion_idOrganizacion = " +str(self.IDOrgPertenecer)+" where idCopa = "+str(self.id)+";")

    def deleteCopa(self):

        BD().run("Delete from Copa where idCopa = '"+str(self.id)+"';")



    @staticmethod
    def getCopa(cls, unID):

        d=BD().run("Select * from Copa Where idCopa = " + str(unID) + ";")
        lista = d.fetchall()
        UnaCopa=Copa()

        UnaCopa.nombre=lista[0]["nombre"]
        UnaCopa.IDOrgPertenecer=lista[0]["IDOrgPertenecer"]

        return UnaCopa

    @staticmethod
    def getCopas(cls):

        d=BD().run("Select * from Copa")

        lista_aux=[]

        for item in d:

            lista_aux.append(item)

