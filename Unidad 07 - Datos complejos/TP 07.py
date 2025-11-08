#1) Dado el diccionario precios_frutas precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450} Añadir las siguientes frutas con sus respectivos precios:
#● Naranja = 1200
#● Manzana = 1500
#● Pera = 2300
precios_frutos={'Banana' : 1200, 'Anana' : 2500, 'Melon': 3000, 'Uva': 1450}
precios_frutos['Naranja']=1200
precios_frutos['Manzana']=1500
precios_frutos['Pera']=2300
print (precios_frutos)

#2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código desarrollado en el punto anterior, actualizar los precios de las siguientes frutas:
#● Banana = 1330
#● Manzana = 1700
#● Melón = 2800
precios_frutos={'Banana' : 1200, 'Anana' : 2500, 'Melon': 3000, 'Uva': 1450}
precios_frutos['Naranja']=1200
precios_frutos['Manzana']=1500
precios_frutos['Pera']=2300
print (precios_frutos)
precios_frutos['Banana']= 1330
precios_frutos['Manzana']=1700
precios_frutos['Melon']=2800
print(precios_frutos)

#3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los precios.
precios_frutos={'Banana' : 1200, 'Anana' : 2500, 'Melon': 3000, 'Uva': 1450}
precios_frutos['Naranja']=1200
precios_frutos['Manzana']=1500
precios_frutos['Pera']=2300
print (precios_frutos)
precios_frutos['Banana']= 1330
precios_frutos['Manzana']=1700
precios_frutos['Melon']=2800
print(precios_frutos)
print(precios_frutos.keys())

#4) Escribí un programa que permita almacenar y consultar números telefónicos.
#• Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
#• Luego, pedí un nombre y mostrale el número asociado, si existe.
name='A'
num='0'
num_telefonos={}
for x in range (5):
    name=input('Ingrese el nombre del usuario: ')
    num=input('Ingrese el número de telefono del usuario: ')
    num_telefonos[name]={num}
name= input('Ingrese el nombre de usuario, para consultar el numero de telefono: ')
print(num_telefonos[name])

#5) Solicita al usuario una frase e imprime:
#• Las palabras únicas (usando un set).
#• Un diccionario con la cantidad de veces que aparece cada palabra.
frase=input('Ingrese una frase: ')
lista_palabras=frase.split()
diccionario_palabras={}
#--------Imprime la lista de palabras sin repetir-------
palabras_unicas=set(lista_palabras)
print (palabras_unicas)
#-------Imprime el diccionario con las palabras que se repiten-------
for palabra in lista_palabras:
    
    if palabra not in diccionario_palabras:
        diccionario_palabras[palabra]=1
    else:
        diccionario_palabras[palabra]+=1
print(diccionario_palabras)
#6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas. 
#Luego, mostrá el promedio de cada alumno. 
diccionario={}
def ingreso_de_notas(tupla):
    name=input('Ingrese el nombre del alumno: ')
    notas=[]
    for x in range(1,4):
        nota=int(input(f'Ingrese la nota del parcial {x} de {name}: '))
        notas.append(nota)
    tupla=tuple(notas)
    diccionario[name]={tupla}
    suma=0
    for nota in tupla:
        suma+=nota
    promedio=print (f'El promedio de {name} es {suma/3}')
    return promedio, diccionario
tupla1=()
tupla2=()
tupla3=()
ingreso_de_notas(tupla1)
ingreso_de_notas(tupla2)
ingreso_de_notas(tupla3)
print (diccionario)

#7) Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1 
#y Parcial 2: 
#• Mostrá los que aprobaron ambos parciales. 
#• Mostrá los que aprobaron solo uno de los dos. 
#• Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir). 

aprobados1={'lucas', 'martin', 'jorge', 'bruno'}
aprobados2={'martin', 'jorge', 'daniel', 'tomas', 'roberto'}

print ('Aprobaron ambos parciales: ',aprobados1 & aprobados2)
print ('Aprobaron un sólo parcial: ', aprobados1^aprobados2)
print ('Aprobaron al menos, un sólo parcial: ', aprobados1 |aprobados2)


#8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock. 
#Permití al usuario: 
#• Consultar el stock de un producto ingresado. 
#• Agregar unidades al stock si el producto ya existe. 
#• Agregar un nuevo producto si no existe. 
stock_productos={'papas': 3 , 'cebollas': 5}
def consultar_stock():
    consulta=input('Ingrese el producto por el cual desea consultar: ').strip().lower()
    if consulta in stock_productos:
        stock=print (f'El stock de {consulta} es: {stock_productos[consulta]}')
        pausa=input('Presione enter para continuar')
        return stock
    else:
        return
def agregar_stock():
    producto=input('Ingrese el producto al cual desea agregar mas stock: ').strip().lower()
    stock=int(input('Ingrese cuanto stock desea agregar: '))
    stock_productos[producto]+=stock
    return stock_productos
def agregar_productos():
    producto=input('Ingrese el nuevo producto: ')
    stock=int(input('Ingrese el stock del producto nuevo: '))
    stock_productos[producto]=stock
    return stock_productos
opcion=''
def menu():
    print('======= MENU =======')
    print('1) Consultar Stock')
    print('2) Agregar Stock')
    print('3) Agregar Producto')
    print('4) Salir')

while opcion != '4':
    menu()
    opcion=input('Ingrese la opcion deseada: ')
    match opcion:
        case '1':
            consultar_stock()
        case '2':
            agregar_stock()
        case '3':
            agregar_productos()
        case '4':
            break
        case _:
            print('Opcion incorrecta.')
            continue
#9) Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos. 
#Permití consultar qué actividad hay en cierto día y hora.
agenda={('lunes', '10:00'):'Reunion', ('martes','15:00'): 'Clases de ingles'}
def menu():
    print('====== MENU ======')
    print('1) Agregar evento')
    print('2) Consultar agenda')
    print('3) Salir')

def agregar_evento():
    dia=input('Ingrese día: ').strip().lower()
    hora=input('Ingrese la hora: ')
    evento=input('Ingrese el nombre del evento: ')
    agenda[(dia,hora)]=evento

def consultar_agenda():
    consulta_dia=input('Ingrese el día que desea consultar: ').strip().lower()
    consulta_hora=input('Ingrese el horario que desea consultar: ').strip()
    if (consulta_dia,consulta_hora) in agenda:
        print(agenda[(consulta_dia,consulta_hora)])
opcion=''
while opcion != '3':
    menu()
    opcion=input('Seleccione una opcion: ')
    match opcion:
        case '1':
            agregar_evento()
        case '2':
            consultar_agenda()
        case '3':
            break
        case _:
            opcion=input('Opcion incorrecta. Intente nuevamente: ')
#10) Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo 
#diccionario donde: 
#• Las capitales sean las claves. 
#• Los países sean los valores. 
original={'Argentina':'Buenos Aires', 'Chile':'Santiago'}
claves=list(original.keys())
valores=list(original.values())
invertido={}
for x in range(len(original)):
    invertido[valores[x]]=claves[x]
print (invertido)


