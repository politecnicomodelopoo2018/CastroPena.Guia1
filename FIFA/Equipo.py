from BD import *
class Equipo(object):

    id = None
    nombre = None
    fecha_creacion = None
    idLigaFK = None


    def __init__(self):

        self.lista_personas = []

    def crearEquipo(self,nom,fec, idLigue,):

        d=fec.strftime('%Y-%m-%d')

        self.nombre=nom
        self.fecha_creacion=d
        self.idLigaFK=idLigue


    def setEquipo(self):

        cursor=BD.run("insert into Equipo (idEquipo, Nombre, Liga_idLiga, Fecha_Creacion) values (null, '"+self.nombre+"', '"+str(self.idLigaFK)+"','"+self.fecha_creacion+"');")
        self.id=cursor.lastrowid


    def updateEquipo(self):

        BD.run("update Equipo set Nombre = '"+self.nombre+"', Liga_idLiga = '"+str(self.idLigaFK)+"', Fecha_Creacion = '"+self.fecha_creacion+"' where idEquipo = '"+str(self.id)+"';")

    def deleteEquipo(self):

        BD.run("delete from Equipo where idEquipo = '"+str(self.id)+"';")


    @staticmethod
    def getEquipo(cls,unID):

        d=BD.run("select * from Equipo where idEquipo = '"+str(unID)+"';")
        lista=d.fetchall()
        unEquipo= Equipo()

        unEquipo.nombre= lista[0]["nombre"]
        unEquipo.fecha_creacion= lista[0]["fecha_creacion"]
        unEquipo.idLigaFK = lista[0]["idLigaFK"]

        return unEquipo

    @staticmethod
    def getEquipos(cls):

        d=BD.run("Select * from Equipo;")

        lista_aux = []

        for item in d:

            lista_aux.append(item)

        return lista_aux