class Fecha(object):

    dia = None
    mes = None
    año = None

    def crearFecha(self, day, month, year, datetime):

        self.dia = day
        self.mes = month
        self.año = year
        self.dia = datetime.day
        self.mes = datetime.month
        self.año = datetime.year



        return


class Persona(object):

    nombre = None
    apellido = None
    fecha_nacimiento = None

    def __init__(self, nom, ape, fecha):

        self.nombre = nom
        self.apellido = ape
        self.fecha_nacimiento = fecha


class Ciudad(object):



    def __init__(self):

        self.lista_personas = []


    def AgregarPersona(self, unPers):

        if unPers not in self.lista_personas:

            self.lista_personas.append(unPers)

    def JSON(self):

        diccionario = {"Persona": []}

        for item in self.lista_personas:

            diccionario["Persona"].append({"Nombre" : item.nombre,
                                           "Apellido" : item.apellido,
                                           "Fecha Nacimiento" : item.fecha_nacimiento
                                           })



