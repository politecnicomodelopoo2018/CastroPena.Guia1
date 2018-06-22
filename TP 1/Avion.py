class Avion(object):

    codigoUnico = None
    cantidadPasajerosMaximos = None
    cantidadTripulacionNecesaria = None

    def crearAvion(self,cod,cantPMax,cantTN):

        self.codigoUnico = cod
        self.cantidadPasajerosMaximos = cantPMax
        self.cantidadTripulacionNecesaria = cantTN


    def DeserializarAvion(self,d):

        self.codigoUnico = d["codigoUnico"]
        self.cantidadPasajerosMaximos = d["cantidadDePasajerosMaxima"]
        self.cantidadTripulacionNecesaria = d["cantidadDeTripulacionNecesaria"]

