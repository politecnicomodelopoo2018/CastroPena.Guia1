from  Ejercicio3jugadores import Jugadores

class Equipo:
    nombre_equipo = None
    barrio = None
    capitan = None

    def __init__(self,nombre_equipo):
        self.nombre_equipo = nombre_equipo
        self.listaJugadores = []
        self.listaHorariosQuePuede = [[False,False,False],[False,False,False],[False,False,False],[False,False,False],[False,False,False],[False,False,False],[False,False,False]]


    #def nombreEquipo(self,nombreEquip):
     #   self.nombre_equipo = nombreEquip

    def setBarrio(self, nombreBarrio):
        self.barrio = nombreBarrio

    def setJugador(self, jugador):
        self.listaJugadores.append(jugador)

    def setCapitan(self, nombreJug):
        for item in self.listaJugadores:
            if item.nombre_Jug == nombreJug:
                self.capitan = item.nombre_Jug

    def HorariosQuePuede(self, dia , turno):
        self.listaHorariosPorDia[dia][turno] = True


    def nroCamiseta(self, nombreJug, nro):
        for item in self.listaJugadores:
            if item.nombre_Jug == nombreJug:
                item.nro_camiseta = nro