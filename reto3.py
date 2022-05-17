def AutoPartes(ventas: list) -> list:
    diccionarios = []
    for tupla in ventas:
        diccionario = {
            "IdProducto" : tupla[0],
            "dProducto"  : tupla[1],
            "pnProducto" : tupla[2],
            "cvProducto" : tupla[3],
            "sProducto"  : tupla[4],
            "nComprador" : tupla[5],
            "cComprador" : tupla[6],
            "fVenta"     : tupla[7]
        }
        
        diccionarios.append(diccionario)
    
    return diccionarios

def consultaRegistro(ventas:list, idProducto:int):
    diccionarios = ventas
    esta = False
    for diccionario in diccionarios:
        if not diccionario["IdProducto"] == idProducto:
            continue
        else:
            print(f'Producto consultado : {diccionario["IdProducto"]}  Descripción  {diccionario["dProducto"]}  #Parte  {diccionario["pnProducto"]}  Cantidad vendida  {diccionario["cvProducto"]}  Stock  {diccionario["sProducto"]}  Comprador {diccionario["nComprador"]}  Documento  {diccionario["cComprador"]}  Fecha Venta  {diccionario["fVenta"]}')
            esta = True
    if not esta:
        print("No hay registro de venta de ese producto")