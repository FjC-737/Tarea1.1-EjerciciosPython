#Cree un programa que elimine los elementos repetidos de una lista y devuelva una nueva lista con elementos únicos ordenados

def eliminarDuplicadosyOrdenar(lista):

    unicos= []
    
    for numero in lista:
        if numero not in unicos:
            unicos.append(numero)

    unicos.sort()

    return unicos


entrada = [4, 2, 7, 4, 2, 1, 9, 7]
resultado = eliminarDuplicadosyOrdenar(entrada)
print(resultado)
