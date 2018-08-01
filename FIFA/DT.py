from Persona import Persona
from BD import *

class DT(Persona):

    tactica_preferida = None

    def crearDT(self,nom,idn,ape,fec_nac,sal,clau,tact):

        self.nombre=nom
        self.dni=idn
        self.apellido=ape
        self.fecha_nacimiento=fec_nac
        self.salario=sal
        self.clausula=clau
        self.tactica_preferida=tact

    def setDT(self):

        cursor=BD().run("Insert Into Persona(idPersona, Nombre, Apellido, Tipo, Dni, Equipo_idEquipo, Salario, Clausula, Tactica_Preferida) values(null,'"+self.nombre+"', '"+self.apellido+"', '"+self.__class__.__name__+"', '"+str(self.dni)+"', '"+self.idEquipoPertenece+"', '"+str(self.salario)+"', '"+str(self.clausula)+"', '"+self.tactica_preferida+"');")

        self.id = cursor.lastrowid

    def updateDT(self):

        BD().run("Update Persona set Nombre ='"+self.nombre+"', Apellido = '"+self.apellido+"', Tipo = '"+self.__class__.__name__+"', Dni= '"+str(self.Dni)+"', Equipo_idEquipo = '"+self.idEquipoPertenece+"', Salario = '"+str(self.salario)+"', Clausula = '"+str(self.clausula)+"', Tactica_Preferida = '"+self.tactica_preferida+"' Where idPersona = '"+str(self.id)+"';")

    def deleteDT(self):

        BD().run("Delete from Persona where idPersona = '"+str(self.id)+"';")


    @staticmethod
    def getDT(cls,unID):

        d=BD.run("select * from Persona where idPersona = '"+str(unID)+"';")

        lista=d.fetchall()

        unaPersona=DT()


        unaPersona.id = lista[0]["id"]
        unaPersona.nombre = lista[0]["nombre"]
        unaPersona.dni = lista[0]["dni"]
        unaPersona.apellido = lista[0]["apellido"]
        unaPersona.fecha_nacimiento = lista[0]["fecha_nacimiento"]
        unaPersona.salario = lista[0]["salario"]
        unaPersona.clausula = lista[0]["clausula"]
        unaPersona.tactica_preferida = lista[0]["tactica_preferida"]
        unaPersona.idEquipoPertenece = lista[0]["idEquipoPertenece"]


        return unaPersona

    @staticmethod
    def getDTs(cls):

        d = BD.run("select * from Persona where Tipo = 'DT'")

        lista_aux = []

        for item in d:

            lista_aux.append(item)

        return lista_aux
