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
    ejemplares=input('Ingrese la cantidad de ejemplares que desea agregar: ').strip()
    while True:
        if not ejemplares.isdigit() or ejemplares =='':
            ejemplares=input("====== ERROR ======\nDebe ingresa un digito. Intente nuevamente: ").strip()
            continue
        ejemplares=int(ejemplares)
        if ejemplares<0:
            ejemplares=input("====== ERROR ======\nDebe ingresar un digito mayor o igual a cero. Intente nuevamente: ").strip()
            continue
        break
    return ejemplares 
def validacion_titulos(titulos_existentes):

    nombre=input(f'Ingrese un titulo para agregarlo a la Biblioteca: ').strip()
    
    while True:
        if nombre.lower() in titulos_existentes:
            nombre=input("====== ERROR ======\nEl libro ingresado ya existe. Intente con otro: ").strip()
            continue
        if nombre=='':
            nombre=input("====== ERROR ======\nNo ha ingresado ningún título. Intente nuevamente: ").strip()
            continue
        break
    return nombre
def buscar_titulo(titulos_existentes):
    titulo=input('Ingrese el titulo deseado: ').strip()
    while True:
        if titulo.lower() in titulos_existentes:
    if titulo 
    return
def ingresar_titulos():
    cantidad=validacion_digitos()

    libros=catalogo()
    titulos_existentes=[]
    for libro in libros:
        titulos_existentes.append(libro['titulo'].lower())

    nuevos_libros=[]
    for i in range (cantidad):
        
        nombre=validacion_titulos(titulos_existentes)
        ejemplares=validacion_ejemplares()
        nuevos_libros.append({'titulo':nombre, 'ejemplares':ejemplares})

        titulos_existentes.append(nombre.lower())

    with open (nombre_archivo, 'a', newline='', encoding='utf-8') as archive:
        escritor=csv.DictWriter(archive, fieldnames=['titulo', 'ejemplares'])
        escritor.writerows(nuevos_libros)
    print('='*60,'\n El catalogo de libros se ha actualizado correctamente!')
    mostrar_catalogo()
    print('='*60)


def ingresar_ejemplares():
     catalogo=mostrar_catalogo()


while opcion != "8":
    menu()
    opcion=input("Opción:").strip()
    match opcion:
        case "1":
            ingresar_titulos()
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