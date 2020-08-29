import re
import sys

import Prueba as Pb


Op1 = 'CARGAR '#Variable a comparar y buscar la accion
Op2 = 'SELECCIONAR'
Op3 = 'MAXIMO'
Op4 = 'MINIMO'
Op5 = 'SUMA'
Op6 = 'CUENTA'
Op7 = 'REPORTAR'
Archivos = list()#Lista dinamica para obtener las listas temporales y guardarlas
ArchivosFin = list()#Lista que guarda el resultado final de la lista "Archivos"
def print_hi():
    print('--------------------------------------------------------------------------------------SimpleQl--------------------------------------------------------------------------------------')
print_hi()

def salirAlv():
    sys.exit()
asdasd = True
Inicio = ' '
while Inicio.upper():
    # Cargar
    Inicio = input('*Ingrese el comando: ')  # Obtener el texto de la consola
    Valores = Inicio.upper()
    ArreglodeBusqueda = Valores.split(" ")
    print(ArreglodeBusqueda)
    if ArreglodeBusqueda[0] == 'CARGAR':#Compara la palabra encontrada con la variable OP1
        Buscar1 = re.search(Op1, Inicio, re.IGNORECASE)  # Funcion para buscar la accion requerida "CARGAR" y también vuelve el texto obtenido a mayusculas para poder comparar con la variable Op
        InstruccionInicial = Inicio[int(Buscar1.start()):int(Buscar1.end())]  # Obtiene la palabra buscada
        RestoEn = Inicio[Buscar1.end():len(Inicio)]  # Obtiene el resto del texto
        ArchivosJSON = re.sub('\s', '', RestoEn)  # Borra los espacios en blanco
        ArchivosJSON1 = re.split(',', ArchivosJSON)  # Identifica cada coma y crea una lista cada ves que encuentra una coincidencia

        print('CARGANDO.... ',ArchivosJSON1,'\n')
        print('\n')

        for i in ArchivosJSON1:
            temporal = Pb.jsonread(i)
            Archivos.extend(temporal)
        print('.....', '\n')
        print('\n')
        print('CARGA COMPLETA')

        Tamaño = len(ArchivosFin)
        ArchivosFin = Archivos

    elif ArreglodeBusqueda[0] == 'SELECCIONAR':
        for R in range(1, len(ArreglodeBusqueda)):
            if ArreglodeBusqueda[R].strip() == '*':
                for M in range(0, len(ArchivosFin)):
                    var = str(ArchivosFin[M])
                    separar = re.split(',', var)
                    separado = separar
                    sin = re.sub('{', '', separado)  # Borra los espacios en blanco
                print(separado[0])

                    #for J in range(0, len(separar)):
                     #   ver = (separar[J])
                      #  vers = (ver)
                       # print(vers[0])
                        #print(vers[1])
                        #print(vers[2])
                        #print(vers[3])
           # elif
    elif ArreglodeBusqueda[0] == Op3:
        print('No sale joven')
    else:
        print('holi')