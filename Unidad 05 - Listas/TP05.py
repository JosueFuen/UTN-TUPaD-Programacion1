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