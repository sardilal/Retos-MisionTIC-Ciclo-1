def ordenes(rutinaContable:list):
    totales =tuple(map(lambda lista: sum(tuple(map(lambda tupla: tupla[1]*tupla[2], lista[1:]))), rutinaContable))
   
    print ('----------------- Inicio Registro diario --------------------------')
    for i in range(len(rutinaContable)):
        print (f'La factura {rutinaContable[i][0]} tiene un total en pesos de {round( totales[i] if totales[i] >= 600000 else (totales[i] + 25000), 2 )}')
    
    print('----------------- Fin Registro diario -----------------------------')
    
ordenes([
[1201, ("5464", 4, 25842.99), ("7854",18,23254.99), ("8521", 9, 48951.95)],
[1202, ("8756", 3, 115362.58),("1112",18,2354.99)],
[1203, ("2547", 1, 125698.20), ("2635", 2, 135645.20), ("1254", 1, 13645.20),("9965", 5, 1645.20)],
[1204, ("9635", 7, 11.99), ("7733",11,18.99), ("88112", 5, 390.95)]
])

