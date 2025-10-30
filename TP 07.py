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
#--------Imprime la lista de palabras sin repetir-------
palabras_unicas=set(lista_palabras)
print (palabras_unicas)
#-------Imprime el diccionario con las palabras que se repiten-------


