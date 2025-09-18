#1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100 
#(incluyendo ambos extremos), en orden creciente, mostrando un número por línea. 
for x in range (101):
    print (x)

#2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de 
#dígitos que contiene.
num=input('Escriba un número entero: ')
digitos=len(num)
print(f"El numero contiene {digitos} digitos")

#3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores 
#dados por el usuario, excluyendo esos dos valores. 
num1= float(input('Ingrese un el número menor: '))
num2= float(input('Ingrese un el número mayor: '))
for x in range (num1, num2):
    print (x)

#4) Elabora un programa que permita al usuario ingresar números enteros y los sume en 
#secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese 
#un 0.
print('Ingrese números enteros para sumarlos. Para finalizar el programa presion la tecla cero')
suma=0
while True:
    num=int(input('Ingrese un número: '))
    if num==0:
        break
    suma+=num
print('La suma total es de: ', suma)

#5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el 
# programa debe mostrar cuántos intentos fueron necesarios para acertar el número. 
import random
num=random.randint(0,9)
num1=int(input('Ingrese un número del 0 al 9, para adivinar el número escogido por la maquina: '))
while num!=num1:
    num1=int(input('Incorrecto, ingrese otro número: '))
    contador+=1
print(f'Excelente! ha adivinado el número en el intento {contador}. El número correcto es: {num}')

#6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos 
# entre 0 y 100, en orden decreciente.
for x in range (100,-1,-2):
    print(x)

#7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un 
# número entero positivo indicado por el usuario. 
num=int(input('Ingrese un número para calcular la suma de todos los números comprendidos entre 0 y ese número: '))
suma=0
for x in range(num+1):
    suma+=x
print('La suma total es: ',suma)

#8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el 
# programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son 
# negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad 
# menor, pero debe estar preparado para procesar 100 números con un solo cambio). 
par=0
impar=0
positivo=0
negativo=0
for x in range (100):
    num=int(input('Ingrese un número: '))
    if num%2==0:
        par+=1
    else:
        impar+=1
    if num>0:
        positivo+=1
    elif num <0:
        negativo+=1
print(f'''La cantidad de números pares es: {par}
La cantidad de números impares es: {impar}
La cantidad de número positivos es: {positivo}
La cantidad de número negativos es: {negativo}''')

#9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la 
#media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe 
#poder procesar 100 números cambiando solo un valor).
total=100
suma=0
for x in range (total):
    num=int(input('Ingrese un número: '))
    suma+=num
media=suma/total
print('La media es: ', media)

#10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el 
#usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745. 
num=input('Ingrese un número: ')
num_inv=''
for x in range(len(num)-1, -1,-1):
    num_inv+=num[x]
print('El número inverso es: ',num_inv)
