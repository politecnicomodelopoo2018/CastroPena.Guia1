
import datetime
import calendar


class Empleado(object):
    nombre= None
    apellido= None
    fecha_nacimiento= None
    telefono = None

    def __init__(self):
        lista_horario = [True, True, True, True, True, False, False]
        lista_asistencia = [ datetime(2018,03,15), datetime(2018,02,16), datetime(2018,02,19)]


    def porcentajeAsistencia(self, año, mes):
        contador=0
        dias_meses = calendar.monthrange(año,mes)[1]
        dias_fue=0
        for item in range(dias_meses):
            i = datetime.date(año, mes, item)
            if self.lista_horario[i.weekday()]:
                for pepe in self.lista_asistencia:
                    if pepe == i:
                        contador+=1
                dias_fue+=1

        return contador / dias_fue * 100









