from BD import *

class Organizacion(object):

    id = None
    nombre = None
    continente = None

    def __init__(self):

        self.lista_paises = []
        self.lista_copas = []




    def crearOrganizacion(self, nom, cont):

        self.nombre=nom
        self.continente=cont

    def setOrganizacion(self):

        cursor=BD().run("Insert into Organizacion (idOrganizacion, Nombre, Continente) values (null, '"+self.nombre+"','"+self.continente+"');")
        self.id=cursor.lastrowid

    def updateOrganizacion(self):

        BD().run("Update Organizacion Set Nombre = '"+self.nombre+"', Continente = '"+self.continente+"' Where idOrganizacion = '"+str(self.id)+"';")


    def deleteOrganizacion(self):

        contPais = BD().run("select count(*) from Pais where Organizacion_idOrganizacion = '"+str(self.id)+"';")
        contCopa = BD().run("select count(*) from Copa where Organizacion_idOrganizacion = '"+str(self.id)+"';")

        cont1 = None
        cont2= None

        for item in contCopa:

            cont1 = item["count(*)"]

            break

        for item in contPais:

            cont2 = item["count(*)"]

            break



        if(cont1 == 0 and cont2 == 0):

            BD().run("Delete from Organizacion Where idOrganizacion = '"+str(self.id)+"';")

        else:

            print("No se puede eliminar porque esta asociado a una tabla")

    @staticmethod
    def getOrganizacion(unID):

        d=BD().run("select * from Organizacion Where idOrganizacion = '"+str(unID)+"';")
        lista = d.fetchall()
        unaOrg=Organizacion()


        unaOrg.id = lista[0]["idOrganizacion"]
        unaOrg.nombre= lista[0]["Nombre"]
        unaOrg.continente=lista[0]["Continente"]
        return unaOrg

    @staticmethod
    def getOrganizaciones():

        d=BD().run("select * from Organizacion;")

        lista_aux=[]

        for item in d:

            lista_aux.append(item)

        return lista_aux









