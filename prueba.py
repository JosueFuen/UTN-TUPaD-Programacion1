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