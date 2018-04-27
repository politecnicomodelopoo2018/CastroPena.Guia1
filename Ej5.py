import datetime

class Discografica(object):

    nombre = None

    def __init__(self, nom):

        self.lista_album = []

        self.nombre = nom

    def agregarAlbumADiscografica(self, UnAlb):

        self.lista_album.append(UnAlb)

class Album(object):

    titulo = None

    def __init__(self, title):

        self.lista_canciones = []

        self.titulo = title


    def agregarCancionALista(self, UnaSong):

        self.lista_canciones.append(UnaSong)

    def listadeArtistasxAlbum(self):

        listaaux = []
        verif = True


        for item in self.lista_canciones:

            for i in item.lista_artista:

                for j in listaaux:

                    if i == j:

                        verif = False

                if verif == True:

                    listaaux.append(i)


        return listaaux



    def artistaMasInfluyente(self):

        Artista_Parcial= None

        ArtistaInfluyente_Parcial = None

        contador_canciones = 0

        max_contador = 0



        for item in self.lista_canciones:

            for i in item.lista_artista:

                Artista_Parcial = i

                for item2 in self.lista_canciones:

                    for i2 in self.lista_artista:

                        if Artista_Parcial == i2:

                            contador_canciones += 1

                if contador_canciones > max_contador:

                    max_contador = contador_canciones

                    ArtistaInfluyente_Parcial = Artista_Parcial

            return ArtistaInfluyente_Parcial









class Cancion(object):

    titulo = None

    def __init__(self,title):

        self.lista_artista = []

        self.lista_autor = []

        self.titulo = title


    def agregarArtistaALista(self,UnArt):

        self.lista_artista.append(UnArt)

    def agregarAutorALista(self, UnAut):

        self.lista_autor.append(UnAut)

    def devuleveArtistas(self, i):

        return self.lista_artista[i]


class Persona(object):

    nombre=None
    apellido=None
    fecha_nac=None

    def __init__(self, nom, ape, fecha):
        self.nombre = nom
        self.apellido = ape
        self.fecha_nac = fecha


class Artista(Persona):

    pass

class Autores(Persona):

    nacionalidad = None

    def __init__(self, nom, ape, fecha, nac):

        Persona.__init__(self, nom, ape, fecha)

        self.nacionalidad = nac

