class Radio(object):

    def __init__(self):

        self.lista_programas = []


class Programas(object):

    nombre_prog= None

    nro_conductores= None

    operador_tecnico = None

    categoria = None

    def __init__(self):

        self.lista_personas = []

        self.lista_horarios = []

class Horarios(object):

    dia = None

    hora = None




class CategoriaMusica(Programas):

    musicalizador = None

    def __init__(self):

        self.lista_estilos = []


class Personas(object):

    nombre = None

    apellido= None

    DNI = None

    ocupacion = None

    fecha_ingreso = None

