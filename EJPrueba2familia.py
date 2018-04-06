from EjPrueba2personas import Personas

class Familia(object):
    def __init__(self, nombre):
        self.lista_personas=[]
        self.nomb_flia = nombre

    def agregarPersonaAFamilia(self,unaPersona):

        self.lista_personas.append(unaPersona)


    def promedioCaloriasFamilia(self):

        guarda_calorias = 0
        contador_personas= 0

        for item in self.lista_personas:

            guarda_calorias += item.cantidadCalorias()

            contador_personas += 1

        return guarda_calorias / contador_personas


    def maxCalorias(self):

        max_kcal = 0
        personaCalMax= None

        for item in self.lista_personas:

            if item.cantidadCalorias() > max_kcal:

                max_kcal = item.cantidadCalorias()

                personaCalMax = item


        return personaCalMax, max_kcal




    def minCalorias(self):

        min_kcal = self.maxCalorias()[1]
        personaCalMin= None

        for item in self.lista_personas:

            if item.cantidadCalorias() < min_kcal:

                min_kcal = item.cantidadCalorias()

                personaCalMin = item


        return personaCalMin, min_kcal




