from Ej7 import Bufes
from Ej7 import Pedidos
from Ej7 import Persona
from Ej7 import Alumno
from Ej7 import Profesores
from Ej7 import Platos
import datetime



A = Bufes()

#Plato1 = Platos()
#Plato1.crearPlato("Milangas", 120)
#Profesor1 = Profesores()


#Profesor1.crearProfe("Carambita","Pecorino", 15)
#Pedido1 = Pedidos()
#Pedido1.crearPedidos(datetime.datetime(2018,5,1),Plato1,Profesor1, datetime.datetime(2018,5,1,13,30),True)

opcion = 1

while opcion != '8':

    opcion = input("-----MENU-----\n1-AGREGAR ALUMNO\n2-AGREGAR PROFESOR\n3-MODIFICAR ALUMNO\n4-MODIFICAR PROFESOR\n5-ELIMINAR ALUMNO\n6-ELIMINAR PROFESOR\n7-GUARDAR\n8-Salir\nOPCION: ")


    def agregarAlumno():
        AlumnoX = Alumno()
        id_alum = input("Id del alumno: ")
        name = input("Nombre del alumno: ")
        apell = input("Apellido del alumno: ")
        divis = input("División del alumno: ")

        for item in A.lista_personas:

            if item.id_persona == id_alum:

                return "El id Alumno ingresado ya existe"


        AlumnoX.nombre = name
        AlumnoX.apellido = apell
        AlumnoX.id_persona = id_alum
        AlumnoX.division = divis
        A.lista_personas.append(AlumnoX)


        return "EL alumno se cargo Perfectamente"

    def modifAlumno(Id_pers):

        for item in A.lista_personas:

            if item.id_persona == Id_pers and item.__class__ == Alumno:
                name = input("Nombre del alumno a modificar: ")
                apell = input("Apellido del alumno a modificar: ")
                divis = input("División del alumno a modificar: ")
                item.nombre = name
                item.apellido=apell
                item.division=divis

                return 'El alumno se modifico perfectamente'

            else:

                return 'El ID ingresado no existe o no es de un alumno'

    def modifProfe(Id_pers):

        for item in A.lista_personas:

            if item.id_persona == Id_pers and item.__class__ == Profesores:
                name = input("Nombre del Profesor a modificar: ")
                apell = input("Apellido del Profesor a modificar: ")
                desc = input("Descuento del Profesor a modificar: ")
                item.nombre = name
                item.apellido=apell
                item.porcentaje_descuento=desc

                return 'El profesor se modifico perfectamente'

            else:

                return 'El ID ingresado no existe o no es de un profesor'

    def agregarProfe():

        ProfX = Profesores()
        id_prof = input("Id del profesor: ")
        name = input("Nombre del Profesor: ")
        apell = input("Apellido del Profesor: ")
        porcen_desc = input("Porcentaje de descuento del profesor: ")

        for item in A.lista_personas:

            if item.id_persona == id_prof:

                return "El id Profesor ingresado ya existe"

        ProfX.nombre = name
        ProfX.apellidio = apell
        ProfX.id_persona = id_prof
        ProfX.porcentaje_descuento = porcen_desc
        A.lista_personas.append(ProfX)

        return "EL profesor se cargo perfectamente"

    def eliminarProfe(Id_pers):


        for item2 in A.lista_personas:

            if item2.id_personas == Id_pers and item2.__class__ == Profesores:

                for item in A.lista_pedidos:

                    if item.persona.id_persona == Id_pers:

                        A.lista_pedidos.remove(item)

                A.lista_personas.remove(item2)

                return 'El profesor se elimino perfectamente'


        return 'No se pudo eliminar al profesor'

    def eliminarAlumn(Id_pers):

        for item in A.lista_personas:

            if item.id_persona == Id_pers and item.__class__ == Alumno:

                for item2 in A.lista_pedidos:

                    if item.persona.id_persona == Id_pers:

                        A.lista_pedidos.remove(item2)

                A.lista_personas.remove(item)

                return 'El alumno se elimino perfectamente'

        return 'No se pudo eliminar el alumno'

    def hola():

        string = None

        for item in A.lista_personas:

            if item.__class__ == Alumno:

                string += item.id_persona+"|"+item.nombre+"|"+item.apellido+"|"+item.division+"\n"

            else:

                string += item.id_persona + "|" + item.nombre + "|" + item.apellido + "|" + item.porcentaje_descuento + "\n"

        return string


    def guardado():

        f = open("archivo.txt", "w")
        f.write(hola())


    if opcion == '1':

       print(agregarAlumno())

    elif opcion == '2':

        print(agregarProfe())

    elif opcion == '3':

        print(modifAlumno(input("Ingrese ID del alumno a modificar: ")))

    elif opcion == '4':

        print(modifProfe(input("Ingrese ID del profesor a modificar: ")))

    elif opcion == '5':

        print(eliminarAlumn(input("Ingrese ID del alumno a eliminar: ")))

    elif opcion == '6':

        print(eliminarProfe(input("Ingrese ID del profesor a eliminar: ")))

    elif opcion == '7':

        guardado()

