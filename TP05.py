#´´´1)Crear una lista con las notas de 10 estudiantes.
•Mostrar la lista completa.
•Calcular y mostrar el promedio.
•Indicar la nota más alta y la más baja.´´´
lista=[10,8,5,6,7,10,9,8,4,1]
suma=0
cantidad= len(lista)
menor_nota=10
mayor_nota=1
for i in range (cantidad+1)
  suma+= lista[i]
  if menor_nota<lista[i]
    menor_nota=lista[i]
  elif mayor_nota>lista[i]
    mayor_nota=lista[i]
print (f"""{lista}
La nota mas alta de la lista es {mayor_nota} 
La nota mas baja de la lista es{menor_nota}"""")
