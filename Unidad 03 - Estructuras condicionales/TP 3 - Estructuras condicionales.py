#1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años, deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.

edad=int(input( "Ingrese su edad: "))
if edad>=18:
  print("Es mayor de edad.")
elif edad<0:
  print("Edad no valida")
else:
  print("Es menor de Edad")


# 2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el mensaje “Desaprobado”.

nota=float(input("Ingrese su nota: "))
if nota>= 6 and nota<=10:
  print ("Aprobado")
elif nota<6 and nota>=0:
  print("Desaprobado")
else:
  print("Nota invalida")


# 3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; 
#    en caso contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del operador de módulo (%) en Python para evaluar si un número es par o impar.

num= int(input("Ingrese un número para determinar si es par: "))
if num%2==0:
  print("El número es par")
else:
  print ("El número es impar")


#4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las siguientes categorías pertenece: 
#  ● Niño/a: menor de 12 años. 
#  ● Adolescente: mayor o igual que 12 años y menor que 18 años. 
#  ● Adulto/a joven: mayor o igual que 18 años y menor que 30 años. 
#  ● Adulto/a: mayor o igual que 30 años.

edad=int(input("Ingrese su edad: "))
if edad<12 and edad>=0:
  print("Es un niño")
elif edad>=12 and edad<18:
  print("Es un adolescente")
elif edad>=18 and edad<30:
  print("Es un adulto joven")
elif edad>=30 and edad<200:
  print("Es un adulto")
else:
  print("Edad no valida")


#5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres (incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, 
#  imprimir por en pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". 
#  Nota: investigue el uso de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal como una lista o un string.

contra=input("Ingrese una contraseña: ")
if 8<=len(contra)<=14:
  print("Ha ingresado una contraseña correcta")
else:
  print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")


#6) Escribir un programa que tome la lista numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.

from statistics import mode, median, mean
import random
numeros_aleatorios =[random.randint(1, 100) for i in range (50)]
moda= mode(numeros_aleatorios)
mediana= median(numeros_aleatorios)
media= mean(numeros_aleatorios)
if media>mediana and mediana>moda:
  print("Sesgo positivo o a la derecha")
elif media<mediana and mediana<moda:
  print("Sesgo negativo o a la izquierda")
elif media==mediana==moda:
  print("Sin sesgo")


#7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por pantalla; 
#    en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por pantalla.

frase=input("Escriba una frase o palabra: ").lower()
ult=frase[-1]
if ult=='a' or ult=='e' or ult=='i' or ult=='o' or ult=='u':
  print(f"{frase}!")
else:
  print (frase)


#8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3 dependiendo de la opción que desee:
#1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
#2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
#3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
#El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(), lower() y title() de Python para convertir entre mayúsculas y minúsculas.

nombre=input("Ingrese su nombre: ")
opcion=int(input("Ingrese 1 si quiere su nombre en mayúsculas, 2 si desea su nombre en minúsucas o 3 si quiere su nombre con la primera letra mayuscula"))
if opcion==1:
  print (nombre.upper())
elif opcion==2:
  print(nombre.lower())
elif opcion==3:
  print(nombre.capitalize())
else:
  print ("Opción ingresada incorrecta")


#9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado por pantalla:
#● Menor que 3: "Muy leve" (imperceptible).
#● Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
#● Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero generalmente no causa daños).
#● Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras débiles).
#● Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
#● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).

magn=float(input("Ingrese la magnitud del terremoto: "))
if 0<=magn<3:
  print("Muy leve (imperceptible)")
elif 3<=magn<4:
  print("Leve (ligeramente perceptible)")
elif 4<=magn<5:
  print("Moderado (sentido por personas, pero generalmente no causa daño)")
elif 5<=magn<6:
  print("Fuerte (puede causar daños en estructuras débiles)")
elif 6<=magn<7:
  print("Muy Fuerte (puede causar daños significativos)")
elif 7<=magn:
  print("Extremo (puede causar graves daños a gran escala)")
  

#10)Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla si el usuario se encuentra en otoño, invierno, primavera o verano.


hemis=input("Ingrese S si se encuentra en el hemisferio sur y N si se encuentra en el hemisferio norte: ").lower()
fecha=input("Ingrese la fecha en el siguiente formato dd/mm/aaaa : ")

#Separamos los dias y los meses del formato y ademas los transformamos en enteros
dia=int(fecha[0:2])
mes=int(fecha[3:5])

#Primero trabajamos con los meses menos conflictivos, por ejemplo, a enero solos le corresponde la estación invierno o verano, dependiendo del hemisferio
# pero a diciembre, que es un mes conflictivo, le pueden corresponder las 4 estaciones, dependiendo de los hemisferios.
if mes==1 or mes==2:
  if hemis=='n':
    print('Su estación es invierno')
  else:
    print('Su estación es verano')
elif mes==4 or mes==5:
  if hemis=='n':
    print('Su estación es primavera')
  else:
    print('Su estación es otoño')
elif mes==7 or mes==8:
  if hemis=='n':
    print('Su estación es verano')
  else:
    print('Su estación es invierno')
elif mes==10 or mes==11:
  if hemis=='n':
    print('Su estación es otoño')
  else:
    print('Su estación es primavera')
elif 1>mes or mes>12 or 0>dia or dia>31:
  print ('Fecha invalida')
  
#Ahora comenzamos con los meses conflictivos.
#En sisntesis, esta fracción de codigo selecciona el mes conflictivo y primero le pregunta si esta entre los dias del 1 al 20
# y luego si se encuentra en el hemisferio sur o norte, para asignarle la estación correspondiente. Esto lo hace con cada mes conflictivo.
if mes==12:
  if 1<=dia<21:
    if hemis=='n':
      print('Su estación es otoño')
    else:
      print('Su estación es primavera')
  elif 21<=dia<=31:
    if hemis=='n':
      print('Su estación es invierno')
    else:
      print('Su estación es verano')
elif mes==3:
  if 1<=dia<21:
    if hemis=='n':
      print('Su estación es invierno')
    else:
      print('Su estación es verano')
  elif 21<=dia<=31:
    if hemis=='n':
      print('Su estación es primavera')
    else:
      print('Su estación es otoño')
elif mes==6:
  if 1<=dia<21:
    if hemis=='n':
      print('Su estación es primavera')
    else:
      print('Su estación es otoño')
  elif 21<=dia<=30:
    if hemis=='n':
      print('Su estación es verano')
    else:
      print('Su estación es invierno')
elif mes==9:
  if 1<=dia<21:
    if hemis=='n':
      print('Su estación es verano')
    else:
      print('Su estación es invierno')
  elif 21<=dia<=30:
    if hemis=='n':
      print('Su estación es otoño')
    else:
      print('Su estación es primavera')

