class Materia(object):
    nombre_materia= None

    def __init__(self,nombre_materia):
        self.nombre_materia=nombre_materia
        self.lista_notas=[]
    def agregarNota(self, nota):
        self.lista_notas.append(nota)
    def promedios(self):
        return sum(self.lista_notas)/len(self.lista_notas)
    def menorNotaMateria(self):
        if len(self.lista_notas) == 0:
            return False
        a=self.lista_notas[0]
        for nota in self.lista_notas:
            if a > nota:
                a = nota
        return a

    def mayorNotaMateria(self):
        if len(self.lista_notas) == 0:
            return False
        a=self.lista_notas[0]
        for nota in self.lista_notas:
            if a < nota:
                a = nota
        return a






