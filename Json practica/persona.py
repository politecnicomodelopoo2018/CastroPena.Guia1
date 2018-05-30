import datetime

class Persona(object):

    nombre = None
    apellido = None
    fecha_nacimiento = None

    def __init__(self, nom, ape, fecha):

        self.nombre = nom
        self.apellido = ape
        self.fecha_nacimiento = fecha

    def senializar(self):

        d = {"nombre" : self.nombre,
             "apellido": self.apellido,
             "fecha_nacimiento": str(self.fecha_nacimiento)
             }
        #self.fecha_nacimiento.year + self.fecha_nacimiento.month +self.fecha_nacimiento.day
        return d

    def desenializar(self, UnaP):

        self.nombre = UnaP["nombre"]
        self.apellido = UnaP["apellido"]
        self.fecha_nacimiento = datetime.strptime(dict["fecha_nacimiento"],"%d%m%Y").date()



class Ciudad(object):



    def __init__(self):

        self.lista_personas = []


    def AgregarPersona(self, unPers):

        if unPers not in self.lista_personas:

            self.lista_personas.append(unPers)




