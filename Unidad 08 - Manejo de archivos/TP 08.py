#1. Crear archivo inicial con productos: Crear un archivo de texto llamado 
#productos.txt con tres productos. Cada línea debe tener:  nombre,precio,cantidad 
def crear_archivo(selector):
    if selector=='w' or selector=='a':
        with open ('productos.txt', f'{selector}') as archivo:
            if selector=='w':
                archivo.write('nombre,precio,cantidad\n')
            archivo.write('Lapicera,150.5,30\n')
            archivo.write('Cuaderno,320.0,20\n')
            archivo.write('Borrador,90,50\n')
    else:
        print('Opcion invalida.')

#2. Leer y mostrar productos: Crear un programa que abra productos.txt, lea cada 
#línea, la procese con .strip() y .split(","), y muestre los productos en el siguiente 
#formato: 
#Producto: Lapicera | Precio: $120.5 | Cantidad: 30
def lista_productos():
    with open ('productos.txt', 'r') as archivo:
        for linea in archivo:
            producto=linea.strip().split(',')
            if producto[0]=='nombre':
                continue
            else:
                print(f'Producto: {producto[0]} | Precio: ${producto[1]} | Cantidad: {producto[2]}')
        return
#3. Agregar productos desde teclado: Modificar el programa para que luego de mostrar 
#los productos, le pida al usuario que ingrese un nuevo producto (nombre, precio, 
#cantidad) y lo agregue al archivo sin borrar el contenido existente.
def agregar_productos():    
    nombre=input('Ingrese el nombre del producto que desea agregar: ')
    precio=input('Ingrese el precio del producto: ')
    cantidad=input('Ingrese la cantidad del producto: ')
    with open ('productos.txt', 'a') as archivo:
        archivo.write(f'{nombre},{precio},{cantidad}\n')
    return
#4. Cargar productos en una lista de diccionarios: Al leer el archivo, cargar los datos en 
#una lista llamada productos, donde cada elemento sea un diccionario con claves: 
#nombre, precio, cantidad. 
productos=[]
def lista_diccionario():
    with open ('productos.txt', 'r') as archivo:
        for linea in archivo:
            producto=linea.strip().split(',')
            if producto[0]=='nombre':
                continue
            else:
                productos.append({'nombre':producto[0],'precio':producto[1],'cantidad':producto[2]})
        print(productos)
    return productos
#5. Buscar producto por nombre: Pedir al usuario que ingrese el nombre de un 
#producto. Recorrer la lista de productos y, si lo encuentra, mostrar todos sus datos. Si 
#no existe, mostrar un mensaje de error. 
def buscar_producto():
    nombre=input('Ingrese el nombre del producto para buscarlo: ').strip().lower()
    encontrado=False
    with open ('productos.txt', 'r') as archivo:
        for producto in archivo:
            producto=producto.strip().split(',')
            if producto[0]=='nombre':
                continue
            if nombre==producto[0].lower():
                encontrado=True
                print(f'Producto: {producto[0]} | Precio: ${producto[1]} | Cantidad: {producto[2]}')
                break
        if encontrado==False:
            print('Error. El producto no existe.')
    return

def menu():
    print('1) Listar productos')
    print('2) Agregar productos')    
    print('3) Listar productos como diccionario')
    print('4) Buscar productos')
    print('5) Abrir o crear archivo')
    print('6) Salir')
opcion=''
while opcion != '6':
    menu()
    opcion=input('Ingrese una opcion: ')
    match opcion:
        case '1':
            lista_productos()
        case '2':
            agregar_productos()
        case '3':
            lista_diccionario()
        case '4':
            buscar_producto()
        case '5':
            selector=input('Ingrese la opción w, para sobreescribir el archivo desde cero, o la opcion a, para continuar trabajando sobre el archivo: ').lower().strip()
            crear_archivo(selector)
        case '6':
            break
        case _:
            print('Opción invalida. Intente nuevamente.')
            continue