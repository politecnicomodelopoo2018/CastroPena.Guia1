
import datetime
import calendar
calendar.monthrange(año,mes)

class Empleado(object):
    nombre= None
    apellido= None
    fecha_nacimiento= None
    telefono = None

    def __init__(self):
        lista_horario = [True, True, True, True, True, False, False]
        lista_asistencia = [ datetime(2018,02,15), datetime(2018,02,16), datetime(2018,02,19)]


    def porcentajeAsistencia(self, año, mes):
        contador=0
        dias_meses = calendar.monthrange(año,mes)[1]

        for item in range(dias_meses):
            i = datetime.date(año, mes, item)
            if i.weekday() >= 0 and i.weekday() <= 4:
                if i == self.lista_asistencia[contador]:
                    contador += 1
        return contador / dias_meses * 100









