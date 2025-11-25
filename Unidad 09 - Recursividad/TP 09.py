#1)Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa
#función para calcular y mostrar en pantalla el factorial de todos los números enteros
#entre 1 y el número que indique el usuario
acumulador=''
def factorial(n):
    if n == 0:
        return 1
    else:
        return factorial (n-1)*n
cantidad=int(input('Ingrese el factorial que desea calcular: '))

for i in range(1, cantidad + 1):
    print(f'Factorial de {i} = {factorial(i)}')

#2)Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición
#indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario
#especifique
def fibonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
cantidad=int(input('Ingrese hasta que posición de la serie de Fibonacci desea calcular: '))

for i in range(cantidad + 1):
    print(f'Posición {i}: {fibonacci(i)}')

#3)Crea una función recursiva que calcule la potencia de un número base elevado a un
#exponente, utilizando la fórmula n^𝑚 = 𝑛 ∗ 𝑛^(𝑚−1). Prueba esta función en un algoritmo general.
def funcion_potencia (n,m):
    if m == 0:
        return 1
    else:
        return n * funcion_potencia(n, m-1)
base = int(input("Ingrese la base: "))
exponente = int(input("Ingrese el exponente: "))

resultado = funcion_potencia(base, exponente)
print(f"El resultado de {base} elevado a {exponente} es: {resultado}")

#4) Crear una función recursiva en Python que reciba un número entero positivo en base
#decimal y devuelva su representación en binario como una cadena de texto·

def decimal_a_binarios (n):
    if n==0:
        return str(0)
    elif n==1:
        return str(1)
    else:
        return decimal_a_binarios(n//2) + str(n%2)
decimal=int(input('Ingrese el numero decimal que desea transformar: '))
print (f'El numero {decimal} es equivalente a {decimal_a_binarios(decimal)} en binario')

#5)Implementá una función recursiva llamada es_palindromo(palabra) que reciba una
#cadena de texto sin espacios ni tildes, y devuelva True si es un palíndromo o False si no
#lo es.

def es_palindromo(palabra):
    if len(palabra)<2 or palabra=='':
        return True
    elif palabra[0] == palabra[-1]:
        return es_palindromo(palabra[1:-1])
    else:
        return False
palabra=input('Ingrese una palabra para determinar si es palindromo: ').strip()
if es_palindromo(palabra):
    print('La palabra ingresada es un palindromo.')
else:
    print('La palabra ingresada no es un palindromo')

#6) Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un
#número entero positivo y devuelva la suma de todos sus dígitos.
def suma_digitos(n):
    if n<10:
        return n
    else:
        return (n % 10) + suma_digitos(n // 10)
num=int(input('Ingrese un numero: '))
print (f'La suma es {suma_digitos(num)}')

#7)Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n
#bloques, en el siguiente nivel uno menos (n - 1), y así sucesivamente hasta llegar al
#último nivel con un solo bloque.
#Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el
#nivel más bajo y devuelva el total de bloques que necesita para construir toda la
#pirámide.
def contar_bloques(n):
    if n ==1:
        return 1
    else:
        return contar_bloques(n-1) + n
    
base_piramide=int(input('Ingrese la base de la piramide: '))
print (f'Para armar un piramide de base {base_piramide} se necesitan {contar_bloques(base_piramide)} bloques.')

#8) Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un
#número entero positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces
#aparece ese dígito dentro del número.
def contar_digito(numero, digito):
    if len (numero)==0:
        return 0
    if numero[-1]== digito:
        return contar_digito(numero[:-1], digito ) +1
    else:
        return contar_digito(numero[:-1], digito )
    
num=input('Ingrese el numero: ')
dig=input('Ingrese el digito: ')
print (f'El digito {dig} se encuentra {contar_digito(num, dig)} en {num}.')