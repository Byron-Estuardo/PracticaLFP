# -*- coding: UTF-8 -*-
import sys, os, re, html
import Prueba as Pb
import webbrowser


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
TableFin = []
table1 = []
TableFin = []
comp = []
RegistroTab = []

AtributosComp = ['NOMBRE', 'EDAD', 'ACTIVO', 'PROMEDIO']
def BorrarContenido(pfile):
    BorrarContenido()
def print_hi():
    print('╔══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗')
    print('║ ------------------------------------------------------------------------------------SimpleQl------------------------------------------------------------------------------------ ║')
    print('╚══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝')
print_hi()
Inicio = ' '
while Inicio.upper():
    Inicio = input('*Ingrese el comando: ')  # Obtener el texto de la consola
    Valores = Inicio.upper()
    ArreglodeBusqueda = Valores.split(" ")
    if ArreglodeBusqueda[0].strip() == 'CARGAR':#Compara la palabra encontrada con la variable OP1
        Buscar1 = re.search(Op1, Inicio, re.IGNORECASE)  # Funcion para buscar la accion requerida "CARGAR" y también vuelve el texto obtenido a mayusculas para poder comparar con la variable Op
        InstruccionInicial = Inicio[int(Buscar1.start()):int(Buscar1.end())]  # Obtiene la palabra buscada
        RestoEn = Inicio[Buscar1.end():len(Inicio)]  # Obtiene el resto del texto
        ArchivosJSON = re.sub('\s', '', RestoEn)  # Borra los espacios en blanco
        ArchivosJSON1 = re.split(',', ArchivosJSON)  # Identifica cada coma y crea una lista cada ves que encuentra una coincidencia
        for i in ArchivosJSON1:
            temporal = Pb.jsonread(i)
            Archivos.extend(temporal)
        ArchivosFin = Archivos
        Tamaño = len(ArchivosFin)
        print('╔═════════════════════════════════════════════════════════════════════════════════╗')
        print('║ CARGANDO....                                                                    ║', '\n║                                                                                 ║')
        print('║ CARGA DE ARCHIVOS COMPLETA                                                      ║')
        print('╚═════════════════════════════════════════════════════════════════════════════════╝')
    elif ArreglodeBusqueda[0] == 'MAXIMO':
        for P in range(1, len(ArreglodeBusqueda)):
            if ArreglodeBusqueda[P].strip() == 'EDAD':
                for L in range(0, len(ArchivosFin)):
                    B = ArchivosFin[L]['edad']
                    table.append(B)
                TableFin = table
                x = max(TableFin)
                print('╔══════════════════════════════════════╗')
                print('║ El Maximo de las Edades es: ', x)
                print('╚══════════════════════════════════════╝')
                TableFin.clear()
            elif ArreglodeBusqueda[P].strip() == 'PROMEDIO':
                for L in range(0, len(ArchivosFin)):
                    B = ArchivosFin[L]['promedio']
                    table1.append(B)
                TableFin = table1
                x = max(TableFin)
                print('╔════════════════════════════════════════╗')
                print('║ El Maximo de los Promedios es: ', x)
                print('╚════════════════════════════════════════╝')
                TableFin.clear()
    elif ArreglodeBusqueda[0] == 'MINIMO':
        for P in range(1, len(ArreglodeBusqueda)):
            print(type(P))
            if ArreglodeBusqueda[P].strip() == 'EDAD':
                for L in range(0, len(ArchivosFin)):
                    B = ArchivosFin[L]['edad']
                    table.append(B)
                TableFin = table
                x = min(TableFin)
                print('╔════════════════════════════════════════╗')
                print('║ El Minimo de las Edades es: ', x)
                print('╚════════════════════════════════════════╝')
                TableFin.clear()
            elif ArreglodeBusqueda[P].strip() == 'PROMEDIO':
                for L in range(0, len(ArchivosFin)):
                    B = ArchivosFin[L]['promedio']
                    table1.append(B)
                TableFin = table1
                x = min(TableFin)
                print('╔════════════════════════════════════════╗')
                print('║ El Minimo de los Promedios es: ', x)
                print('╚════════════════════════════════════════╝')
                TableFin.clear()
    elif ArreglodeBusqueda[0] == 'SUMA':
        for P in range(1, len(ArreglodeBusqueda)):
            if ArreglodeBusqueda[P].strip() == 'EDAD':
                for L in range(0, len(ArchivosFin)):
                    B = ArchivosFin[L]['edad']
                    table.append(B)
                TableFin = table
                x = sum(TableFin)
                print('╔════════════════════════════════════════╗')
                print('║ La suma de las Edades es: ', x)
                print('╚════════════════════════════════════════╝')
                TableFin.clear()
            elif ArreglodeBusqueda[P].strip() == 'PROMEDIO':
                for L in range(0, len(ArchivosFin)):
                    B = ArchivosFin[L]['promedio']
                    table1.append(B)
                TableFin = table1
                x = sum(TableFin)
                print('╔════════════════════════════════════════╗')
                print('║ La suma de los Promedios es: ', x)
                print('╚════════════════════════════════════════╝')
                TableFin.clear()
    elif ArreglodeBusqueda[0] == 'CUENTA':
        print('╔═════════════════════════════════════════════╗')
        print('║ El Numero de Registros Cargados es:', Tamaño)
        print('╚═════════════════════════════════════════════╝')
    elif ArreglodeBusqueda[0] == 'REGISTRO':

        CantidadR = ArreglodeBusqueda[1]
        CantidadRINT = int(CantidadR)
        for N in range(0,CantidadRINT):
            temp = ArchivosFin[N]
            RegistroTab.append(temp)
        TableFin = RegistroTab



        with open('ArchivoHTML.txt', 'w') as F:
            for T in TableFin:

                F.write('REGISTRO '+ T)
                F.write(str(T) + '\n')
                print(F)

        f = open('Reporte.html', 'wb')
        F.close()
        #mensaje = """<!DOCTYPE html>
        #<html lang="es">
        #<head>
#            <meta charset="UTF-8">
 #           <meta name="viewport" content="width=device-width, initial-scale=1.0">
  #          <title>SIMPLEQL</title>
   #         <link rel="icon" href="img\logoPython.png">
    #        <link href="https://fonts.googleapis.com/css2?family=Limelight&display=swap" rel="stylesheet">
     #       <link href="https://fonts.googleapis.com/css2?family=IM+Fell+DW+Pica+SC&display=swap" rel="stylesheet">
      #      <link href="https://fonts.googleapis.com/css2?family=Alata&display=swap" rel="stylesheet">
       #     <link rel="stylesheet" href="estilo.css">
       # </head>
#        <body>
 #       <div class="contenedor">
  #          <center>
   #         <header class="fila">
    #            <center><div id="logo" class="col-lg-12 col-md-12 col-sm-13 col-xs-12"><img src="asd-removebg-preview.png" height="60">
     #           SIMPLEQL</div></center>
      #      </header>
       #     </center>
        #    <section id="seccion4" class="fila">
         #       <aside id="izq" class="col-lg-3 col-md-3 col-sm-3 col-xs-12">
          #      </aside>
           #     <article class="col-lg-6 col-md-6 col-sm-6 col-xs-12">
            #        <center><h1>Reporte de Registros</h1></center>
             #       <center><iframe src="ArchivoHTML.txt" width="620"  style="border: solid;" title="REPORTE DE REGISTROS"></iframe></center>
              #  </article
               # <aside id="der" class="col-lg-3 col-md-3 col-sm-3 col-xs-12">
                #</aside>
          #  </section>
           # <footer class="fila">
            #    <div class="col-lg-12 col-md-12 col-sm-12 col-xs-12">&reg;201901907, BYRON ESTUARDO CAAL CATÚN</div>
            #</footer>
        #</div>
        #</body>
        #</html>""".encode()
        #f.write(mensaje)
        #f.close()
        #webbrowser.open_new_tab('Reporte.html')

    elif ArreglodeBusqueda[0] == 'SALIR':
        print('╔═══════════════════════════╗')
        print('║ SALIENDO DEL PROGRAMA.... ║')
        print('╚═══════════════════════════╝')

        sys.exit()
    elif ArreglodeBusqueda[0].strip() == 'SELECCIONAR':
        try:
            Buscar1 = re.search('SELECCIONAR', Valores)
            Buscar2 = re.search('DONDE', Valores)
            print(Valores)
            print(Buscar2)
            if Buscar2 != None:
                DespuesDeSelecAntDonde = Valores[Buscar1.end():Buscar2.start()]
                print(DespuesDeSelecAntDonde)
                Atributos = re.split(' ', DespuesDeSelecAntDonde.strip())
                print(Atributos)
                DespuesDonde = Valores[Buscar2.end():len(Inicio)]
                print(DespuesDonde)
                Condicion = re.split('=', DespuesDonde.strip())
                print(Condicion)
                comp = Condicion[0]
                print(comp)
                for A in ArchivosFin:
                    for C in Atributos:
                        for C in A:
                            Coincidencia = re.search(Atributos[C], ArchivosFin[A])
                            print(Coincidencia)
                for R in range(1, len(ArreglodeBusqueda)):
                    if ArreglodeBusqueda[R].strip() == '*':
                        for B in range(0, len(ArchivosFin)):
                            print('╔═════════════════════════════════════════════════════════════════════════════════╗')
                            print('║ ',ArchivosFin[B])
                            print('╚═════════════════════════════════════════════════════════════════════════════════╝')
                    for z in range(0, len(ArchivosFin)):
                        coins = re.search(comp, ArchivosFin[z])
                        Conditions = ArchivosFin[coins.start():coins.end()]
                        print(Conditions)


            else:
                for R in range(1, len(ArreglodeBusqueda)):
                    if ArreglodeBusqueda[R].strip() == '*':
                        for B in range(0, len(ArchivosFin)):
                            print('╔═════════════════════════════════════════════════════════════════════════════════╗')
                            print('║ ',ArchivosFin[B])
                            print('╚═════════════════════════════════════════════════════════════════════════════════╝')
        except:
            print('DE ESTA FUNCION SOLO IMPRIME TODOS, *')

#seleccionar nombre edad activo promedio Donde nombre="Billy Anderson"
    #cargar practica1.json, practica2.json, practica3.json
    else:
        print('ERROR, NO IDENTIFICADO, REVISE SU SINTAXIS')
        print(Condicion)