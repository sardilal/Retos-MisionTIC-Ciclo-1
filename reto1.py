def CDT(cliente: str, capital: int, tiempo: int):
    if tiempo > 2:
        PorcentajeInteres = 0.03
        ValorIntereses = capital*PorcentajeInteres*tiempo/12
        ValorTotal = ValorIntereses+capital
    else:
        PorcentajePerder = 0.02
        ValorPerder = capital*PorcentajePerder
        ValorTotal = capital-ValorPerder
    
    return(f'Para el usuario {cliente} La cantidad de dinero a recibir, según el monto inicial {capital} para un tiempo de {tiempo} meses es: {ValorTotal}')

print(CDT("AB1012", 1000000, 3))
print(CDT("ER3366", 650000, 2))
        