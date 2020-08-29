import json
import re

lista = []
listAux = []

class texto:
    def __init__(self, nombre, edad, activo, promedio):
        self.nombre = nombre
        self.edad = edad
        self.activo = activo
        self.promedio = promedio

def subirArch:
    try:
        nom = (input("~Ingrese la Instruccion: "))
        Buscar1 = re.search('CARGAR', nom.upper())
        InstruccionInicial = nom[int(Buscar1.start()):int(Buscar1.end())]
        Comparacion = str(InstruccionInicial)
        RestoEn = nom[Buscar1.end():len(nom)]
        ArchivosJSON = re.sub('\s', '', RestoEn)
        ArchivosJSON1 = re.split(',', ArchivosJSON)
        if 'CARGAR' == Comparacion.upper():
            for i in ArchivosJSON1:
                with open(ArchivosJSON1) as FileU:
                    reader = json.load(FileU)

    except:
        print('F')