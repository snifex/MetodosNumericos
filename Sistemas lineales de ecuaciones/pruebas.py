import numpy as np
import math as math
import metodosSistemas as metodosSistemas

def main():
    n = int(input("Ingresa el tamaño de la matriz"))
    A = np.arange(n*n).reshape(n,n)
    columna = []

    for i in range(n):
        for j in range(n):
            print("A[{}][{}] = {}\n".format(i,j,A[i][j]))

    #Aplicamos factorización LU
    resultados = metodosSistemas.factorizacionLU(A,columna)
    (L,U) = resultados

    print("L = {}\n".format(L))
    print("U = {}\n".format(U))

if __name__ == '__main__':
    main()