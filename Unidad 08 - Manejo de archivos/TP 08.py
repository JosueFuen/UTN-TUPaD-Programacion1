#1. Crear archivo inicial con productos: Crear un archivo de texto llamado 
#productos.txt con tres productos. Cada línea debe tener:  nombre,precio,cantidad 
with open ('productos.txt', 'w',newline='', encoding='utf-8') as archivo:
    archivo.write('nombre,precio,cantidad\n')

#2. Leer y mostrar productos: Crear un programa que abra productos.txt, lea cada 
#línea, la procese con .strip() y .split(","), y muestre los productos en el siguiente 
#formato: 
#Producto: Lapicera | Precio: $120.5 | Cantidad: 30
with open ('productos.txt', 'r', newline='', encoding='utf-8') as archivo:
    leer=archivo.readlines
    leer.strip()
    leer.split('|')
    