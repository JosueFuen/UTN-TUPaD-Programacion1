#1 Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”. 
print ("Hola Mundo!")


#2 Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando 
    #el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir 
    #por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para 
    #realizar la impresión por pantalla. 
nombre=input("Escribir nombre: ")
print (f'Hola {nombre}!')

#3  Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e 
    #imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa 
    #“Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30 
    #años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar 
    #la impresión por pantalla. 
nombre=input('Escribir nombre: ')
apellido=input('Escribir apellido: ')
edad=input('Escribir edad: ')
nacion=input('Escribir lugar de residencia: ')
print (f'Soy {nombre} {apellido}, tengo {edad} anios y vivo en {nacion}')

#4 Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y 
    #su perímetro. 
radio=int(input('Escribir el radio del circulo: '))
pi=3.14
area= pi*radio*radio
perimetro= 2*pi*radio
print(f'El area del circulo es {area} y el perimetro es {perimetro}.')

#5 Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a 
    #cuántas horas equivale. 
seg=int(input('Escribir una cantidad de segundos: '))
min= seg/60
print (f'{seg} segundos equivalen a {min} minutos.')

#6 Crear un programa que pida al usuario un número e imprima por pantalla la tabla de 
    #multiplicar de dicho número.
num=int(input("Introducir un número: "))
print (f'''1 x {num} = {1*num}
2 x {num} = {2*num}
3 x {num} = {3*num}
4 x {num} = {4*num}
5 x {num} = {5*num}
6 x {num} = {6*num}
7 x {num} = {7*num}
8 x {num} = {8*num}
9 x {num} = {9*num}
10 x {num} = {10*num}''')

#7 Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por 
    #pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos. 
num1=int(input('Ingrese el primer número: '))
num2=int(input('Ingrese el segundo número: '))
suma= num1+num2
resta=num1-num2
div= num1/num2
mult=num1*num2
print (f'El resultado de la suma es {suma}, el de la resta es {resta}, el de la division es {div} y el de la multiplicacion es {mult}')

#8 Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice de masa corporal.
peso=float(input('Ingrese su peso en kg: '))
altura=float(input('Ingrese su altura en m: '))
imc=peso/(altura**2)
print (f'Su índice de masa corporal es: {imc}')

#9 Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por 
    #pantalla su equivalente en grados Fahrenheit. 
temp=float(input('Escriba la temperatura en grtados celsius: '))
fahr= (9/5)*temp+32
print(f'La temperatura en grados Fahrenheit es: {fahr}')

#10 Crear un programa que pida al usuario  3 números e imprima por pantalla el promedio de 
    #dichos números.
num1=float(input('Ingrese el primer número: '))
num2=float(input('Ingrese el segundo número: '))
num3=float(input('Ingrese el tercer número: '))
promedio= (num1+num2+num3)/3
print(f'El promedio de los números ingresados es {promedio}')

