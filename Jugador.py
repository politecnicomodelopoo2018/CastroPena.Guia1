from Persona import Persona
from BD import *
from datetime import *

class Jugador(Persona):


    patrocinador = None
    numero = None
    posicion = None


    def crearJugador(self,nom,idn,ape,fec_nac,sal,clau,pat,num,poc,idEquipo):

        d = datetime.strptime(fec_nac, "%Y-%m-%d").date()

        self.nombre=nom
        self.dni=idn
        self.apellido=ape
        self.fecha_nacimiento=d
        self.salario=sal
        self.clausula=clau
        self.patrocinador = pat
        self.numero = num
        self.posicion = poc
        self.idEquipoPertenece = idEquipo


    def setJugador(self):

        cursor = BD().run("Insert Into Persona(idPersona, Nombre, Apellido, Tipo, Dni, Equipo_idEquipo, Salario, Clausula, Tactica_Preferida, Fecha_Nacimiento, Posicion, Numero, Patrocinador) values(null,'" + self.nombre + "', '" + self.apellido + "', 'Jugador', '" + str(self.dni) + "', '" + str(self.idEquipoPertenece) + "', '" + str(self.salario) + "', '" + str(self.clausula) + "', null,'" + str(self.fecha_nacimiento) + "','"+self.posicion+"','"+str(self.numero)+"','"+self.patrocinador+"');")

        self.id = cursor.lastrowid


    def updateJugador(self):

        BD().run("Update Persona set Nombre = '"+self.nombre+"', Apellido = '"+self.apellido+"', Dni = '"+str(self.dni)+"', Equipo_idEquipo = '"+str(self.idEquipoPertenece)+"', Salario = '"+str(self.salario)+"', Fecha_Nacimiento = '"+str(self.fecha_nacimiento)+"',Clausula = '"+str(self.clausula)+"', Patrocinador = '"+self.patrocinador+"', Posicion = '"+self.posicion+"', Numero = '"+str(self.numero)+"', Tipo = 'Jugador' where idPersona = '"+str(self.id)+"';")


    def deleteJugador(self):

        BD().run("Delete from Persona where idPersona = '"+str(self.id)+"' and Tipo = 'Jugador';")

    @staticmethod
    def getJugador(unID):

        d = BD().run("select * from Persona where idPersona = '" + str(unID) + "'and Tipo = 'Jugador';")

        lista = d.fetchall()

        unaPersona = Jugador()

        unaPersona.id = lista[0]["idPersona"]
        unaPersona.nombre = lista[0]["Nombre"]
        unaPersona.dni = lista[0]["Dni"]
        unaPersona.apellido = lista[0]["Apellido"]
        unaPersona.fecha_nacimiento = lista[0]["Fecha_Nacimiento"]
        unaPersona.salario = lista[0]["Salario"]
        unaPersona.clausula = lista[0]["Clausula"]
        unaPersona.idEquipoPertenece = lista[0]["Equipo_idEquipo"]
        unaPersona.patrocinador = lista[0]["Patrocinador"]
        unaPersona.numero = lista[0]["Numero"]
        unaPersona.posicion = lista[0]["Posicion"]


        return unaPersona

    @staticmethod
    def getJugadores():

        d = BD().run("select * from Persona where Tipo = 'Jugador';")

        lista_aux = []

        for item in d:

            lista_aux.append(item)

        return lista_aux