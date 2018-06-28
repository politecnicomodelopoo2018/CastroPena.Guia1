from Ej6 import Empresa
from Ej6 import Auto
from Ej6 import Camioneta


E = Empresa()


opcion = None


while opcion != '5':

    opcion = input('1-Crear Auto\n'
                   '2-Crear Camioneta\n'
                   '3-Guardar\n'
                   '4-Cargar\n'
                   '5-SALIDA\n'
                   'OPCION: ')


    if opcion == '1':

        pat = input('Patente del auto: ')

        cant_rue = input('Cantidad de ruedas del auto: ')

        ano_fabric = input('Año de fabricacion del auto: ')

        desca = input('El auto es descapotable?: ')

        auto = Auto(pat, cant_rue, ano_fabric, desca)

        if auto not in E.lista_autos:

            E.lista_autos.append(auto)


    elif opcion == '2':

        pat = input('Patente del camion: ')
        cant_rue = input('Cantidad de ruedas del camion: ')
        ano_fabric = input('Año de fabricacion del camion: ')
        carga = input('Capacidad de carga del camion [kg]: ')

        camion = Camioneta(pat, cant_rue, ano_fabric, carga)

        if camion not in E.lista_camioneta:

            E.lista_camioneta.append(camion)


    elif opcion == '3':

        if E.lista_camioneta or E.lista_autos:

            archivo = open("archivo.txt","w")

            for item in E.lista_autos:

                archivo.write(item.__class__.__name__ + "/" + item.patente + "/" + item.cant_ruedas + "/" + item.año_fabricacion + "/" + item.descapotable + "/\n" )


            for item in E.lista_camioneta:

                archivo.write(item.__class__.__name__ + "/" + item.patente + "/" + item.cant_ruedas + "/" + item.año_fabricacion + "/" + item.capacidad_carga + "/\n" )


            print("Se guardo todo!!")


        else:

            print("No se pudo guardar!!")


        archivo.close()


    elif opcion == '4':

        archivo = open("archivo.txt", "r")


        for line in archivo:

            lista = line.split("/")


            if lista[0] == 'Auto':

                lista.remove(lista[0])

                AutoAux = Auto(lista[0],lista[1],lista[2],lista[3])

                E.lista_autos.append(AutoAux)

            elif lista[0] == 'Camioneta':

                lista.remove(lista[0])

                CamionAux = Camioneta(lista[0],lista[1],lista[2],lista[3])

                E.lista_camioneta.append(CamionAux)



        archivo.close()


