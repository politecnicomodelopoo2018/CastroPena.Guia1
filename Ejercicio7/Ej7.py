class Bufes(object):


    def __init__(self):

        self.lista_pedidos=[]
        self.lista_personas=[]



    def agregarPedidosALista(self,UnPedido):

        self.lista_pedidos.append(UnPedido)

    def agregarProfesoresALista(self,UnPerso):

        self.lista_personas.append(UnPerso)



class Pedidos(object):

    fecha_creacion = None
    plato = None
    persona = None
    hora_entrega = None
    estado_pedido = None

    def crearPedidos(self,fec,pla,per,hor,est):

        self.fecha_creacion=fec
        self.plato=pla
        self.persona=per
        self.hora_entrega=hor
        self.estado_pedido=est

class Platos(object):

    nombre_plato = None

    precio = None

    def crearPlato(self,nom,pre):

        self.nombre_plato = nom

        self.precio = pre



class Persona(object):

    id_persona=None
    nombre = None
    apellido = None


class Profesores(Persona):

    porcentaje_descuento = None


class Alumno(Persona):

    division = None

