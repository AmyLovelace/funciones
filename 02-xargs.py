def suma(*numeros): #asterisco en el parametro determina que es un dato iterable
    resultado = 0
    for numero in numeros:
        resultado += numero
    print(resultado)

suma(2, 5, 7)#iterable (2,5,7) se les puede agregar FOR
suma(2,5)
suma(2, 8, 7, 45, 32)
