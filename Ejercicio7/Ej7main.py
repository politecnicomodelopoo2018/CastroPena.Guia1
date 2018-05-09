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

opcion = input("-----MENU-----\n1-AGREGAR ALUMNO\n2-AGREGAR PROFESOR\n3-MODIFICAR ALUMNO\n4-MODIFICAR PROFESOR\n5-ELIMINAR ALUMNO\n6-ELIMINAR PROFESOR\nOPCION: ")


def agregarAlumno():
    AlumnoX = Alumno()
    id_alum = input("Id del alumno: ")
    name = input("Nombre del alumno: ")
    apell = input("Apellido del alumno: ")
    divis = input("División del alumno: ")

    for item in A.lista_personas:

        if item.id_persona == id_alum:

            return "El id Alumno ingresado ya existe"


    AlumnoX.crearAlumno(id_alum ,name, apell, divis)
    A.lista_personas.append(AlumnoX)


def modifAlumno(Id_pers):

    for item in A.lista_personas:

        if item.id_persona == Id_pers and item.__class__ == Alumno:
            name = input("Nombre del alumno a modificar: ")
            apell = input("Apellido del alumno a modificar: ")
            divis = input("División del alumno a modificar: ")
            item.nombre = name
            item.apellido=apell
            item.division=divis

def modifProfe(Id_pers):

    for item in A.lista_personas:

        if item.id_persona == Id_pers and item.__class__ == Profesores:
            name = input("Nombre del Profesor a modificar: ")
            apell = input("Apellido del Profesor a modificar: ")
            desc = input("Descuento del Profesor a modificar: ")
            item.nombre = name
            item.apellido=apell
            item.porcentaje_descuento=desc


def agregarProfe():
    ProfX = Profesores()
    id_prof = input("Id del profesor: ")
    name = input("Nombre del Profesor: ")
    apell = input("Apellido del Profesor: ")
    porcen_desc = input("Porcentaje de descuento del profesor: ")

    for item in A.lista_personas:

        if item.id_persona == id_prof:
            return "El id Profesor ingresado ya existe"

    ProfX.crearProfe(id_prof,name,apell,porcen_desc)
    A.lista_personas.append(ProfX)


def eliminarProfe(Id_pers):


    for item2 in A.lista_personas:

        if item2.id_personas == Id_pers and item2.__class__ == Profesores:


            for item in A.lista_pedidos:

                if item.persona.id_persona == Id_pers:

                    A.lista_pedidos.remove(item)

            for item in A.lista_personas:

                if item.id_persona == Id_pers:

                    A.lista_personas.remove(item)




if opcion == "1":

   agregarAlumno()



elif opcion == "2":

    agregarProfe()

elif opcion == 3:



    modifAlumno(input("Ingrese ID del alumno a modificar: "))

elif opcion == 4:


   modifProfe(input("Ingrese ID del alumno a modificar: "))

elif opcion == 5:

    def eliminarProfe(unBufe,unProfe):

        for item in unBufe.lista_pedidos:

            if item.persona == unProfe:
                item.persona.remove()
                item.remove()

elif opcion == 6:

    def eliminarAlumno(unBufe,unAlumn):

        for item in unBufe.lista_pedidos:

            if item.persona == unAlumn:
                item.persona.remove()
                item.remove()


