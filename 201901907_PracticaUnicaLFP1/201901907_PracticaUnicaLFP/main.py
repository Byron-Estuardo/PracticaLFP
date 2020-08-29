import re
import sys
import json
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
Archivos2 = list()
varJunt = []
varA = []
varFin = []
varFin1 = []
table = []
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
    if ArreglodeBusqueda[0].strip() == 'CARGAR':#Compara la palabra encontrada con la variable OP1
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
    elif ArreglodeBusqueda[0].strip() == 'SELECCIONAR':
        for R in range(1, len(ArreglodeBusqueda)):
            if ArreglodeBusqueda[R].strip() == '*':
                for M in range(0, len(ArchivosFin)):
                    var = str(ArchivosFin[M])
                    var1 = re.sub('{', '', var)
                    var2 = re.sub('}', '', var1)
                    varA = re.split(',', var2)
                    varJunt = varJunt + varA
                Archivos2 = varJunt
                varFin1 = varJunt
                for B in range(0, len(ArchivosFin)):
                    print('-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*')
                    print(ArchivosFin[B])
                    print('-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*')

            elif ArreglodeBusqueda[0].strip() == 'SELECCIONAR':
                if ArreglodeBusqueda[R].strip() == 'NOMBRE':
                    for z in range(0, len(ArchivosFin)):
                        print('Nombre:'),print(ArchivosFin[z]['nombre'])

    elif ArreglodeBusqueda[0] == Op3:
        print('No sale joven')
    else:
        print('holi')