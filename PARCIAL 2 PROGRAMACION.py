import csv
import os
nombre_archivo= 'libros.csv'

if not os.path.exists('libros.csv'):
    with open ('libros.csv', 'w', newline='', encoding='utf-8') as archivo:
        csv.DictWriter(archivo, fieldnames=['titulos','ejemplares']).writeheader

        
def mostrar_catalogo():
    libros=[]
    with open (nombre_archivo, newline='', encoding='utf-8') as archivo:
        lector=csv.DictReader(archivo)
        for fila in lector:
            libros.append({'Titulo':fila['titulos'], 'Ejemplar':int(fila['ejemplares'])})
    return libros
libros = {"It", "1984", "Rayuela", "Hamlet", "Dune", "Siddharta", "El Aleph", "Solaris", "Drácula", "Frankenstein"}
ejemplares = [3, 3, 8, 9, 14, 10, 13, 3, 0, 18]
opcion=""
while opcion != "8":
    print("\n           📚  MENÚ DE LA BIBLIOTECA  📚")
    print("1)   Ingresar títulos")
    print("2)   Ingresar ejemplares")
    print("3)   Mostrar catálogo")
    print("4)   Consultar disponibilidad")
    print("5)   Listar agotados")
    print("6)   Agregar título")
    print("7)   Actualizar ejemplares(préstamo/devolución)")
    print("8)   Salir")
    opcion=input("Opción:").strip()
    match opcion:
        case "1":
            ingresar_titulos()
            cantidad=input("Ingrese la cantidad de títulos que desea agregar:").strip()
            #Validacion
            #En este caso, quiero que el usuario ingrese los datos y que intente indefinidamente si se equivoca. Tampoco quiero que salga un error.
            #entonces, coloque dos while, el primero para validar que haya ingresado un digito y el segundo para que este en el rango correcto ejemplares
            #pero a su vez, luego de pasar el primer while, el usuario podria volver a insertar un valor que no sea un numero, por eso el ultimo while.
            while not cantidad.isdigit() or cantidad=="":
                cantidad=input("Debe ingresa un digito. Intente nuevamente: ").strip()
            cantidad=int(cantidad)
            while cantidad<1:
                cantidad=input("Debe ser un numero mayor a 0. Intente nuevamente: ").strip()
                while not cantidad.isdigit() or cantidad=="":
                    cantidad=input("Debe ingresar un número. Intente nuevamente")
                cantidad=int(cantidad)
            #Ingresa la cantidad de titulos elegidos para agregar
            for x in range (cantidad):
                titulo=input(f"Ingresar el título {x+1} del libro que desea agregar: ").strip()
                while titulo in libros or titulo=="":
                    if titulo in libros:
                        print("-----------------------------------------------------")
                        titulo=input("El título ingresado ya existe. Intente ingresando otro: ").strip()
                    elif titulo=="":
                        print("-----------------------------------------------------")
                    titulo=input("Debe ingresar un titulo. Intente nuevamente: ").strip()
                #En el video indicaba, que se debia agregar de otra manera. Preferi usar este metodo, ya que si se borra un titulo por error o
                #sucede algun error, la sincronización se va a arruinar de todos modos.
                libros.append(titulo)
                ejemplares.append(0)
                pausa=input("El titulo se ha agregado correctamente. Presione enter para continuar: ")
            print("------------------------")
            pausa=input("Todos los libros se han ingresado corectamente. Presione enter para ir al menú principal. ")


        case "2":
            #Verifica que hayan titulos 
            if not libros:
                pausa=input("Para poder ingresar repertorios, debe existir al menos un titulo. Presione enter para continuar")
                continue
            #Imprime la lista de titulos
            while True:
                print("------   TITULOS DISPONIBLES    ------")
                for i, titulo in enumerate(libros, start=1):
                    print(f"{i} - {titulo}")
                
                #Valida que sea un digito
                print("------------------------------------")
                indice=input("Indique el título al que desea agregar mas ejemplares:")
                while not indice.isdigit() or indice=="":
                    indice=input("Debe ingresa un digito. Intente nuevamente: ").strip()

                #Valida que sea rango correcto
                indice=int(indice)
                while indice<1 or indice> len(libros):
                    indice=input("Debe ingresar los ejemplares dentro del catalogo existente. Intente nuevamente: ").strip()
                    while not indice.isdigit() or indice=="":
                        indice=input("Debe ingresar un número. Intente nuevamente: ")
                    indice=int(indice)    

                #Ingreso de cantidad de ejemplares a agregar
                cantidad=input("Ingrese la cantidad de ejemplares que desea agregar:").strip()
                while not cantidad.isdigit() or cantidad=="":
                    cantidad=input("Debe ingresa un digito. Intente nuevamente: ").strip()

                cantidad=int(cantidad)
                while cantidad<1:
                    cantidad=input("Debe ser un numero mayor a 0. Intente nuevamente: ").strip()
                    while not cantidad.isdigit() or cantidad=="":
                        cantidad=input("Debe ingresar un número. Intente nuevamente")
                    cantidad=int(cantidad)
                
                #Se agrega la cantidad seleccionada al stock que ya habia
                print("-------------------") 
                print("Los ejemplares se han agregado correctamente")
                print(f"Cantidad original de ejemplares: {ejemplares[indice-1]}")
                ejemp=ejemplares[indice-1]
                ejemplares[indice-1]=ejemp+cantidad
                print(f"Cantidad actual de ejemplares: {ejemplares[indice-1]}")
                print("------------------")
                pausa=input("Presione enter para regresar al menú principal:")
                break

        case "3":
            
            if not libros:
                pausa=input("No hay títulos que mostrar. Presione enter para continuar")
                continue
            while True:
                print("------   CATÁLOGO DE LIBROS    ------")
                for i, titulo in enumerate(libros, start=1):
                    print(f"{i} - {titulo}")
                print("------------------------------------")
                pausa=input("Presione enter para continuar:")
                break
        case "4":
            if not libros:
                pausa=input("No hay títulos que mostrar. Presione enter para continuar")
                continue
            print("------------------------------------")
            consulta=input("Ingrese título para consultar: ").strip()
            while True:
                if consulta in libros:
                    indice= libros.index(consulta)
                    print(f"'{libros[indice]}' se encuentra en el indice {indice+1} y tiene {ejemplares[indice]} ejemplares disponibles.")
                    pausa=input("Presione enter para continuar.")
                    break
                else:
                    print("El libro ingresado no se encuentra en nuestro catálogo.")
                    x=input("Si desea intentar denuevo presione E, sino enter: ").strip().upper()
                    if x == "E":
                        consulta=input("Ingrese título para consultar:")
                        continue
                    else:
                        break
        case "5":
            if not libros:
                pausa=input("\nNo hay títulos disponibles. Presione enter para salir")
                break

            agotados=False
            
            for i in ejemplares:
                if i==0:
                    agotados=True
                    continue
            if agotados:

                #Recorre los ejemplares, buscando el stock 0
                print("     LIBROS AGOTADOS ")
                for i in range (len(libros)):
                    if ejemplares[i]==0:
                        agotados=True
                        print(f"-{libros[i]}      índice: {i+1} ")
                print("---------------------------------------")
                pausa=input("Presione enter para salir: ")
            if not agotados:
                print("No hay libros agotados")

        case "6":
            titulo=input("Ingresar el título del libro que desea ingresar: ").strip()
            while titulo in libros or titulo=="":
                if titulo in libros:
                    print("-----------------------------------------------------")
                    titulo=input("El título ingresado ya existe. Intente ingresando otro: ").strip()
                elif titulo=="":
                    print("-----------------------------------------------------")
                    titulo=input("Debe ingresar un titulo. Intente nuevamente: ").strip()

            libros.append(titulo)
            pausa=input("El titulo se ha agregado correctamente. Presione enter para agregar ejemplares: ")

            #Se ingresa la cantidad de ejemplares iniciales, validando
            cantidad=input("Ingrese la cantidad de ejemplares que desea agregar:").strip()
            while not cantidad.isdigit() or cantidad=="":
                cantidad=input("Debe ingresa un digito. Intente nuevamente: ").strip()

            cantidad=int(cantidad)
            while cantidad<1:
                cantidad=input("Debe ser un numero mayor a 0. Intente nuevamente: ").strip()
                while not cantidad.isdigit() or cantidad=="":                        
                    cantidad=input("Debe ingresar un número. Intente nuevamente")
                cantidad=int(cantidad)
                
            #Se agrega la cantidad seleccionada 
            ejemplares.append(cantidad)

            print("-------------------") 
            print("El libro se ha agregado correctamente al catálogo")
            posicion=len(libros)-1
            print(f"{posicion+1}) {libros[posicion]}    -    Ejemplares: {ejemplares[posicion]}")
            print("-------------------")
            pausa=input("Presione enter para regresar al menú principal:")
            continue

        case "7":
            if not libros:
                pausa=input("No existen libros para prestar o realizar una devolucion. Presione enter para salir. ")
                break
    
            while True:
                print("------   TITULOS DISPONIBLES    ------")
                for i, titulo in enumerate(libros, start=1):
                    print(f"{i} - {titulo}")

                print("------------------------------------")
                indice=input("Indique el libro al cual desea pedir prestamos o realizar devolución: ")
                while not indice.isdigit() or indice=="":
                    indice=input("Debe ingresa un digito. Intente nuevamente: ").strip()

                indice=int(indice)
                while indice<1 or indice> len(libros):
                    indice=input("Debe ingresar los ejemplares dentro del catalogo existente. Intente nuevamente: ").strip()
                    while not indice.isdigit() or indice=="":
                        indice=input("Debe ingresar un número. Intente nuevamente: ")
                    indice=int(indice)    

                x=input("Si desea pedir un prestamo ingrese 'P', si desea hacer una devolución ingrese 'D': ").strip().upper()
                if x == "P":
                    if ejemplares[indice-1]>0:
                        ejemplares[indice-1]-=1
                        print("Su solicitud de préstamo ha sido aceptada.")
                        print(f"Cantidad actual de ejemplares: {ejemplares[indice-1]}")
                        print("------------------")
                    else:
                        print("No hay ejemplares disponibles para préstamo")
                    pausa=input("Presione enter para regresar al menú principal:")
                    break
                elif x== "D":
                    ejemplares[indice-1]+=1
                    print(f"Cantidad actual de ejemplares: {ejemplares[indice-1]}")
                    print("-------------------")
                    pausa=input("Presione enter para regresar al menú principal:")
                    break
                else:
                    print("Ha ingresado una opción invalida")
                    pausa=input("Presione enter para continuar")
                    continue

        case "8":
            print("Hasta luego!")
            break
        case _:
            print("Opción invalida.")
            pausa=input("Presione enter para continuar")