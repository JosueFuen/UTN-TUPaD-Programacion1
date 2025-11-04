import csv
import os
nombre_archivo= 'libros.csv'
opcion=''
if not os.path.exists('libros.csv'):
    with open (nombre_archivo, 'w', newline='', encoding='utf-8') as archivo:
        csv.DictWriter(archivo, fieldnames=['titulo','ejemplares']).writeheader()

def menu():
    print("\n           📚  MENÚ DE LA BIBLIOTECA  📚")
    print("1)   Ingresar títulos")
    print("2)   Ingresar ejemplares")
    print("3)   Mostrar catálogo")
    print("4)   Consultar disponibilidad")
    print("5)   Listar agotados")
    print("6)   Agregar título")
    print("7)   Actualizar ejemplares(préstamo/devolución)")
    print("8)   Salir")

def catalogo():
    libros=[]
    with open (nombre_archivo, newline='', encoding='utf-8') as archivo:
        lector=csv.DictReader(archivo)
        for fila in lector:
            libros.append({'titulo':fila['titulo'], 'ejemplares':int(fila['ejemplares'])})
    return libros

def mostrar_catalogo():
    libros=catalogo()
    if not libros:
        pausa=input("No hay títulos que mostrar. Presione enter para continuar")
    else:
        print('='*60)
        print("------   CATÁLOGO DE LIBROS    ------\n")
        for i, libro in enumerate(libros, start=1):
            print(f"{i}) - Título: {libro['titulo']} - Ejemplares: {libro['ejemplares']}")
        print("="*60)
        pausa=input("Presione enter para continuar:")
def validacion_digitos():
    print('='*60)
    cantidad=input("Indique la cantidad de titulos que desea ingresar a la biblioteca:").strip()
    while True:
        if not cantidad.isdigit() or cantidad =='':
            cantidad=input("====== ERROR ======\nDebe ingresa un digito. Intente nuevamente: ").strip()
            continue
        cantidad=int(cantidad)
        if cantidad<1:
            cantidad=input("====== ERROR ======\nDebe ingresar un digito mayor a cero. Intente nuevamente: ").strip()
            continue
        return cantidad

def validacion_ejemplares():
    cantidad=validacion_digitos()
    nuevos_titulos=validacion_libros()
    nuevos_ejemplares=[]
    for i in range (cantidad):
        ejemplares=input(f'Ingrese la cantidad de ejemplares del libro {nuevos_titulos[i]: }').strip()
        while True:
            if not ejemplares.isdigit() or ejemplares =='':
                ejemplares=input("====== ERROR ======\nDebe ingresa un digito. Intente nuevamente: ").strip()
                continue
            ejemplares=int(ejemplares)
            if ejemplares<0:
                ejemplares=input("====== ERROR ======\nDebe ingresar un digito mayor o igual a cero. Intente nuevamente: ").strip()
                continue
            break
        nuevos_ejemplares.append(ejemplares)
    return nuevos_ejemplares
def validacion_libros():
    cantidad=validacion_digitos()
    libros=catalogo()
    titulos_existentes=[]

    for libro in libros:
        titulos_existentes.append(libro['titulo'].lower())

    nuevos_titulos=[]
    for i in range (cantidad):
        nombre=input(f'Ingrese el titulo {i+1} para agregarlo a la Biblioteca: ').strip()
        
        while True:
            if nombre.lower() in titulos_existentes:
                nombre=input("====== ERROR ======\nEl libro ingresado ya existe. Intente con otro: ").strip()
                continue

            if nombre=='':
                nombre=input("====== ERROR ======\nNo ha ingresado ningún título. Intente nuevamente: ").strip()
                continue
            break
        nuevos_titulos.append(nombre)
    return nuevos_titulos
    
def ingresar_titulos():
    nuevos_titulos=validacion_libros()
    nuevos_ejemplares=validacion_ejemplares()
    cantidad=validacion_digitos()
    nuevos_libros=[]

    for i in range (cantidad):
        nuevos_libros(i)=[{'titulo':nuevos_titulos[i], 'ejemplares':nuevos_ejemplares[i]}]

    with open (nombre_archivo, 'a', newline='', encoding='utf-8') as archive:
        escritor=csv.DictWriter(archive, fieldnames=['titulo', 'ejemplares'])
        escritor.writerow(nuevos_libros)
    print('='*60,'\n El catalogo de libros se ha actualizado correctamente!')
    mostrar_catalogo()
    print('-'*60)
    pausa=input('Presione enter para continuar: ')

while opcion != "8":
    menu()
    opcion=input("Opción:").strip()
    match opcion:
        case "1":
            ingresar_titulos()
            continue
        case "2":
            #ingresar_ejemplares()
            continue
        case "3":
            mostrar_catalogo()
        case "4":
            #consultar_disponibilidad()
            continue
        case "5":
            #listar_agotados()
            continue
        case "6":
            #agregar_titulo()
            continue
        case "7":
            continue
            #actualizar_ejemplares()
        case "8":
            print("Hasta luego!")
            break
        case _:
            pausa=input("Opción invalida. Presione enter para continuar: ")