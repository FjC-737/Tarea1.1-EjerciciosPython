# Escriba un programa que solicite un numero al usuario y muestre la tabla de multiplicar del 1 al 10 de ese numero.

numero = int(input("Introduzca un numero: "))

for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")