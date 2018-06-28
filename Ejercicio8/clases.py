class Radio(object):

    def __init__(self):

        self.lista_programas = []


class Programa(object):

    nombre = None
    operador_tecnico = None
    categoria = None

    def __init__(self):

        self.lista_conductores = []

        self.lista_horario = []


class Categoria(object):

    nombre = None

    def __init__(self, name):

        self.nombre = name


class Musica(Categoria):

    musicalizador = None
    estilo = None

    def __init__(self,name, dj, style):

        Categoria.__init__(self, name)
        self.musicalizador = dj
        self.estilo = style


class Horario(object):

    dia = None
    hora = None

    def __init__(self, day, hour):

        self.dia = day
        self.hora = hour



class Persona(object):

    idPersona = None
    nombre = None
    apellido = None
    dni = None
    fecha_ingreso = None


class Musicalizadores(Persona):

    def __init__(self, id, name, lastname, dni, fecha_ing):

        Persona.__init__(self)

        self.idPersona = id
        self.nombre = name
        self.apellido = lastname
        self.dni = dni
        self.fecha_ingreso = fecha_ing


class OperadoresTecnicos(Persona):

    def __init__(self, id, name, lastname, dni, fecha_ing):

        Persona.__init__(self)

        self.idPersona = id
        self.nombre = name
        self.apellido = lastname
        self.dni = dni
        self.fecha_ingreso = fecha_ing

class Conductores(Persona):



    def crearConductor(self):

        id = input('Id del conductor: ')
        name = input('Nombre del conductor: ')
        lastname  = input('Apellido del conductor: ')
        dni = input('Dni del conductor: ')
        fecha_ing = input('Fecha de ingreso del conductor')

        Conductor = Conductores(id, name, lastname, dni, fecha_ing)






    def __init__(self, id, name, lastname, dni, fecha_ing):

        Persona.__init__(self)

        self.idPersona = id
        self.nombre = name
        self.apellido = lastname
        self.dni = dni
        self.fecha_ingreso = fecha_ing



