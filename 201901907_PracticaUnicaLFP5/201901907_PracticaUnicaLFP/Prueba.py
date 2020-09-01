def jsonread(ArchivoEntr):
    import json
    FileU = open(f'{ArchivoEntr}',)
    reader = json.load(FileU)
    FileU.close()
    lista = list()
    for jsons in reader:
        lista.append(jsons)
    return reader