def imprimir(m,f,c):
    filas=len(m)
    columnas=len(m[0])
    print("\n")
    for i in range(filas):
        for j in range(columnas):
            print(m[i][j],sep=' , ',end=' ')
        print("\n")

def llenarmatriz(m,f,c):
    for f in range(filas):
        matriz.append([])
        for c in range(columnas):
            print(f'columnas {c} filas {f}')
            valor=int(input("valor: "))
            matriz[f].append(valor)

def acumulador_filas(m,f,c):
    for f in range(filas):
        acumulador_filas=0
        for c in range(columnas):
            acumulador_filas=acumulador_filas+matriz[f][c]
        print(f'la suma de la fila {f} es {acumulador_filas}')

def acumulador_columnas(m,f,c):
    for c in range(columnas):
        acumulador_columnas=0
        for f in range(filas):
            acumulador_columnas=acumulador_columnas+matriz[f][c]
        print(f'la suma de la columna {c} es {acumulador_columnas}')


def sumaDiagonal(m,f,c):
    for c in range(columnas):
        sumDiagonal=0
        for f in range(filas):
            if f==c:
                sumDiagonal=sumDiagonal+matriz[f][c]
    print("la suma diagonal es: ", sumDiagonal)



while True:
    filas=int(input("ingrese cantidad de filas: "))
    if filas>0:
        break

    else:
        print("el numero de filas debe ser mayor que 0 ")

while True:
    columnas=int(input("ingrese cantidad de columnas: "))
    if columnas>0:
        break

    else:
        print("el numero de columnas debe ser mayor a 0 ")





matriz=[]
print(f'la matriz esta compuesta por {filas} filas y {columnas} columnas')
llenarmatriz(matriz,filas,columnas)
imprimir(matriz,filas,columnas)
acumulador_filas(matriz,filas,columnas)
acumulador_columnas(matriz,filas,columnas)
if filas==columnas:
    print("la matriz es cuadrada")

sumaDiagonal(matriz,filas,columnas)







