def cliente (informacion:dict) -> dict:
    diccionario = {}
    diccionario['nombre'] = informacion['nombre']
    diccionario['edad'] = informacion['edad']
    
    
    if diccionario['edad'] > 18:
        diccionario['atraccion'] = "X-Treme"
        diccionario['apto'] = True
        if informacion['primer_ingreso']:
            valorBoleta = 20000*0.95
        else:
            valorBoleta = 20000
    elif diccionario['edad'] >= 15:
        diccionario['atraccion'] = 'Carros chocones'
        diccionario['apto'] = True
        if informacion['primer_ingreso']:
            valorBoleta = 5000*0.93
        else:
            valorBoleta = 5000
    elif diccionario['edad'] >= 7:
        diccionario['atraccion'] = 'Sillas voladoras'
        diccionario['apto'] = True
        if informacion['primer_ingreso']:
            valorBoleta = 10000*0.95
        else:
            valorBoleta = 10000
    else:
        diccionario['atraccion'] = 'N/A'
        diccionario['apto'] = False
        valorBoleta = 'N/A'
    
    diccionario['primer_ingreso'] = informacion['primer_ingreso']
    diccionario['total_boleta'] = valorBoleta
    return diccionario