def ordenes(rutinaContable:list):
    totales =tuple(map(lambda lista: sum(tuple(map(lambda tupla: tupla[1]*tupla[2], lista[1:]))), rutinaContable))
   
    print ('------------------------ Inicio Registro diario ---------------------------------')
    for i in range(len(rutinaContable)):
        print (f'La factura {rutinaContable[i][0]} tiene un total en pesos de {round( totales[i] if totales[i] >= 600000 else (totales[i] + 25000), 2 ):,}')
    
    print('-------------------------- Fin Registro diario ----------------------------------')