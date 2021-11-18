import nolinealesf0 as nol
import math
import numpy as np

																			

def f(x):		#Aqui editamos la función que se le requiera pasar
	return pow(math.e,x) - x - 2
	
	
"""
Para que el programa corra correctamente debemos modificar la funcion f() con la función en su forma
f(x) = 0 en este caso la funcion es e^x - x - 2 = 0
"""

def g1(x):
	return x-pow(x,3) - 4*pow(x,2) + 10

def g2(x):
	return math.sqrt(((10/x)-4*x))

def g3(x):
	return math.sqrt(10-pow(x,3))/2

def g4(x):
	return math.sqrt(10/(4+x))

"""
Para que la funcion punto fijo funcione correctamente debemos pasarle las fuciones de esta forma
"""

def main():
	"""
	a = input("Ingresa el valor de a_1: ")
	b = input("Ingresa el valor de b_1: ")

	a = float(a)															BISECCION
	b = float(b)

	datosRecibidos = ( )
	datosRecibidos = nol.metodoBiseccion(f,a,b) #nos devuelve 2 valores la funcion metodoBisección en una tupla el 
	(l , i) = datosRecibidos					#1er valor es el ultimo punto medio y el 2do el valor de i (iteraciones hechas)
	valorUltimo = l
	l = f(l)
	limited_f = round(l,2)

	print("\nP({}) = {} (llega a error y se termina el programa antes de que ocurra desbordamiento)".format(i+2,limited_f))
	print("\nValor de la ultima iteración antes de llegar a error P({}) = {}".format(i+1,valorUltimo))
	"""
	p_0 = float(input("Ingresa el valor de p_0 (p₀): "))
	datosRecibidos = ( )

	datosRecibidos = nol.iteracionPuntoFijo(g3,p_0,10E-10)
	p = np.zeros(30,dtype=int)
	print(datosRecibidos)

	(p,i) = datosRecibidos
	
	#print("La raiz real de la función probada es con {:.4f} probada con la g3".format(p[i]))



	

if __name__ == '__main__':
	main()