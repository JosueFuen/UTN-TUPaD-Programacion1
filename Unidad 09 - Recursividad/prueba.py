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