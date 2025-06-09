def encontrar_mayor(lista): 
    mayor = lista[0]

    for numero in lista: 
        if mayor < numero: 
            mayor = numero
    
    return mayor

numeros = [3, 9, 4, 1, 15]
resultado = encontrar_mayor(numeros)
print(resultado)