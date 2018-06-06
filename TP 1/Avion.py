class Avion(object):

    codigoUnico = None
    cantidadPasajerosMaximos = None
    cantidadTripulacionNecesaria = None

    def crearAvion(self,cod,cantPMax,cantTN):

        self.codigoUnico = cod
        self.cantidadPasajerosMaximos = cantPMax
        self.cantidadTripulacionNecesaria = cantTN