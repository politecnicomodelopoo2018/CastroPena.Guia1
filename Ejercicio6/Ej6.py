class Empresa:

    def __init__(self):

        self.lista_autos=[]
        self.lista_camioneta=[]

class Vehiculos(object):
    patente=None
    cant_ruedas=None
    año_fabricacion=None


class Camioneta(Vehiculos):

    capacidad_carga = 0

    def __init__(self, pat, ruedas, año_fab,carga):
        self.patente = pat

        self.cant_ruedas = ruedas

        self.año_fabricacion = año_fab

        self.capacidad_carga = carga

class Auto(Vehiculos):

    descapotable = None

    def __init__(self, pat, ruedas, año_fab,desc):

        self.patente = pat

        self.cant_ruedas = ruedas

        self.año_fabricacion = año_fab

        self.descapotable=desc


