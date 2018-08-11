from BD import *
from datetime import *

class Equipo(object):

    id = None
    nombre = None
    fecha_creacion = None
    idLigaFK = None


    def __init__(self):

        self.lista_personas = []

    def crearEquipo(self,nom,fec, idLigue):


        d=datetime.strptime(fec, "%Y-%m-%d").date()

        self.nombre=nom
        self.fecha_creacion=d
        self.idLigaFK=idLigue


    def setEquipo(self):

        cursor=BD().run("insert into Equipo (idEquipo, Nombre, Liga_idLiga, Fecha_Creacion) values (null, '"+self.nombre+"', '"+str(self.idLigaFK)+"','"+str(self.fecha_creacion)+"');")
        self.id=cursor.lastrowid


    def updateEquipo(self):

        BD().run("update Equipo set Nombre = '"+self.nombre+"', Liga_idLiga = '"+str(self.idLigaFK)+"', Fecha_Creacion = '"+str(self.fecha_creacion)+"' where idEquipo = '"+str(self.id)+"';")

    def deleteEquipo(self):

        contPersonas = BD().run("Select count(*) from Persona where Equipo_idEquipo = '" + str(self.id) + "';")

        cont1 = None

        for item in contPersonas:
            cont1 = item["count(*)"]


        if(cont1 == 0):

            BD().run("delete from Equipo where idEquipo = '"+str(self.id)+"';")

        else:

            print("No se puede eliminar porque tiene Personas asociadas al equipo")


    @staticmethod
    def getEquipo(unID):

        d=BD().run("select * from Equipo where idEquipo = '"+str(unID)+"';")
        lista=d.fetchall()
        unEquipo= Equipo()

        unEquipo.id = lista[0]["idEquipo"]
        unEquipo.nombre= lista[0]["Nombre"]
        unEquipo.fecha_creacion= lista[0]["Fecha_Creacion"]
        unEquipo.idLigaFK = lista[0]["Liga_idLiga"]

        return unEquipo

    @staticmethod
    def getEquipos():

        d=BD().run("Select * from Equipo;")

        lista_aux = []

        for item in d:

            lista_aux.append(item)

        return lista_aux