import numpy as np
import math as math

def metodoGaussSeidel(A,x,x0,iter,n):
	"""
	Metodo de Gauss-Seidel
	________________________
	Parametros
	A = matriz A 
	x = matriz columna que recibe que son los resultados de A ecuaciones
	x0 = matriz columna con los x0 iniciales que recibe
    iter= numero maximo de iteraciones que hara
    n = dimension de la matriz
	________________________
	Salida
	
	"""
	resultado = np.arange(iter*n).reshape(iter,n)



def main():
    n = int(input("Ingresa el tamanio de la matriz n: "))
    A = np.arange(n*n,dtype=float).reshape(n,n)
    
    """
    n+1 tomando en cuenta que el renglon b = resultados esta añadido en la matriz A

    [[ 0      0.1    -0.2     0   ]
    [ 0.0909  0.      0.2727  0.0909]
    [-0.2     0.1     0     0.1   ]
    [ 0.     -0.375   0.125   0]]
    """

    for i in range(n):
        for j in range(n):
            A[i][j] = float(input("Ingresa el valor que tomarara la posicion A[{}][{}]: ".format(i,j)))

    print(A)        

    x0 = np.zeros((n,1))
    print("\n")
    print(x0)

if __name__ == '__main__':
    main()


