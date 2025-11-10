import csv
import os
nombre_archivo= 'libros.csv'
opcion=''
#------VALIDA QUE NO EXISTA EL ARCHIVO 'libros.csv', para crearlo solo si no existe.
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


##############################FUNCIONES COMPLEMENTARIAS#################################

#-------LEE EL CATALOGO DE LIBROS DESDE EL ARCHIVO 'libros.csv'
def catalogo():
    libros=[]
    with open (nombre_archivo, newline='', encoding='utf-8') as archivo:
        lector=csv.DictReader(archivo)
        for fila in lector:
            libros.append({'titulo':fila['titulo'], 'ejemplares':int(fila['ejemplares'])})
    return libros

#---------ES UNA FUNCIÓN QUE SE ENCARGA DE MOSTRAR EL CATALOGO DE LIBROS
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
    
#--------- VALIDA QUE EL CARACTER INGRESADO SEA UN DIGITO.
#Se utiliza el num, para poder reutilizar la función, ya que esta validación se usa en casos, 
# donde el numero tiene que ser mayo a cero y en otros que tiene que ser mayor a uno
def validacion_digitos(num):
    print('='*60)
    cantidad=input("Indique la cantidad de titulos que desea ingresar a la biblioteca:").strip()
    while True:
        if not cantidad.isdigit() or cantidad =='':
            cantidad=input("====== ERROR ======\nDebe ingresa un digito. Intente nuevamente: ").strip()
            continue
        cantidad=int(cantidad)
        if cantidad<num:
            cantidad=input(f"====== ERROR ======\nDebe ingresar un digito mayor a {num}. Intente nuevamente: ").strip()
            continue
        return cantidad

#----------- VALIDA QUE LA CANTIDAD DE EJEMPLARES SEA MAYOR A LAS INDICADAS POR num
def validacion_ejemplares(num):
    ejemplares=input('Ingrese la cantidad de ejemplares que desea agregar: ').strip()
    while True:
        if not ejemplares.isdigit() or ejemplares =='':
            ejemplares=input("====== ERROR ======\nDebe ingresa un digito. Intente nuevamente: ").strip()
            continue
        ejemplares=int(ejemplares)
        if ejemplares<num:
            ejemplares=input("====== ERROR ======\nDebe ingresar un digito mayor o igual a {num}. Intente nuevamente: ").strip()
            continue
        break
    return ejemplares 

#--------- CREA UNA LISTA CON SOLO LOS TITULOS DE LOS LIBROS, QUE LUEGO SE UTILIZA PARA VALIDAR
def lista_titulos():
    libros=catalogo()
    titulos_existentes=[]
    for libro in libros:
        titulos_existentes.append(libro['titulo'].lower())
    return titulos_existentes

#-------- SE ENCARGA DE VALIDAR QUE EL TITULO INGRESADO **NO** SE ENCUENTRE EN EL CATALOGO
# Para ello, compara el titulo ingresado, con la lista de titulos existentes.
def validacion_titulos(titulos_existentes):
    nombre=input(f'Ingrese un titulo para agregarlo a la Biblioteca: ').strip()
    while True:
        if nombre.lower() in titulos_existentes:
            nombre=input("====== ERROR ======\nEl libro ingresado ya existe. Intente con otro: ").strip()
            continue
        elif nombre=='':
            nombre=input("====== ERROR ======\nNo ha ingresado ningún título. Intente nuevamente: ").strip()
            continue
        break
    return nombre
#-------- SE ENCARGA DE VALIDAR QUE EL TITULO INGRESADO **SI** SE ENCUENTRE EN EL CATALOGO
# Para ello, compara el titulo ingresado, con la lista de titulos existentes.
def buscar_titulo(titulos_existentes):
    titulo=input('Ingrese el titulo deseado: ').strip()
    while True:
        if titulo.lower() not in titulos_existentes:
            titulo=input("====== ERROR ======\nEl titulo ingresado no existe. Intente nuevamente: ").strip()
            continue
        elif titulo=='':
            titulo=input("====== ERROR ======\nNo ha ingresado ningún título. Intente nuevamente: ").strip()
            continue
        break
    return titulo


############################FUNCIONES PRINCIPALES############################################


#----- SE ENCARGA DE COMPROBAR LA EXISTENCIA DE UN LIBRO Y SI EXISTE, TE DICE CUANTO EJEMPLARES TIENE EL LIBRO
def consultar_disponibilidad():
    titulos_existentes=lista_titulos()
    libros=catalogo()
    titulo=buscar_titulo(titulos_existentes)
    for libro in libros:
        if libro['titulo'].lower()==titulo.lower():
            print ('='*60)
            print (f'Titulo:{libro['titulo']} - Ejemplares: {libro['ejemplares']}\n')
            print('='*60,) 
            pausa=input('Presione enter para continuar: ')
            break

#--------INGRESA VARIOS TITULOS NUEVOS, HACIENDO TODAS LAS VALIDACIONES CORRESPONDIENTES
def ingresar_titulos():
    cantidad=validacion_digitos(0)

    titulos_existentes=lista_titulos()

    nuevos_libros=[]
    for i in range (cantidad):
        nombre=validacion_titulos(titulos_existentes)
        ejemplares=validacion_ejemplares(0)
        nuevos_libros.append({'titulo':nombre, 'ejemplares':ejemplares})
        titulos_existentes.append(nombre.lower())

    with open (nombre_archivo, 'a', newline='', encoding='utf-8') as archive:
        escritor=csv.DictWriter(archive, fieldnames=['titulo', 'ejemplares'])
        escritor.writerows(nuevos_libros)
    print('='*60,'\n El catalogo de libros se ha actualizado correctamente!')
    mostrar_catalogo()
    print('='*60)

#-------AGREGA EJEMPLARES A LOS TITULOS QUE YA EXISTEN
def ingresar_ejemplares():
    libros=catalogo()
    if not libros:
        pausa=input('Todavía no se ha agregado ningún título a la biblioteca. Presione enter para salir: ')
        return
    
    titulos_existentes=lista_titulos()

    titulo=buscar_titulo(titulos_existentes)
    ejemplares=validacion_ejemplares(1)

    #Suma la cantidad de ejemplares al titulo indicado
    for libro in libros:
        if libro['titulo'].lower()==titulo.lower():
            libro['ejemplares']=libro['ejemplares']+int(ejemplares)
    
    #Agrega la nueva información, sobreescribiendo todo el archivo
    with open (nombre_archivo, 'w', newline='', encoding='utf-8') as archive:
        escritor=csv.DictWriter(archive, fieldnames=['titulo', 'ejemplares'])
        escritor.writeheader()
        escritor.writerows(libros)

#-------FUNCION PARA MOSTRAR LOS TITULOS QUE NO TIENEN EJEMPLARES DISPONIBLES
def listar_agotados():
    libros=catalogo()
    print('='*60,'\nLISTA DE AGOTADOS')
    print('='*60)
    agotados=[]
    for libro in libros:
        if libro['ejemplares']==0:
            print(f'Título: {libro['titulo']} ')
            agotados.append(libro)
    if not agotados:
        print('\nNO HAY LIBROS AGOTADOS')
    
    print('='*60)
    pausa=input('Presione enter para continuar: ')
    
#-----FUNCION PARA AGREGAR UN SÓLO TITULO
def agregar_titulo():
    titulos_existentes=lista_titulos()

    nombre=validacion_titulos(titulos_existentes)
    ejemplares=validacion_ejemplares(1)
    nuevos_libros=[]
    nuevos_libros.append({'titulo':nombre, 'ejemplares':ejemplares})
    with open (nombre_archivo, 'a', newline='', encoding='utf-8') as archive:
        escritor=csv.DictWriter(archive, fieldnames=['titulo', 'ejemplares'])
        escritor.writerows(nuevos_libros)
    print('='*60,'\n El catalogo de libros se ha actualizado correctamente!')
    mostrar_catalogo()
    print('='*60)

#----- FUNCION PARA GESTIONAR LOS PRESTAMOS O DEVOLUCIONES
def actualizar_ejemplares():
    libros=catalogo()
    if not libros:
        pausa=input('Todavía no se ha agregado ningún título a la biblioteca. Presione enter para salir: ')
        return
    titulos_existentes=lista_titulos()
    titulo=buscar_titulo(titulos_existentes)

    option=input("Si desea pedir un prestamo ingrese 'P', si desea hacer una devolución ingrese 'D': ").strip().lower()
    bandera=False

    # GESTION DEL PRESTAMO
    if option=='p':
        for libro in libros:
            if titulo.lower()== libro['titulo'].lower() and libro['ejemplares']>0:
                libro['ejemplares']-=1
                pausa=input('El prestamo se ha gestionado correctamente. Presione enter para continuar: ')
                bandera=True
                break
            elif titulo.lower()== libro['titulo'].lower() and libro['ejemplares']==0:
                print('No puede solicitar un prestamo de este libro, debido a que no hay disponibilidad.')
                pausa=input('Presione enter para continuar: ')
                break

    # GESTION DE LA DEVOLUCION
    elif option=='d':
        for libro in libros:
            if titulo.lower()==libro['titulo'].lower():
                libro['ejemplares']+=1
                pausa=input('Titulo ingresado correctamente. Presione enter para continuar: ')
                bandera=True
                break

    else:
        pausa=input('Ha ingresado una opción incorrecta. Presione enter para continuar: ')  

    if bandera==True:
        with open (nombre_archivo, 'w', newline='', encoding='utf-8') as archive:
            escritor=csv.DictWriter(archive, fieldnames=['titulo', 'ejemplares'])
            escritor.writeheader()
            escritor.writerows(libros)
        mostrar_catalogo()

while opcion != "8":
    menu()
    opcion=input("Opción:").strip()
    match opcion:
        case "1":
            ingresar_titulos()
        case "2":
            ingresar_ejemplares()
        case "3":
            mostrar_catalogo()
        case "4":
            consultar_disponibilidad()
        case "5":
            listar_agotados()
        case "6":
            agregar_titulo()
        case "7":
            actualizar_ejemplares()
        case "8":
            print("Hasta luego!")
            break
        case _:
            pausa=input("Opción invalida. Presione enter para continuar: ")