import numpy as np
import math as math

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
    historial = np.arange(iter*n).reshape(iter,n)
    matrizAux = np.arange(n*n+n,dtype=float).reshape(n,n+1) 

    #Comprobamos que converga a alguna solución antes de resolver el sistema comprobando si es estrictamente diagonal dominante
    if diagonalDominanteComprobar(A,n) != True:
        return print("Este sistema matricial no convergera")

    #Pasamos los resultados en una matriz auxiliar
    
    for i in range(n):
        for j in range(n):
            if j == i:
                matrizAux[i][i] = float(0) #Diagonal de la matriz == 0
            elif j == i-1:
                matrizAux[i][j] = b[i]/A[i][i]
            else:
                matrizAux[i][j] = -(A[i][j]/A[i][i])
    print(matrizAux)             

               

    """
    for recorreIteraciones in range(iter):
        for i in range(n):
            for j in range(n):
                auxiliar += matrizAux[i][j] * x0[i]
                if j == i:
                    auxiliar -= matrizAux[i][i]
            auxliar = matrizAux[i][i]   
        
        #Calulamos error relativo
    """
            
            


    
            
    


def main():
    n = int(input("Ingresa el tamanio de la matriz n: "))
    A = np.arange(n*n,dtype=float).reshape(n,n)
    #A = np.array([[3,-1,-1],[-1,3,1],[2,1,4]],dtype=float)
    x0 = np.zeros((n,1))
    b = np.arange(3).reshape(1,n)
    
    """
    n+1 tomando en cuenta que el renglon b = resultados esta añadido en la matriz A

    [[ 0      0.1    -0.2     0   ]
    [ 0.0909  0.      0.2727  0.0909]
    [-0.2     0.1     0     0.1   ]
    [ 0.     -0.375   0.125   0]]
    """
    print(A)        
    metodoJacobi(A,b,x0,30,n)
    
    print("\n")
    print(x0)


if __name__ == '__main__':
    main()


