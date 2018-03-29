from Ejercicio3equipo import Equipo
from Ejercicio3Partidos import Partidos

class Torneo:
    def __init__(self):
        listaEquipos = []
        listaPosibPartidos = [[[]],[[]],[[]]]  ,  [[[]],[[]],[[]]]  ,  [[[]],[[]],[[]]]  ,  [[[]],[[]],[[]]]  ,  [[[]],[[]],[[]]]  ,  [[[]],[[]],[[]]]  ,  [[[]],[[]],[[]]]
        fixture = []


    def setEquipo(self, unEquipo):
        self.listaEquipos.append(unEquipo)

    def setPosiblesHorariosPartidos(self):
        for i in range(7):
            for j in range(3):
                for item in self.listaEquipos:
                    if item.listaHorariosQuePuede[i][j]:
                        self.listaPosibPartidos[i][j].append(item)
        for i in range(7):
            for j in range(3):
                for equi1 in self.listaPosibPartidos[i][j]:
                    for equi2 in self.listaPosibPartidos[i][j]:
                         if equi1 != equi2:
                             Match = Partidos()
                             Match.setEquipo1(equi1)
                             Match.setEquipo2(equi2)
                             Match.diaPartido(i)
                             Match.turnoPartido(j)

                             if Match not in self.fixture:
                                self.fixture.append(Match)