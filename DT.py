from Persona import Persona
from BD import *
from datetime import *

class DT(Persona):

    tactica_preferida = None

    def crearDT(self,nom,idn,ape,fec_nac,sal,clau,tact, idEquipo):

        d = datetime.strptime(fec_nac, "%Y-%m-%d").date()

        self.nombre=nom
        self.dni=idn
        self.apellido=ape
        self.fecha_nacimiento=d
        self.salario=sal
        self.clausula=clau
        self.tactica_preferida=tact
        self.idEquipoPertenece=idEquipo

    def setDT(self):

        cursor=BD().run("Insert Into Persona(idPersona, Nombre, Apellido, Tipo, Dni, Equipo_idEquipo, Salario, Clausula, Tactica_Preferida, Fecha_Nacimiento, Posicion, Numero, Patrocinador) values(null,'"+self.nombre+"', '"+self.apellido+"', 'DT', '"+str(self.dni)+"', '"+str(self.idEquipoPertenece)+"', '"+str(self.salario)+"', '"+str(self.clausula)+"', '"+self.tactica_preferida+"','"+str(self.fecha_nacimiento)+"',null,null,null);")

        self.id = cursor.lastrowid

    def updateDT(self):

        BD().run("Update Persona set Nombre ='"+self.nombre+"', Apellido = '"+self.apellido+"', Tipo = 'DT', Dni= '"+str(self.dni)+"', Equipo_idEquipo = '"+str(self.idEquipoPertenece)+"', Salario = '"+str(self.salario)+"', Clausula = '"+str(self.clausula)+"', Tactica_Preferida = '"+self.tactica_preferida+"', Fecha_Nacimiento = '"+str(self.fecha_nacimiento)+"' Where idPersona = '"+str(self.id)+"';")

    def deleteDT(self):

        BD().run("Delete from Persona where idPersona = '"+str(self.id)+"';")


    @staticmethod
    def getDT(unID):

        d=BD().run("select * from Persona where idPersona = '"+str(unID)+"';")

        lista=d.fetchall()

        unaPersona=DT()


        unaPersona.id = lista[0]["idPersona"]
        unaPersona.nombre = lista[0]["Nombre"]
        unaPersona.dni = lista[0]["Dni"]
        unaPersona.apellido = lista[0]["Apellido"]
        unaPersona.fecha_nacimiento = lista[0]["Fecha_Nacimiento"]
        unaPersona.salario = lista[0]["Salario"]
        unaPersona.clausula = lista[0]["Clausula"]
        unaPersona.tactica_preferida = lista[0]["Tactica_Preferida"]
        unaPersona.idEquipoPertenece = lista[0]["Equipo_idEquipo"]


        return unaPersona

    @staticmethod
    def getDTs():

        d = BD().run("select * from Persona where Tipo = 'DT';")

        lista_aux = []

        for item in d:

            lista_aux.append(item)

        return lista_aux
