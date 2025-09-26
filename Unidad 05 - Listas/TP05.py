#1)Crear una lista con las notas de 10 estudiantes.
#•Mostrar la lista completa.
#•Calcular y mostrar el promedio.
#•Indicar la nota más alta y la más baja.
lista=[10,8,5,6,7,10,9,8,4,1]
suma=0
promedio=0
cantidad= len(lista)
menor_nota=0
mayor_nota=0
suma= sum(lista)
promedio= suma/cantidad
menor_nota=min(lista)
mayor_nota=max(lista)
for nota in lista:
    print (nota)
print (f"""La nota mas alta de la lista es {mayor_nota} 
La nota mas baja de la lista es {menor_nota}
El promedio de notas es {promedio}""")

#2)Pedir al usuario que cargue 5 productos en una lista.
#•Mostrar la lista ordenada alfabéticamente. Investigue el uso del método sorted().
#•Preguntar al usuario qué producto desea eliminar y actualizar la lista.
lista=[]
opcion= "e"
for x in range (5):
    producto = input("Ingrese un producto: ")
    lista.append(producto)

print("\n¿Desea eliminar o agregar u producto?")
while opcion !="X":
    opcion=input("Presione A para agregar, E para eliminar, X para salir:")
    opcion=opcion.upper()
    if opcion == "A":
        producto=input("Inserte el producto que desea agregar: ")
        lista.append(producto)
    elif opcion=="E":
        producto=input("Inserte el producto que desea eliminar: ")
        if producto in lista:
            lista.remove(producto)
        else:
            print("El producto no está en la lista")
    elif opcion!="X":
        print("Opción incorrecta. Vuelva a ingresar una opción:")
lista1=sorted(lista)
print("\nLista de productos ordenada: ")
for productos in lista1:
    print(f"-{productos}")

#3)Generar una lista con 15 números enteros al azar entre 1 y 100.
#•Crear una lista con los pares y otra con los impares.
#•Mostrar cuántos números tiene cada lista.
import random
lista=[]
par=[]
impar=[]
npar=0
nimpar=0
for x in range (15):
    num=random.randint(1,100)
    lista.append(num)
    if num%2==0:
        par.append(num)
        npar+=1
    else:
        impar.append(num)
        nimpar+=1
print("Lista de numeros: ") 
for y in lista:
    print(y)
print ("\nLista de pares: ")
for z in par:
    print(z)
print(f"Total de pares: {npar}")
print("\nLista de impares: ")
for s in impar:
    print(s)
print(f"Total de impares: {nimpar}")

#4)Dada una lista con valores repetidos:
#•Crear una nueva lista sin elementos repetidos.
#•Mostrar el resultado.
datos=[1,3,5,3,7,1,9,5,3]
lista=[]
for x in datos:
    if x not in lista:
        lista.append(x)
    else:
        continue
print("Lista original")
for x in datos:
    print (x, end=" ")
print("\nLista sin duplicados")
for x in lista:
    print (x, end=" ")

#5) Crear una lista con los nombres de 8 estudiantes presentes en clase. 
#• Preguntar al usuario si quiere agregar un nuevo estudiante o eliminar uno existente. 
#• Mostrar la lista final actualizada.
opcion="a"
estudiantes=["Juan", "Lorenzo", "Josue", "David", "Fernando", "Raul", "Abigail", "Ines"]
for x in estudiantes:
    print (x)

while opcion != "X":
    opcion=input("\nSi desea agregar otro estudiante ingrese A, si desea quitar uno ingrese E, si desea finalizar ingrese X: ")
    opcion=opcion.upper()
    if opcion == "A":
        estu=input("Ingrese el nombre del estudiante: ")
        estudiantes.append (estu)
    elif opcion=="E":
        if estu in estudiantes:
            estu=input("Ingrese el nombre del estudiante: ")
            estudiantes.remove(estu)
        else:
            print("El estudiante no se encuentra en la lista.")
    else:
        print("Opcion invalida.")
for x in estudiantes:
    print (x)

#6)Dada una lista con 7 números, rotar todos los elementos una posición hacia la derecha (el 
#último pasa a ser el primero). 
lista=[0,8,9,4,56,7,4]
print("Lista de numero originales:")
for num in lista:
    print (num)
lista1=lista[-1:]+lista[:-1]
print("\nLista de numeros rotados hacia la derecha:")
for num in lista1:
    print(num)

#7) Crear una matriz (lista anidada) de 7x2 con las temperaturas mínimas y máximas de una semana.
#•Calcular el promedio de las mínimas y el de las máximas.
#•Mostrar en qué día se registró la mayor amplitud térmica.
print("Temperaturas minimas y maximas de Villa la Angostura del 26/09 al 02/10")
suma=0
suma1=0
prom_max=0
prom_min=0
matriz=[[3,9],[-1,7],[0,5],[1,5],[0,9],[3,13],[5,16]]
for x in range(len(matriz)):
    temp_min=matriz[x][0]
    suma+=temp_min
    temp_max=matriz[x][1]
    suma1+=temp_max
prom_min=round(suma/7,1)
prom_max=round(suma1/7,1)
print(f"La temperatura mínima promedio de la semana del 26/09 al 02/10 es: {prom_min} °C")
print(f"La temperatura máxima promedio de la semana del 26/09 al 02/10 es: {prom_max} °C")

#8)Crear una matriz con las notas de 5 estudiantes en 3 materias.
#•Mostrar el promedio de cada estudiante.
#•Mostrar el promedio de cada materia.
matriz=[[9, 7, 5, 8, 5],[10, 6, 3, 7, 5], [8, 7, 2, 9, 4]]
for i in range (3):
    suma=0
    for x in range(5):
        nota=matriz[i][x]
        suma+=nota
        promedio=suma/5
    print(f"Promedio de materia {i+1}: {promedio}")
print("")
for x in range (5):
    suma=0
    for i in range(3):
        nota=matriz[i][x]
        suma+=nota
        promedio=suma/5
    print(f"Promedio del alumno {x+1}: {promedio}")
