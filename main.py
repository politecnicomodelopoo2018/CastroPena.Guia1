from Organizacion import *
from Copa import *
from Pais import *
from Liga import *
from Equipo import *
from Persona import *
from Jugador import *
from DT import *
from BD import *
import pymysql
import datetime



BD().setConnection("127.0.0.1","root","alumno","mydb", True, "utf8")


#Org1.setOrganizacion()


#Org1.crearOrganizacion("CONCACAF","Africa")

#Org1.nombre="sasasa"
#Org1.updateOrganizacion()
#print(Organizacion.getOrganizacion(1).nombre)
#print(Organizacion.getOrganizaciones())


#CopaLeche=Copa()

#CopaLeche.crearCopa("UEFA Chanchos lig", 1)

#CopaLeche.setCopa()

#print(Copa.getCopas())

#CopaLeche.nombre="Caquita"

#CopaLeche.updateCopa()


#MENUUU


opcion = int(input("MENU\n 1-ORGANIZACIONES \n 2-COPAS \n 3-PAISES \n 4-LIGAS \n 5-EQUIPOS \n 6-JUGADOR \n 7- DTs \n 8- Salir \n OPCION: "))
ORG = Organizacion()
COPA = Copa()
PAIS = Pais()
Ligue = Liga()
Team = Equipo()
Player = Jugador()
DeTe = DT()

while(opcion != 8):


    if(opcion == 1):

        opcionOrg = int(input("1-CREAR ORGANIZACION \n 2-INSERTAR ORG EN BASE \n 3-VER ORGANIZACIONES DE LA BASE \n 4-MODIFICAR UNA ORGANIZACION \n 5-ELIMINAR UNA ORGANIZACION \n 6-VOLVER AL 1ER MENU \n OPCION: "))


        if(opcionOrg == 1):

            nombre_org = input("Escriba el nombre de la organizacion: ")

            cont_org = input("Escriba el nombre del continente de la organizacion: ")

            ORG.crearOrganizacion(nombre_org, cont_org)


        elif(opcionOrg == 2):

            ORG.setOrganizacion()

            print("La org. creada se inserto en la base")


        elif(opcionOrg == 3):

            print(Organizacion.getOrganizaciones())


        elif(opcionOrg == 4):

            ORG.updateOrganizacion()


        elif(opcionOrg == 5):

            ORG.deleteOrganizacion()

        elif(opcionOrg == 6):

            opcion = int(input("\n MENU\n 1-ORGANIZACIONES \n 2-COPAS \n 3-PAISES \n 4-LIGAS \n 5-EQUIPOS \n 6-JUGADOR \n 7- DTs \n 8- Salir \n OPCION: "))

        else:

            print("Se presiono una opcion incorrecta, vuelva a intentar\n")



    elif(opcion == 2):


        opcionCopa = int(input("\n1-CREAR COPA \n 2-INSERTAR COPA. CREADA \n 3-VER COPA DE LA BASE \n 4-MODIFICAR UNA COPA \n 5-ELIMINAR UNA COPA \n 6-VOLVER AL 1ER MENU \n OPCION: "))

        if(opcionCopa == 1):

            nom_copa = input("Escriba el nombre Copa: ")

            nro_org = input("Escriba el nro de la organizacion a la cual pertenecera: ")

            COPA.crearCopa(nom_copa,nro_org)

        elif(opcionCopa == 2):

            COPA.setCopa()

        elif(opcionCopa == 3):

            print(Copa.getCopas())

        elif(opcionCopa == 4):

            COPA.updateCopa()

        elif(opcionCopa == 5):

            COPA.deleteCopa()

        elif(opcionCopa == 6):

            opcion = int(input("MENU\n 1-ORGANIZACIONES \n 2-COPAS \n 3-PAISES \n 4-LIGAS \n 5-EQUIPOS \n 6-JUGADOR \n 7- DTs \n 8- Salir \n OPCION: "))

        else:

            print("Se oprimio una opcion incorrecta, vuelva a intentarlo\n")


    elif(opcion == 3):


        opcionPais = int(input("1-CREAR PAIS \n 2-INSERTAR PAIS CREADO \n 3-VER PAISES DE LA BASE \n 4-MODIFICAR UN PAIS \n 5-ELIMINAR UN PAIS \n 6-VOLVER AL 1ER MENU \n OPCION: "))

        if(opcionPais == 1):

            nombre_pais = input("Escriba el nombre del pais: ")
            nro_org2 = input("Escriba el nro de la org a la cual pertenecera: ")


            PAIS.crearPais(nombre_pais, nro_org2)

        elif(opcionPais == 2):

            PAIS.setPais()

        elif(opcionPais == 3):

            print(Pais.getPaises())

        elif(opcionPais == 4):

            PAIS.updatePais()

        elif(opcionPais == 5):

            PAIS.deletePais()

        elif(opcionPais == 6):

            opcion = int(input("MENU\n 1-ORGANIZACIONES \n 2-COPAS \n 3-PAISES \n 4-LIGAS \n 5-EQUIPOS \n 6-JUGADOR \n 7- DTs \n 8- Salir \n OPCION: "))

        else:
            print("se oprimio una opcion incorrecta, vuelva a intentar")


    elif(opcion == 4):



        opcionLiga = int(input("1-CREAR ORGANIZACION \n 2-INSERTAR LIGA CREADA \n 3-VER LIGAS DE LA BASE \n 4-MODIFICAR UNA LIGA \n 5-ELIMINAR UNA LIGA \n 6-VOLVER AL 1ER MENU \n OPCION: "))

        if(opcionLiga == 1):

            nom_liga = input("Escriba el nombre de la liga: ")

            nro_pais = input("Escriba el numero del pais que pertenece: ")

            Ligue.crearLiga(nom_liga,nro_pais)

        elif(opcionLiga == 2):

            Ligue.setLiga()

            print("La liga se inserto en la base")

        elif(opcionLiga == 3):

            print(Liga.getLigas())

        elif(opcionLiga == 4):

            Ligue.updateLiga()

        elif(opcionLiga == 5):

            Ligue.deleteLiga()

        elif(opcionLiga == 6):

            opcion = int(input("MENU\n 1-ORGANIZACIONES \n 2-COPAS \n 3-PAISES \n 4-LIGAS \n 5-EQUIPOS \n 6-JUGADOR \n 7- DTs \n 8- Salir \n OPCION: "))

        else:

            print("Se oprimio una tecla incorrecta, vuelva a intentar")



    elif(opcion == 5):

        opcionEquipo=int(input("1-CREAR EQUIPO \n 2-INSERTAR EQUIPO CREADA \n 3-VER EQUIPOS DE LA BASE \n 4-MODIFICAR UNA EQUIPOS \n 5-ELIMINAR UN EQUIPO \n 6-VOLVER AL 1ER MENU \n OPCION: "))



        if(opcionEquipo == 1):

            nombre_equipo = input("Escriba Nombre del equipo: ")

            fecha_equipo = input("Escriba fecha de creacion del equipo con formato YYYY-MM-DD: ")

            num_liga2 = input("Escriba el numero de la liga que pertenece el equipo: ")

            Team.crearEquipo(nombre_equipo,fecha_equipo,num_liga2)

        elif(opcionEquipo== 2):

            Team.setEquipo()

        elif(opcionEquipo == 3):

            print(Equipo.getEquipos())

        elif(opcionEquipo == 4):

            Team.updateEquipo()

        elif(opcionEquipo == 5):

            Team.deleteEquipo()

        elif(opcionEquipo == 6):

            opcion = int(input("MENU\n 1-ORGANIZACIONES \n 2-COPAS \n 3-PAISES \n 4-LIGAS \n 5-EQUIPOS \n 6-JUGADOR \n 7- DTs \n 8- Salir \n OPCION: "))

        else:

            print("Se oprimio una opcion incorrecta, vuelva a intentar: ")



    elif(opcion == 6):

        opcionJugador = int(input("1-CREAR JUGADOR \n 2-INSERTAR JUGADOR CREADA \n 3-VER JUGADORES DE LA BASE \n 4-MODIFICAR UN JUGADOR \n 5-ELIMINAR UN JUGADOR \n 6-VOLVER AL 1ER MENU \n OPCION: "))

        Player = Jugador()

        if(opcionJugador == 1):

            nomJugador = input("Ingrese el nombre del jugador: ")
            apeJugador = input("Ingrese el apellido del jugador: ")
            dniJugador = input("Ingrese el dni del jugador: ")
            fecJugador = input("Ingrese fecha de nacimiento de jugador formato YYYY-MM-DD: ")
            salJugador = input("Ingrese salario del jugador: ")
            clauJugador = input("Ingrese clausula del jugador: ")
            patJugador = input("Ingrese patrocinador del jugador: ")
            numJugador = input("Ingrese numero del jugador: ")
            posJugador = input("Ingrese posicion del jugador: ")
            equipoJugador = input("Ingrese id del equipo que pertenece: ")

            Player.crearJugador(nomJugador,dniJugador,apeJugador,fecJugador,salJugador,clauJugador,patJugador,nomJugador,posJugador,equipoJugador)


        elif(opcionJugador==2):

            Player.setJugador()

        elif(opcionJugador == 3):

            print(Jugador.getJugadores())

        elif(opcionJugador == 4):

            Player.updateJugador()

        elif(opcionJugador == 5):

            Player.deleteJugador()

        elif(opcionJugador == 6):

            opcion = int(input("MENU\n 1-ORGANIZACIONES \n 2-COPAS \n 3-PAISES \n 4-LIGAS \n 5-EQUIPOS \n 6-JUGADOR \n 7- DTs \n 8- Salir \n OPCION: "))

        else:

            print("Se oprimio una opcion incorrecta, vuelva a intentar: ")

    elif(opcion == 7):

        opcionDT = int(input("1-CREAR DT \n 2-INSERTAR DT CREADO \n 3-VER DTs DE LA BASE \n 4-MODIFICAR UN DT \n 5-ELIMINAR UN DT \n 6-VOLVER AL 1ER MENU \n OPCION: "))

        if(opcionDT ==1):

            nomDT = input("Ingrese el nombre del DT: ")
            apeDT = input("Ingrese el apellido del DT: ")
            dniDT = input("Ingrese el dni del DT: ")
            fecDT = input("Ingrese fecha de nacimiento de DT formato YYYY-MM-DD: ")
            salDT = input("Ingrese salario del DT: ")
            clauDT = input("Ingrese clausula del DT: ")
            tacDT= input("Ingrese posicion del DT: ")
            equipoDT = input("Ingrese id del equipo que pertenece: ")

            DeTe.crearDT(nomDT,dniDT,apeDT,fecDT,salDT,clauDT,tacDT,equipoDT)

        elif(opcionDT == 2):

            DeTe.setDT()

        elif(opcionDT == 3):

            DT.getDTs()

        elif(opcionDT == 4):

            DeTe.updateDT()

        elif(opcionDT ==5):

            DeTe.deleteDT()

        elif(opcionDT == 6):

            opcion = int(input("MENU\n 1-ORGANIZACIONES \n 2-COPAS \n 3-PAISES \n 4-LIGAS \n 5-EQUIPOS \n 6-JUGADOR \n 7- DTs \n 8- Salir \n OPCION: "))

        else:
            print("Se oprimio una opcion incorrecta, vuelva a intentar: ")


    elif(opcion == 8):

        exit()