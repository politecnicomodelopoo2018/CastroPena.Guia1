from Persona import Persona
from BD import *

class Jugador(Persona):


    patrocinador = None
    numero = None
    posicion = None


    def crearJugador(self,nom,idn,ape,fec_nac,sal,clau,pat,num,poc,idEquipo):

        d = fec_nac.strftime('%Y-%m-%d')

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

        cursor=BD.run("Insert into Personas(idPersona, Nombre, Apellido, Dni, Equipo_idEquipo, Fecha_Nacimiento, Salario, Clausula, Patrocinador, Numero, Posicion, Tipo, Tactica_Preferida) Values(null, '"+self.nombre+"', '"+self.apellido+"', '"+str(self.dni)+"','"+str(self.idEquipoPertenece)+"','"+self.fecha_nacimiento+"','"+str(self.salario)+"','"+str(self.clausula)+"', '"+self.patrocinador+"', '"+str(self.numero)+"', '"+self.posicion+"', '"+self.__class__.__name__+"', null );")

        self.id = cursor.lastrowid


    def updateJugador(self):

        BD.run("Update Personas set Nombre = '"+self.nombre+"', Apellido = '"+self.apellido+"', Dni = '"+str(self.dni)+"', Equipo_idEquipo = '"+str(self.idEquipoPertenece)+"', Salario = '"+str(self.salario)+"', Fecha_Nacimiento = '"+self.fecha_nacimiento+"',Clausula = '"+str(self.clausula)+"', Patrocinador = '"+self.patrocinador+"', Posicion = '"+self.posicion+"', Numero = '"+str(self.numero)+"', Tipo = '"+self.__class__.__name__+"' where idPersonas = '"+str(self.id)+"'; ")


    def deleteJugador(self):

        BD.run("Delete from Personas where idPersonas = '"+str(self.id)+"' and Tipo = '"+self.__class__.__name__+"';")

    @staticmethod
    def getJugador(unID):

        d = BD.run("select * from Persona where idPersona = '" + str(unID) + "';")

        lista = d.fetchall()

        unaPersona = Jugador()

        unaPersona.id = lista[0]["id"]
        unaPersona.nombre = lista[0]["nombre"]
        unaPersona.dni = lista[0]["dni"]
        unaPersona.apellido = lista[0]["apellido"]
        unaPersona.fecha_nacimiento = lista[0]["fecha_nacimiento"]
        unaPersona.salario = lista[0]["salario"]
        unaPersona.clausula = lista[0]["clausula"]
        unaPersona.idEquipoPertenece = lista[0]["idEquipoPertenece"]
        unaPersona.patrocinador = lista[0]["patrocinador"]
        unaPersona.numero = lista[0]["numero"]
        unaPersona.posicion = lista[0]["posicion"]


        return unaPersona

    @staticmethod
    def getJugadores():

        d = BD.run("select * from Persona where Tipo = 'Jugador';")

        lista_aux = []

        for item in d:

            lista_aux.append(item)

        return lista_aux