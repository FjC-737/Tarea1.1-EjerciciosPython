ventas = {
    'Producto': ['A', 'B', 'A', 'C', 'B', 'A'],
    'Cantidad': [10, 5, 7, 3, 2, 8]
}

ventas_totales = {}

for i in range(len(ventas['Producto'])):
    producto = ventas['Producto'][i]
    cantidad = ventas['Cantidad'][i]

    if producto in ventas_totales:
        ventas_totales[producto] = ventas_totales[producto] + cantidad
    else:
        ventas_totales[producto] = cantidad


print(ventas_totales)
