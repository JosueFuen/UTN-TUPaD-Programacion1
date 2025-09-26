#9)Representar un tablero de Ta-Te-Ti como una lista de listas (3x3).
#•Inicializarlo con guiones "-" representando casillas vacías.
#•Permitir que dos jugadores ingresen posiciones (fila, columna) para colocar "X" o "O".
#•Mostrar el tablero después de cada jugada.
TaTeTi=[["-", "-", "-"],["-", "-", "-"],["-", "-", "-"]]
for x in TaTeTi:
    print(x)
    opcion="a"
while opcion!="E"
    
    colum=int(input("Jugador 1, indica en que columna deseas marcar: "))
    fila=int(input("Jugador 1, indica en que fila deseas marcar: "))
    TaTeTi[fila][colum]="X"
    for x in TaTeTi:
        print(x)
    colum=int(input("Jugador 2, indica en que columna deseas marcar: "))
    fila=int(input("Jugador 2, indica en que fila deseas marcar: "))
    TaTeTi[fila][colum]="O"
    for x in TaTeTi:
        print(x)