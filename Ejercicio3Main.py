from Ejercicio3torneo import Torneo


Superliga = Torneo()

Superliga.setEquipo("AAAJ")

#Superliga.listaEquipos[0].nombreEquipo('Argentinos Juniors')
Superliga.listaEquipos[0].setBarrio('Paternal')
Superliga.listaEquipos[0].setJugador('A')
Superliga.listaEquipos[0].setJugador('B')
Superliga.listaEquipos[0].setJugador('C')
Superliga.listaEquipos[0].setJugador('D')
Superliga.listaEquipos[0].listaJugadores[0].setNombreJug('Lucas Barrios')
Superliga.listaEquipos[0].listaJugadores[1].setNombreJug('Damian Batallini')
Superliga.listaEquipos[0].listaJugadores[2].setNombreJug('Nicolas Gonzalez')
Superliga.listaEquipos[0].listaJugadores[3].setNombreJug('Leonardo Pisculichi')
Superliga.listaEquipos[0].nroCamiseta('Lucas Barrios', 88)

#Superliga.listaEquipos[0].listaJugadores[0].setFechaNac(datetime(1989,05,23))

Superliga.listaEquipos[0].setCapitan('Lucas Barrios')

Superliga.listaEquipos[0].HorariosQuePuede(0,0)
Superliga.listaEquipos[0].HorariosQuePuede(2,1)
Superliga.listaEquipos[0].HorariosQuePuede(4,2)



