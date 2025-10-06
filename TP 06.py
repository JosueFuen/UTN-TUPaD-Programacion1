"""1) Crear una función llamada imprimir_hola_mundo que imprima por
pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el
programa principal."""
def saludo_inicial():
    #Escribe "Hola Mundo!".

    print("Hola, Mundo!")
saludo_inicial()

"""2) Crear una función llamada saludar_usuario(nombre) que reciba
como parámetro un nombre y devuelva un saludo personalizado.
Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá devolver:
“Hola Marcos!”. Llamar a esta función desde el programa
principal solicitando el nombre al usuario."""
nombre=input("Ingrese su nombre: ")

def saludar_usuario(nombre):
    #Escribe un saludo para el usuario
    #Args:
    #  - nombre: string del nombre de usuario.
    print(f"Hola {nombre}!")
saludar_usuario(nombre)

"""3) Crear una función llamada informacion_personal(nombre, apellido,
edad, residencia) que reciba cuatro parámetros e imprima: “Soy
[nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pedir
los datos al usuario y llamar a esta función con los valores ingresados."""
nombre=input('Escribir nombre: ')
apellido=input('Escribir apellido: ')
edad=input('Escribir edad: ')
residencia=input('Escribir su lugar de residencia: ')

def informacion_personal(nombre, apellido, edad, residencia):
    #Imprime datos personales del usuario.
    #Args:
    #  - nombre: string.
    #  - apellido: string
    #  - edad: string
    #  - residencia: string
    print (f'Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}')

informacion_personal(nombre, apellido, edad, residencia)

"""4) Crear dos funciones: calcular_area_circulo(radio) que reciba el radio
como parámetro y devuelva el área del círculo. calcular_perimetro_
circulo(radio) que reciba el radio como parámetro y devuelva
el perímetro del círculo. Solicitar el radio al usuario y llamar ambas
funciones para mostrar los resultados."""
from math import pi
radio=float(input("Ingresar el radio del circulo: "))
area=1
perimetro=1
def calcular_area_circulo(radio):
    #calcula el area de un circulo.
    #Args:
    #  - radio: int
    #Returns:
    #  - area: area del circulo
    area=pi*(radio**2)
    return area
def calcular_preimetro_circulo(radio):
       #calcula el area de un circulo.
    #Args:
    #  - radio: float
    #Returns:
    #  - perimetro: perimetro del circulo
    perimetro=2*pi*radio
    return perimetro
calcular_preimetro_circulo(radio)
calcular_area_circulo(radio)

"""5)Crear una función llamada segundos_a_horas(segundos) que reciba
una cantidad de segundos como parámetro y devuelva la cantidad
de horas correspondientes. Solicitar al usuario los segundos y mostrar
el resultado usando esta función."""
horas=0
segundos=int(input("Ingrese la cantidad de segundos: "))

def segundos_a_horas(segundos):
    #Convierte de segundos a horas
    #Args:
    #   -segundos: lee los segundos en enteros
    #Returns:
    #   -horas: devuelve la cantidad de horas en flotantes
    horas=segundos/3600
    return horas
print(segundos_a_horas(segundos))

"""6) Crear una función llamada tabla_multiplicar(numero) que reciba un
número como parámetro y imprima la tabla de multiplicar de ese
número del 1 al 10. Pedir al usuario el número y llamar a la función."""
numero=(int(input("Ingrese un numero: ")))
def tabla_multiplicar(numero):
    #Imprime la tabla de multiplicar de un numero solicitado
    #Args:
    #   -numero: numero al que se le imrimira la tabla de multiplicar
    for x in range (1,11):
        print(f"{x} X {numero} = {x*numero}")
tabla_multiplicar(numero)

"""7) Crear una función llamada operaciones_basicas(a, b) que reciba
dos números como parámetros y devuelva una tupla con el resultado
de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los resultados
de forma clara."""
a=int(input("Ingrese un numero: "))
b=int(input("Ingrese un numero: "))

#ACLARACIÓN:  Lo ideal sería hacer una función para cada operación, pero debido a la consigna se realiza asi.
def operaciones_basicas(a, b):
    #Realiza las operaciones de suma, resta, division y multiplicacion.
    #Args:
    #   - a: numero entero
    #   - b: numero entero
    #Return:
    #   Resultado: imprime los siguientes items:
    #      suma: la suma entre a y b
    #      resta: el resultado de a menos b
    #      multiplicacion: la multiplicacion entre a y b
    #      division: el resultado de a dividido b
    suma=a+b
    resta=a-b
    multiplicacion=a*b
    division=a/b
    print(f"Suma: {suma}, resta: {resta}, multiplicación: {multiplicacion}, división: {division}")

operaciones_basicas(a,b)

"""8) Crear una función llamada calcular_imc(peso, altura) que reciba el
peso en kilogramos y la altura en metros, y devuelva el índice de
masa corporal (IMC). Solicitar al usuario los datos y llamar a la función
para mostrar el resultado con dos decimales."""
peso=float(input('Ingrese su peso en kg: '))
altura=float(input('Ingrese su altura en m: '))

def calcular_imc(peso, altura):
    imc=round(peso/(altura**2), 2)
    return imc
print(calcular_imc(peso, altura))