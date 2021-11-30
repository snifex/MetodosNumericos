import numpy as np
import math as math

def sustitucionDelante(A,n):
    resultado = []
    tamanioN = len(n)
    acum = float(0)

    for i in range(tamanioN):
        acum = n[i]
        if i >= 1:
            for j in range(i):
                acum -= A[i][j] * resultado[j]
        acum /= A[i][i]
        resultado.append(acum)
    return resultado

def sustitucionAtras(mat, n):
	tamanioN = len(n)
	resultado = np.zeros(tamanioN)
    
	for i in range(1, tamanioN+1):
		acum = float(0)
		acum = n[tamanioN - i]
		if tamanioN - i <= tamanioN - 2:
			for j in range(1, i):
				acum -= mat[tamanioN-i][tamanioN-j] * resultado[tamanioN-j]
		acum /= mat[tamanioN-i][tamanioN-i]
		resultado[tamanioN-i] = acum
	return resultado    




def factorizacionLU(A,n):
    L = np.zeros(pow(n,2)).reshape(n,n)
    U = np.array(len(n))

    for i in range(len(n)):
        L[i][i] = 1

    for i in range(1,len(A[0])):
        for j in range(n):
            L[i][j] = U[i][j] / U[j][j]
            U[i] = U[i] - U[i][j] / U[j][j] * U[j]
    return (L,U)
    

def diagonalDominanteComprobar(A,n):
    """[summary]

    Args:
        A (Matriz): Matriz con elementos
        n (Int): Tamaño de la matriz 

    Returns:
        boolean: True si converge la matriz, false si diverge
    """
    acumulador = float(0)
    for i in range(n):
        for j in range(n):
            acumulador += abs(A[i][j]) 
            if(j == n):
                acumulador = A[i][i] - acumulador
                if(abs(A[i][i]) < acumulador):
                    return False
                
    return True


def metodoJacobi(A,b,x0,iter,n):
    auxiliar = float(0)
    X = []
    X.append(x0)
    k = 1

    #Comprobamos que converga a alguna solución antes de resolver el sistema comprobando si es estrictamente diagonal dominante
    if diagonalDominanteComprobar(A,n) != True:
        return print("Este sistema matricial no convergera")

    while True or k < 30:
        #Historial de las iteraciones
        historial = []

        for i in range(n):
            resultado = b[i]
            for j in range(n):
                if j != 1:
                    resultado -= A[i][j] * historial[k-1][j]
            resultado /= A[i][i]

            #Agregamos a Historial
            historial.append(resultado)

        #Comprobamos error relativo
        ER = errorRelativoNormaEuclidiana(historial,X[k-1])
        if(ER < 1e-5):
            break

        X.append(historial)
        k += 1
    return X.pop() #devolvemos el ultimo valor de historial

def errorRelativoNormaEuclidiana(x1,x2):
    """[summary]

    Args:
        x1 (Vector): Vector x0
        x2 (Vector): Vector x1

    Returns:
        Float: Resultado de dividir el numerador y el denominador de la suma de sus elementos de los vectores
    """
    numerador = float(0)
    denominador = float(0)
    for i in range(len(x2)):
        numerador += pow((x2[i] - x1[i]),2) 
        denominador += pow(x1[i],2)
    numerador = math.sqrt(numerador)
    denominador = math.sqrt(denominador)
    
    resultado = numerador/denominador

    return resultado
    



