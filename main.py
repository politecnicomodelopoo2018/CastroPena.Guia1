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

    #opcion = int(input("\n MENU\n 1-ORGANIZACIONES \n 2-COPAS \n 3-PAISES \n 4-LIGAS \n 5-EQUIPOS \n 6-JUGADOR \n 7- DTs \n 8- Salir \n OPCION: "))

    if(opcion == 1):

        opcionOrg = int(input("\n 1-CREAR ORGANIZACION \n 2-INSERTAR ORG EN BASE \n 3-VER ORGANIZACIONES DE LA BASE \n 4-MODIFICAR UNA ORGANIZACION \n 5-ELIMINAR UNA ORGANIZACION \n 6-VOLVER AL 1ER MENU \n OPCION: "))


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

            print(Organizacion.getOrganizaciones())

            updateOrg = int(input("Ingrese el id de la organizacion que desea modificar: "))

            ORG = Organizacion.getOrganizacion(updateOrg)


            ORG.nombre = input("Escriba el nombre de la organizacion: ")

            ORG.continente = input("Escriba el nombre del continente de la organizacion: ")

            ORG.updateOrganizacion()

        elif(opcionOrg == 5):

            print(Organizacion.getOrganizaciones())

            deleteOrg = int(input("Ingrese el id de la Organizacion que desea eliminar: "))

            ORG = Organizacion.getOrganizacion(deleteOrg)

            ORG.deleteOrganizacion()

        elif(opcionOrg == 6):

            #opcion = 0
            #continue

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

            print(Copa.getCopas())

            updateCopita = int(input("Ingrese el id de la copa que desea modificar: "))

            COPA = Copa.getCopa(updateCopita)

            COPA.nombre = input("Escriba el nombre de la Copa: ")

            COPA.IDOrgPertenecer = input("Escriba el id de la organizacion a la que pertenece: ")

            COPA.updateCopa()

        elif(opcionCopa == 5):

            print(Copa.getCopas())

            deleteCopita = int(input("Ingrese el id de la Copa que desea eliminar: "))

            COPA = Copa.getCopa(deleteCopita)

            COPA.deleteCopa()

        elif(opcionCopa == 6):

            #opcion = 0
            #continue

            opcion = int(input("\nMENU\n 1-ORGANIZACIONES \n 2-COPAS \n 3-PAISES \n 4-LIGAS \n 5-EQUIPOS \n 6-JUGADOR \n 7- DTs \n 8- Salir \n OPCION: "))

        else:

            print("Se oprimio una opcion incorrecta, vuelva a intentarlo\n")


    elif(opcion == 3):


        opcionPais = int(input("\n 1-CREAR PAIS \n 2-INSERTAR PAIS CREADO \n 3-VER PAISES DE LA BASE \n 4-MODIFICAR UN PAIS \n 5-ELIMINAR UN PAIS \n 6-VOLVER AL 1ER MENU \n OPCION: "))

        if(opcionPais == 1):

            nombre_pais = input("Escriba el nombre del pais: ")
            nro_org2 = input("Escriba el nro de la org a la cual pertenecera: ")


            PAIS.crearPais(nombre_pais, nro_org2)

        elif(opcionPais == 2):

            PAIS.setPais()

        elif(opcionPais == 3):

            print(Pais.getPaises())

        elif(opcionPais == 4):

            print(PAIS.getPaises())

            updateCountry = int(input("Ingrese el id del pais que desea modificar: "))

            PAIS = Pais.getPais(updateCountry)

            PAIS.nombre = input("Escriba el nombre de la Pais: ")

            PAIS.IDOrgPertenecer = input("Escriba el id de la organizacion a la que pertenece: ")

            PAIS.updatePais()

        elif(opcionPais == 5):

            print(Pais.getPaises())

            deletePaiss = int(input("Ingrese el id del Pais que desea eliminar: "))

            PAIS = Pais.getPais(deletePaiss)

            PAIS.deletePais()

        elif(opcionPais == 6):

            #opcion = 0
            #continue

            opcion = int(input("\nMENU\n 1-ORGANIZACIONES \n 2-COPAS \n 3-PAISES \n 4-LIGAS \n 5-EQUIPOS \n 6-JUGADOR \n 7- DTs \n 8- Salir \n OPCION: "))

        else:
            print("se oprimio una opcion incorrecta, vuelva a intentar")


    elif(opcion == 4):



        opcionLiga = int(input("\n 1-CREAR LIGA \n 2-INSERTAR LIGA CREADA \n 3-VER LIGAS DE LA BASE \n 4-MODIFICAR UNA LIGA \n 5-ELIMINAR UNA LIGA \n 6-VOLVER AL 1ER MENU \n OPCION: "))

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

            print(Liga.getLigas())

            updateLigue = int(input("Ingrese el id de la ligue que desea modificar: "))

            Ligue = Liga.getLiga(updateLigue)

            Ligue.nombre = input("Escriba el nombre de la Liga: ")

            Ligue.IDPaisPertenecer = input("Escriba el id del Pais a la que pertenece: ")

            Ligue.updateLiga()

        elif(opcionLiga == 5):

            print(Liga.getLigas())

            deleteLigue = int(input("Ingrese el id de la Ligaque desea eliminar: "))

            Ligue = Liga.getLiga(deleteLigue)

            Ligue.deleteLiga()

        elif(opcionLiga == 6):

            #opcion = 0
            #continue

            opcion = int(input("\nMENU\n 1-ORGANIZACIONES \n 2-COPAS \n 3-PAISES \n 4-LIGAS \n 5-EQUIPOS \n 6-JUGADOR \n 7- DTs \n 8- Salir \n OPCION: "))

        else:

            print("Se oprimio una tecla incorrecta, vuelva a intentar")



    elif(opcion == 5):

        opcionEquipo=int(input("\n 1-CREAR EQUIPO \n 2-INSERTAR EQUIPO CREADA \n 3-VER EQUIPOS DE LA BASE \n 4-MODIFICAR UNA EQUIPOS \n 5-ELIMINAR UN EQUIPO \n 6-VOLVER AL 1ER MENU \n OPCION: "))



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

            print(Equipo.getEquipos())

            updateTeam = int(input("Ingrese el id del equipo que desea modificar: "))

            Team = Equipo.getEquipo(updateTeam)

            Team.nombre = input("Escriba el nombre del Equipo: ")

            Team.idLigaFK = input("Escriba el id de la Liga a la que pertenece: ")

            Team.updateEquipo()

        elif(opcionEquipo == 5):

            print(Equipo.getEquipos())

            deleteTeam = int(input("Inserte el id del Equipo que desea eliminar: "))

            Team = Equipo.getEquipo(deleteTeam)

            Team.deleteEquipo()

        elif(opcionEquipo == 6):

            #opcion = 0
            #continue

            opcion = int(input("MENU\n 1-ORGANIZACIONES \n 2-COPAS \n 3-PAISES \n 4-LIGAS \n 5-EQUIPOS \n 6-JUGADOR \n 7- DTs \n 8- Salir \n OPCION: "))

        else:

            print("Se oprimio una opcion incorrecta, vuelva a intentar: ")



    elif(opcion == 6):

        opcionJugador = int(input("\n  1-CREAR JUGADOR \n 2-INSERTAR JUGADOR CREADA \n 3-VER JUGADORES DE LA BASE \n 4-MODIFICAR UN JUGADOR \n 5-ELIMINAR UN JUGADOR \n 6-VOLVER AL 1ER MENU \n OPCION: "))


        if(opcionJugador == 1):

            nomJugador = input("Ingrese el nombre del jugador: ")
            apeJugador = input("Ingrese el apellido del jugador: ")
            dniJugador = int(input("Ingrese el dni del jugador: "))
            fecJugador = input("Ingrese fecha de nacimiento de jugador formato YYYY-MM-DD: ")
            salJugador = int(input("Ingrese salario del jugador: "))
            clauJugador = int(input("Ingrese clausula del jugador: "))
            patJugador = input("Ingrese patrocinador del jugador: ")
            numJugador = int(input("Ingrese numero del jugador: "))
            posJugador = input("Ingrese posicion del jugador: ")
            equipoJugador = int(input("Ingrese id del equipo que pertenece: "))

            Player.crearJugador(nomJugador,dniJugador,apeJugador,fecJugador,salJugador,clauJugador,patJugador,numJugador,posJugador,equipoJugador)


        elif(opcionJugador==2):

            Player.setJugador()

        elif(opcionJugador == 3):

            print(Jugador.getJugadores())

        elif(opcionJugador == 4):

            print(Jugador.getJugadores())

            updatePlayer = int(input("Ingrese un id del Jugador que se desea modificar: "))

            Player = Jugador.getJugador(updatePlayer)

            Player.nombre = input("Ingrese el nombre del jugador: ")
            Player.apellido = input("Ingrese el apellido del jugador: ")
            Player.dni = int(input("Ingrese el dni del jugador: "))
            Player.fecha_nacimiento = input("Ingrese fecha de nacimiento de jugador formato YYYY-MM-DD: ")
            Player.salario = int(input("Ingrese salario del jugador: "))
            Player.clausula = int(input("Ingrese clausula del jugador: "))
            Player.patrocinador = input("Ingrese patrocinador del jugador: ")
            Player.numero = int(input("Ingrese numero del jugador: "))
            Player.posicion = input("Ingrese posicion del jugador: ")
            Player.idEquipoPertenece = int(input("Ingrese id del equipo que pertenece: "))

            Player.updateJugador()

        elif(opcionJugador == 5):

            print(Jugador.getJugadores())

            deletePlayer = int(input("Ingrese el id del jugador que desea eliminar: "))

            Player = Jugador.getJugador(deletePlayer)

            Player.deleteJugador()

        elif(opcionJugador == 6):

            #opcion = 0
            #continue

            opcion = int(input("MENU\n 1-ORGANIZACIONES \n 2-COPAS \n 3-PAISES \n 4-LIGAS \n 5-EQUIPOS \n 6-JUGADOR \n 7- DTs \n 8- Salir \n OPCION: "))

        else:

            print("Se oprimio una opcion incorrecta, vuelva a intentar: ")


    elif(opcion == 7):

        opcionDT = int(input("\n 1-CREAR DT \n 2-INSERTAR DT CREADO \n 3-VER DTs DE LA BASE \n 4-MODIFICAR UN DT \n 5-ELIMINAR UN DT \n 6-VOLVER AL 1ER MENU \n OPCION: "))

        if(opcionDT ==1):

            nomDT = input("Ingrese el nombre del DT: ")
            apeDT = input("Ingrese el apellido del DT: ")
            dniDT = int(input("Ingrese el dni del DT: "))
            fecDT = input("Ingrese fecha de nacimiento de DT formato YYYY-MM-DD: ")
            salDT = int(input("Ingrese salario del DT: "))
            clauDT = int(input("Ingrese clausula del DT: "))
            tacDT= input("Ingrese tactica preferida del DT: ")
            equipoDT = int(input("Ingrese id del equipo que pertenece: "))

            DeTe.crearDT(nomDT,dniDT,apeDT,fecDT,salDT,clauDT,tacDT,equipoDT)

        elif(opcionDT == 2):

            DeTe.setDT()

        elif(opcionDT == 3):

            print(DT.getDTs())

        elif(opcionDT == 4):

            print(DT.getDTs())

            updateDT = int(input("Ingrese id del dt que desea modificar: "))

            DeTe = DT.getDT(updateDT)

            DeTe.nombre = input("Ingrese el nombre del DT: ")
            DeTe.apellido = input("Ingrese el apellido del DT: ")
            DeTe.dni = int(input("Ingrese el dni del DT: "))
            DeTe.fecha_nacimiento = input("Ingrese fecha de nacimiento de DT formato YYYY-MM-DD: ")
            DeTe.salario = int(input("Ingrese salario del DT: "))
            DeTe.clausula = int(input("Ingrese clausula del DT: "))
            DeTe.tactica_preferida = input("Ingrese tactica preferida del DT: ")
            DeTe.idEquipoPertenece = int(input("Ingrese id del equipo que pertenece: "))

            DeTe.updateDT()

        elif(opcionDT ==5):

            print(DT.getDTs())

            deleteDeTe = int(input("Ingrese el id del jugador que desea eliminar: "))

            DeTe = DT.getDT(deleteDeTe)

            DeTe.deleteDT()

        elif(opcionDT == 6):

            #opcion = 0
            #continue

            opcion = int(input("\nMENU\n 1-ORGANIZACIONES \n 2-COPAS \n 3-PAISES \n 4-LIGAS \n 5-EQUIPOS \n 6-JUGADOR \n 7- DTs \n 8- Salir \n OPCION: "))

        else:
            print("Se oprimio una opcion incorrecta, vuelva a intentar: ")


    elif(opcion == 8):

        exit()

    else:

        print("Se oprimio una opcion incorrecta, vuelva a intentar: ")
        opcion = int(input("\nMENU\n 1-ORGANIZACIONES \n 2-COPAS \n 3-PAISES \n 4-LIGAS \n 5-EQUIPOS \n 6-JUGADOR \n 7- DTs \n 8- Salir \n OPCION: "))