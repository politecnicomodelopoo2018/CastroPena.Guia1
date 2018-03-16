# -*- coding: utf-8 -*-

from materia import Materia



class Alumno(object):
    nombre = ""
    apellido=""
    fecha_nacimiento = None

    def __init__(self):
        self.lista_materias = []

    def agregarMateria(self, nombre_materia):
        unaM =Materia(nombre_materia)
        self.lista_materias.append(unaM)

    def agregarNotaAMateria(self, nombre_materia, nota):
        for mat in self.lista_materias:
            if mat.nombre_materia == nombre_materia:
                mat.agregarNota(nota)

    def promedio(self, nombre_materia):
        for mat in self.lista_materias:
            if mat.nombre_materia == nombre_materia:
                pro = mat.promedios()
        return pro



    def setNombre(self, nombre):
        self.nombre=nombre

    def setApellido(self, apellido):
        self.apellido=apellido

    def setFechaNac(self,fecha):
        self.fecha_nacimiento= fecha

    def AgregarNota(self, nota):
        if nota <=1 or nota >= 10:
            return False
        self.lista_notas.append(nota)
        return True

    def MayorNota(self):
        if len(self.lista_notas) == 0:
            return False
        m=self.lista_notas[0]
        for item in self.lista_notas:
            if item > m:
                m=item
        return m

    def MenorNota(self):
        if len(self.lista_notas) == 0:
            return False
        l= self.lista_notas[0]
        for item in self.lista_notas:
            if item < l:
                l=item
        return l

    def PromedioNota(self):
        if len(self.lista_notas) == 0:
            return False
        CantidadNotas = len(self.lista_notas)
        SumaNotas = sum(self.lista_notas)
        return SumaNotas/CantidadNotas


    def MenorNotaMateria(self,nombre_materia):
        for mat in self.lista_materias:
            if mat.nombre_materia == nombre_materia:
                menor = mat.menorNotaMateria()
        return menor


    def MayorNotaMateria(self,nombre_materia):
        for mat in self.lista_materias:
            if mat.nombre_materia == nombre_materia:
                mayor = mat.mayorNotaMateria()
        return mayor

    def PromedioGeneral(self):
        if len(self.lista_materias) == 0:
            return False
        a=0
        for mat in self.lista_materias:
            a += mat.promedios()
        return a / len(self.lista_materias)

    def PromedioMax(self):

        proms = []

        for mat in self.lista_materias:
            proms.append(mat.promedios())

        return max(proms)

    def PromedioMin(self):

        proms = []

        for mat in self.lista_materias:
            proms.append(mat.promedios())

        return min(proms)
