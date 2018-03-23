from  Ejercicio3jugadores import Jugadores

class Equipo(object):
    nombre = None
    capitan = None

    def __init__(self):
        lista_jugadores = []
        lista_horarios = []

    def agregarNombre(self,nom):
        self.nombre = nom

    def definirCapitan(self,nombreJug):
        for i in self.lista_jugadores:
            if i.nombre ==  nombreJug:
                capitan = i.nombre


