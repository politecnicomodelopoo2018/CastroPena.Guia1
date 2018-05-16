from EJ8 import *

unaRadio=Radio()

def agregarPersona(nom,ape,dni,ocu, fec):

    UnaPers = Personas()
    UnaPers.nombre = nom
    UnaPers.apellido=ape
    UnaPers.DNI=dni
    UnaPers.ocupacion=ocu
    UnaPers.fecha_ingreso=fec




def crearHorario(day, hour):

    unHorario=Horarios()

    unHorario.dia=day
    unHorario.hora=hour

def crearPrograma(nom,nro_con,ope_tec,cat):



    if cat == "Musica":

        unProgMusical=CategoriaMusica()

        unProgMusical.nombre_prog=nom
        unProgMusical.nro_conductores=nro_con
        unProgMusical.operador_tecnico=ope_tec
        unProgMusical.categoria=cat

        unMusicalizador =  Personas()

        unMusicalizador.nombre= input("Ingrese Nombre: ")
        unMusicalizador.apellido = input("Ingrese Apellido: ")
        unMusicalizador.DNI = input("Ingrese DNI: ")
        unMusicalizador.fecha_ingreso = input("Ingrese Fecha Ingreso: ")
        unMusicalizador.ocupacion = "Musicalizador"

        for item in range(nro_con):
            unProgMusical.lista_personas.append(
                agregarPersona(input("Ingrese Nombre: "), input("Ingrese Apellido: "), input("Ingrese DNI: "),
                               input("Ingrese Fecha Ingreso: "), input("Ingrese su ocupacion: ")))

        unProgMusical.lista_horarios.append(crearHorario(input("Ingrese un dia: "), input("Ingrese un horario: " )))
        unProgMusical.lista_personas.append(unMusicalizador)

        nro_estilos = None

        for item in range(nro_estilos):

            unProgMusical.lista_estilos.append(input("Ingrese un estilo de musica: "))


    else:

        unProg = Programas()

        unProg.nombre_prog = nom
        unProg.nro_conductores = nro_con
        unProg.operador_tecnico = ope_tec
        unProg.categoria = cat

        for item in range(nro_con):
            unProg.lista_personas.append(
                agregarPersona(input("Ingrese Nombre: "), input("Ingrese Apellido: "), input("Ingrese DNI: "),
                               input("Ingrese Fecha Ingreso: "), input("Ingrese su ocupacion: ")))

def agregarProgramaALista(Prog):

    unaRadio.lista_programas.append(Prog)
















