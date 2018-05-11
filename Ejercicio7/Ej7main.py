from Ej7 import Bufes
from Ej7 import Pedidos
from Ej7 import Persona
from Ej7 import Alumno
from Ej7 import Profesores
from Ej7 import Platos
import datetime



def agregarAlumno():
    AlumnoX = Alumno()
    name = input("Nombre del alumno: ")
    apell = input("Apellido del alumno: ")
    divis = input("División del alumno: ")
    AlumnoX.crearAlumno(name, apell, divis)

A = Bufes()


#Plato1 = Platos()
#Plato1.crearPlato("Milangas", 120)
#Profesor1 = Profesores()


#Profesor1.crearProfe("Carambita","Pecorino", 15)
#Pedido1 = Pedidos()
#Pedido1.crearPedidos(datetime.datetime(2018,5,1),Plato1,Profesor1, datetime.datetime(2018,5,1,13,30),True)

opcion = "0"

while opcion != "9":
    print(A.mostrarListaPersonas())
    opcion = input("-----MENU-----\n1-AGREGAR ALUMNO\n2-AGREGAR PROFESOR\n3-MODIFICAR ALUMNO\n4-MODIFICAR PROFESOR\n5-ELIMINAR ALUMNO\n6-ELIMINAR PROFESOR\n7-GUARDAR\n8-CARGAR\n9-SALIR\nOPCION: ")


    def agregarAlumno():
        AlumnoX = Alumno()
        id_alum = input("Id del alumno: ")
        name = input("Nombre del alumno: ")
        apell = input("Apellido del alumno: ")
        divis = input("División del alumno: ")

        for item in A.lista_personas:

            if item.id_persona == id_alum:

                return "El id Alumno ingresado ya existe"


        AlumnoX.id_persona= id_alum
        AlumnoX.nombre = name
        AlumnoX.apellido = apell
        AlumnoX.division = divis
        A.lista_personas.append(AlumnoX)
        return "Se ha agregado un Alumno a la lista "


    def modifAlumno(Id_pers):

        for item in A.lista_personas:

            if item.id_persona == Id_pers and item.__class__ == Alumno:
                name = input("Nombre del alumno a modificar: ")
                apell = input("Apellido del alumno a modificar: ")
                divis = input("División del alumno a modificar: ")
                item.nombre = name
                item.apellido=apell
                item.division=divis
            else:

                return "El ID alumno ingresado no existe"


    def modifProfe(Id_pers):

        for item in A.lista_personas:

            if item.id_persona == Id_pers and item.__class__ == Profesores:
                name = input("Nombre del Profesor a modificar: ")
                apell = input("Apellido del Profesor a modificar: ")
                desc = input("Descuento del Profesor a modificar: ")
                item.nombre = name
                item.apellido=apell
                item.porcentaje_descuento=desc
            else:

                return "El ID profesor ingresado no existe"


    def agregarProfe():

        ProfX = Profesores()
        id_prof = input("Id del profesor: ")
        name = input("Nombre del Profesor: ")
        apell = input("Apellido del Profesor: ")
        porcen_desc = input("Porcentaje de descuento del profesor: ")

        for item in A.lista_personas:

            if item.id_persona == id_prof:

                return "El id Profesor ingresado ya existe"

        ProfX.id_persona = id_prof
        ProfX.nombre = name
        ProfX.apellido = apell
        ProfX.porcentaje_descuento = porcen_desc
        A.lista_personas.append(ProfX)
        return "Se ha agregado un Profesor a la lista "


    def eliminarProfe(Id_pers):


        for item2 in A.lista_personas:

            if item2.id_persona == Id_pers and item2.__class__ == Profesores:


                for item in A.lista_pedidos:

                    if item.persona.id_persona == Id_pers:

                        A.lista_pedidos.remove(item)

                for item in A.lista_personas:

                    if item.id_persona == Id_pers:

                        A.lista_personas.remove(item)


    def eliminarAlumno(Id_pers):


        for item2 in A.lista_personas:

            if item2.id_persona == Id_pers and item2.__class__ == Alumno:

                for item in A.lista_pedidos:

                    if item.persona.id_persona == Id_pers:

                        A.lista_pedidos.remove(item)

                for item in A.lista_personas:

                    if item.id_persona == Id_pers:

                        A.lista_personas.remove(item)


    def codification():

        personas_str = ""

        for item in A.lista_personas:

            if item.__class__ == Alumno:

                nombre_clase = item.__class__.__name__

                personas_str += nombre_clase+"/"+item.id_persona+"/"+item.nombre+"/"+item.apellido+"/"+item.division+"\n"

            else:

                nombre_clase = item.__class__.__name__

                personas_str += nombre_clase+"/"+item.id_persona+"/"+item.nombre+"/"+item.apellido+"/"+item.porcentaje_descuento+"\n"

        return personas_str




    if opcion == "1":

       print(agregarAlumno())



    elif opcion == "2":

        print(agregarProfe())

    elif opcion == "3":


        print(modifAlumno(input("Ingrese ID del alumno a modificar: ")))

    elif opcion == "4":


       print(modifProfe(input("Ingrese ID del alumno a modificar: ")))

    elif opcion == "5":


        eliminarAlumno(input("Ingrese ID del alumno a eliminar"))


    elif opcion == "6":

        eliminarProfe(input("Ingrese ID del profesor a eliminar"))

    elif opcion == "7":

        f = open("archivo.txt","w")

        f.write(codification())

        f.close()


    elif opcion == "8":

        f = open("archivo.txt", "r")

        for line in f:

            line = line.replace('\n','')

            d = line.split('/')

            clase = eval(d[0])

            x = clase()

            if  d[0] == "Alumno":

                x.id_persona = d[1]
                x.nombre = d[2]
                x.apellido = d[3]
                x.division = d[4]

                A.lista_personas.append(x)

            elif d[0] == "Profesores":

                x.id_persona = d[1]
                x.nombre = d[2]
                x.apellido = d[3]
                x.porcentaje_descuento = d[4]

                A.lista_personas.append(x)

    #elif opcion == "9":

        #pepe=0
        #