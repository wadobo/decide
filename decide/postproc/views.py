from rest_framework.views import APIView
from rest_framework.response import Response
import math


import math
import copy

class PostProcView(APIView):


    def ley_de_hondt(self,listaEscaños,escañosTotales):

        numEscañosRepartidos = 0
        
        #inicializamos la lista con el num de escaños y cociente por partido a 0
        for x in listaEscaños:
             x.update({ 
                        'cociente' : 0,
                        'escanyos' : 0 })


        #Hacer lo siguiente HASTA que el numero de escaños repartidos y el real sean el mismo
        while(numEscañosRepartidos != escañosTotales):

            #Calculamos en primer lugar los cocientes para cada partido en la iteracion
            for x in listaEscaños:

                    esc = int(x.get('escanyos'))
                    ci = x.get('votes')/(esc+1)
                    print(ci)
                    x.update({ 'cociente' : ci})

                
            mayor_cociente = 0 

            #Una vez hecho esto, sacamos el mayor cociente de todos en esta iteracion
            for x in listaEscaños:
               if(x.get('cociente') > mayor_cociente):
                   mayor_cociente = x.get('cociente')

            #Finalmente, vemos a que partido pertenece dicho cociente mayor y , en caso de ser el suyo,
            #se le otarga como ganador 1 escaño mas y ninguno al resto de partidos
            for x in listaEscaños:
               if(x.get('cociente') == mayor_cociente):
                   x.update({'escanyos':x.get('escanyos')+1})
                
               else:
                   x.update({'escanyos':x.get('escanyos')})
                
            numEscañosRepartidos =  numEscañosRepartidos + 1
        
        #Finalmente le damos el formato de la coleccion que recibe el test para hacer la comprobaciones pertinentes
        #y eliminamos el campo cociente
        for x in listaEscaños:
            x.pop('cociente')

        return listaEscaños


    def metodoHuntington_Hill(self,data,escanyos):

        #Calculamos el numero de votos totales
        totalVotes = 0
        for x in data:
            totalVotes += x['votes']

        #Calculamos el divisor
        d = totalVotes/escanyos

        #Creamos divisores un 0.1% inferior y superior por si necesitamos otro divisor
        dpercent = d*0.001
        dinf = d-dpercent
        dsup = d+dpercent

        #Creamos la lista de partidos con sus escaños y el numero de escaños que ha repartido nuestro metodo
        reparto = data
        numEscanyosRepartidos = 0

        #Creamos un contador para evitar el bucle infinito. 1000 vueltas como maximo es suficiente
        contador = 0

        #Hacer lo siguiente HASTA que el numero de escaños repartidos y el real concuerden
        while(numEscanyosRepartidos != escanyos and contador<1000):
            contador +=1

            #Reseteamos la lista y el numero de escaños repartidos por si nos hemos equivocado de divisor
            reparto = data
            numEscanyosRepartidos = 0

            #Por cada partido...
            for x in reparto:

                #Si sus votos no superan el divisor pues no tendran escaños
                if(x['votes']<d):
                    x['escanyos']=0
                
                #Si sus votos superan el divisor...
                else:
                    
                    #Creamos la cuota de cada partido, en base al divisor actual
                    quota = x['votes']/d
                    
                    #Si la cuota es un entero el numero de escaños es, directamente, la cuota
                    if(int(quota) == quota):
                        x['escanyos']=int(quota)
                    
                    #Si la cuota no es un entero...
                    else:
                        
                        #Calculamos las cotas superior e inferior de la cuota y despues la media geometrica
                        lQ = int(quota)
                        hQ = lQ+1
                        gM = math.sqrt(lQ*hQ)

                        #Si la cuota es superior a la media geometrica el numero de escaños es la cota sup.
                        if(quota > gM):
                            x['escanyos']=hQ

                        #Si la cuota es inferior a la media geometrica el numero de escaños es la cota inf.
                        else:
                            x['escanyos']=lQ
            
            #Una vez rellenada la lista calculamos cuantos escaños hemos utilizados en nuestro reparto
            for x in reparto:
                numEscanyosRepartidos += x['escanyos']
            
            #Si el numero de escaños utilizados es menor que el real disminuimos el divisor
            if(numEscanyosRepartidos < escanyos):
                d = dinf
                dinf = d-dpercent
                dsup = d+dpercent

            #Si el numero de escaños utilizados es mayor que el real aumentamos el divisor
            else:
                d = dsup
                dinf = d-dpercent
                dsup = d+dpercent
            
            #Como cuanto mayor menor divisor mayor cuota (quota=numVotos/divisor) es mas facil para un partido
            # que su cuota supere la media geometrica, por lo que, el proximo intento, es muy posible que
            # aumenten los escaños, solucionando el problema. Para el caso de demasiados escaños se aplicaria
            # el metodo inverso, mayor divisor > menor cuota > menos posibilidad de obtener escaños
            #
            #Si el divisor da problemas lo mejor sera cambiar el 'dpercent' ya que este determina la variacion
            # de divisor que se produce con cada intento, cuanto menor porciento de d menos posiblidad de
            # saltarse el divisor correcto pero mayor cantidad de vueltas se darian al bucle (Eficiencia = 1/Precision)
        
        return Response(reparto)

    # Método de reparto de escaños mediante el Cociente Hare
    # Type: HARE
    # Realizado por Fran
    def hare(self, options, numSeats):

        out = []
        inputData = {}
        results = {}
        quotient = 0

        # Formateo de la entrada
        for opt in options:
            i = opt['number']
            v = opt['votes']
            inputData[i] = v

        totalVotes = self.votesSum(inputData)
        quotient = math.floor(totalVotes/numSeats)

        # Tratamos el caso extremo en el que una votacion tenga 0 votos
        if quotient != 0:
            results = self.residueDistribution(self.seatsAndResidues(inputData, quotient), numSeats)

            print('OK',results)

            # Formateo de la salida añadiendo la distribucion de escaños calculada
            for index, opt in enumerate(options, start = 1):
                out.append({
                    **opt,
                    'escanyos': results.get(index)[0],
                })

        # Consideramos la votacion invalida y devolvemos todos las opciones con 0 escaños asignados
        else:
            for index, opt in enumerate(options, start = 1):
                out.append({
                    **opt,
                    'escanyos': 0,
                })

        return Response(out)

    # Sumatorio de los votos totales
    def votesSum(self, allVotes):
        sum = 0
        for x in allVotes.values():
            sum += x
        return sum       

    # Primera repartición de escaños y cálculo de los votos 
    # residuo para cada partido
    def seatsAndResidues(self, data, quotient):
        res = {}
        for index, x in enumerate(data.values(), start = 0):
            a = []

            seats = math.floor(x/quotient)
            
            residue = x - quotient*seats

            a.append(seats)
            a.append(residue)

            key_list = list(data.keys()) 
            n = key_list[index]

            res[n] = a

        return res

    # Segunda repatición teniendo en cuenta el nº de escaños 
    # aún sin repartir y los votos residuos
    def residueDistribution(self, initalDist, numSeats):
        distSeats = 0
        n = 0
        residues = []
        finalDist = copy.deepcopy(initalDist)
        values = finalDist.values()

        for x in values:
            distSeats += x[0]
            residues.append(x[1])

        notDistributed = numSeats - distSeats
        sortedResidues = residues.copy()
        sortedResidues.sort(reverse = True)

        while notDistributed > 0:
            selected = sortedResidues[n]
            pos = residues.index(selected)

            notDistributed -= 1

            list(values)[pos][0] += 1

            n += 1

        return finalDist

    def identity(self, options):
        out = [] 

        for opt in options:
            out.append({
                **opt,
                'postproc': opt['votes'],
            });

        out.sort(key=lambda x: -x['postproc'])

        return Response(out)

    def cocienteImperiali(self, numEscanyos, datos):
        #Obtenemos los votos totales de la votacion
        totalVotos = self.sumaVotos(datos)

        if totalVotos > 0 and numEscanyos > 0:

            #Calculamos el cociente y lo redondeamos
            q = round(totalVotos / (numEscanyos + 2), 0)
  
            #Realizamos la primera asignación de los escaños
            #y lo añadimos a la lista de datos
            for x in datos:
                ei = math.trunc(x['votes']/q)
                x.update({'escanyos' : ei})
  
            #Calculamos el número de escaños asignados
            escanyosAsignados = self.sumaEscanyos(datos)

            #Si quedan escaños por asignar....
            if(escanyosAsignados < numEscanyos):
                #Calculamos los votos de residuo para añadirlo a la lista según al partido que corresponda
                for x in datos:
                    x.update({ 
                        'escanyosResiduo' : x['votes'] - (q * x['escanyos'])})

                #Ordenamos la lista por los votos de residuo
                datos.sort(key=lambda x : -x['escanyosResiduo'])

                #Mientras quedan escaños por asignar, recorremos la lista de votos de residuo y le sumamos +1 al numero de escaños del partido correspondiente
                for x in datos:
                    while(escanyosAsignados < numEscanyos):
                        x.update({
                        'escanyos' : x['escanyos'] + 1})
                        escanyosAsignados = escanyosAsignados + 1
      
                    #Eliminamos el campo de votos de residuo de la lista
                    x.pop('escanyosResiduo')

                #Ordenamos la lista por escaños antes de devolverla
            datos.sort(key=lambda x : -x['escanyos'])
            
            return Response(datos)
        else:
            for x in datos:
                x.update({'escanyos' : 0})
            return Response(datos)
    

    #Método que calcula el número de votos en la votación
    def sumaVotos(self, datos):
        suma = 0
        for x in datos:
            suma = suma + x['votes']
  
        return suma

    #Método que calcula el número de escaños asignados
    def sumaEscanyos(self, datos):
        suma = 0
        for x in datos:
            suma = suma + x['escanyos']
  
        return suma


        #Recuento borda. Realizado por Raúl.
    def borda(self, options):
        salida = {}
        #salida = options
        boole = False

        #Cada "opcion" es un diccionario de la lista options
        for opcion in options:
            #dicc= {}
            if len(opcion['positions']) != 0:
                suma_total_opcion = 0
                for posicion in opcion['positions']:
                    valor = len(options) - posicion + 1
                    suma_total_opcion += valor
                salida[opcion['option']] = suma_total_opcion
                opcion['votes'] = suma_total_opcion

            else:
                salida = {}
                boole = True
                break
        if boole == True:
            for opcion in options:
                opcion['votes'] = 0
        return Response(options)


    def post(self, request):
        """
         * type: IDENTITY | EQUALITY | WEIGHT | BORDA
         * options: [
            {
             option: str,
             number: int,
             votes: int,
             ...extraparams
            }
           ]
        """

        t = request.data.get('type', 'IDENTITY')
        opts = request.data.get('options', [])
        numEscanyos = request.data.get('numEscanyos', 0)
        
        if t == 'IDENTITY':
            return self.identity(opts)
        elif t == 'COCIENTE_IMPERIALI':
            return self.cocienteImperiali(numEscanyos, opts)
        elif t == 'BORDA':
            return self.borda(opts)
        elif t == 'HARE':
            return self.hare(opts, numEscanyos)
        elif t == 'HUNTINGTON_HILL':
            return self.metodoHuntington_Hill(opts,numEscanyos)

        return Response({})

    def metodoHondt(self, data):
        t = data.get('type')
        lista = data.get('options')
        escañosTotales = data.get('numEscanyos')
        if(t == 'HONDT'):
            return self.ley_de_hondt(lista,escañosTotales)
        else:
            return {}
