def registrarnotas():

    estudiantes= {}

    while True:
        nombre =input("Ingrese el nombre del estudiante: ")

        nota= input("Nota :")

        estudiantes[nombre]= int (nota)

        seguir= input("Desea ingresar otra nota? (s/n): ")

        if seguir.lower() != 's':
            break

        
    
    return estudiantes

resultado = registrarnotas()
print("Notas registradas:")
print (resultado)