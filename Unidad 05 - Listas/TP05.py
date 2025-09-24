#1)Crear una lista con las notas de 10 estudiantes.
#•Mostrar la lista completa.
#•Calcular y mostrar el promedio.
#•Indicar la nota más alta y la más baja.
lista=[10,8,5,6,7,10,9,8,4,1]
suma=0
promedio=0
cantidad= len(lista)
menor_nota=0
mayor_nota=0
suma= sum(lista)
promedio= suma/cantidad
menor_nota=min(lista)
mayor_nota=max(lista)

print (f"""La lsita de notas es {lista}
La nota mas alta de la lista es {mayor_nota} 
La nota mas baja de la lista es {menor_nota}
El promedio de notas es {promedio}""")
