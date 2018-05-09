import datetime

from EjPrueba1persona import Persona
from EjPrueba1registro import Registro

Lucho = Persona()



Lucho.agregarNombre('Luchota')
Lucho.agregarApellido('Larga')
Lucho.agregarFechaNacimiento(datetime.date(2000,10,24))


reg = Registro()
reg.agregarFechaRegistro(datetime.date(2017,1,1))
reg.agregarPeso(65)
reg.agregarAltura(1.70)
Lucho.agregarRegistro(reg)

reg = Registro()
reg.agregarFechaRegistro(datetime.date(2018,1,1))
reg.agregarPeso(70)
reg.agregarAltura(1.80)
Lucho.agregarRegistro(reg)

print(Lucho.averiguarRegistro(datetime.date(2017,1,1)))

print(Lucho.PromedioPesoAlturaEnAño(2017))

print("%",Lucho.PorcentajeCrecimiento(2017))





