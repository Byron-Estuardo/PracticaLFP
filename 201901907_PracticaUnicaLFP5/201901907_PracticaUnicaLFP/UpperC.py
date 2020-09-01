            Buscar1 = re.search('SELECCIONAR', Inicio, re.IGNORECASE)
            InstruccionBuscar = Inicio[int(Buscar1.start()):int(Buscar1.end())]
            Buscar2 = re.search('DONDE', Inicio, re.IGNORECASE)
            InstruccionBuscar1 = Inicio[int(Buscar2.start()):int(Buscar2.end())]
            DespuesDeSelecAntDonde = Inicio[Buscar1.end():Buscar2.start()]
            Lista1 = re.split(' ', DespuesDeSelecAntDonde.strip().upper())
            print(Lista1)
            DespuesDonde = Inicio[Buscar2.end():len(Inicio)]
            print(DespuesDonde)
            SinComillas = re.sub('"', ' ', DespuesDonde)
            print(SinComillas)
            DosPuntos = re.sub('=', ':', SinComillas)
            Mari = DosPuntos.strip()
            print(Mari)
            Comparar = re.split(' ', Mari)
            print(Comparar[0])



