"""Busqueda de Raices 
Este modulo contiene 2 metodos para encontrar las raices de ecuaciones no lineales
de la forma f(x) = 0, con f como función real de variables reales, continua

Programado por Gerardo Gonzalo Nuñez Bello
"""
import numpy as np
import math as math

def metodoBiseccion(f,a,b):
	"""Metodo de Bisección
	   Encuentra una raiz de la función f en el intervalo [a,b] mediante
	   el metodo de bisección o busqueda binaria

	Argumentos
	--------------
	f = Función continua, real, tal que f(a) f(b) < 0
	a = Extremo inferior del intervalo
	b = Extremo superior del intervalo
	______________

	toler = tolerancia, en este caso sera de 10 e -10 (constante)
	x = operación de la bisección
	p[i] = elemento del arreglo que regresa como raiz en el periodo [a,b]
	______________
	"""

	toler = 10E-10

	if np.sign(f(a)) == np.sign(f(b)):
		raise OppositeSigns("No tienen signos opuestos segun Bolzano")

	if a > b:
		raise ValueError("Intervalo mal definido")

	x = a + ((b - a)/2.0)
	p = np.full(1,x) #Creamos el arreglo donde se almacenaran los puntos medios (el primer elemento es f(p1))
	i = int(0)

	while True:
		if np.sign(f(p[i])) <= 0:
			return (p[i],i)
		else:
			if np.sign(f(p[i])) == np.sign(f(a)):		#Si f(p1) y f(a) signos == entonces p ∈ (p1,b1)
				a = p[i]
			else:
				b = p[i]								#Si f(p1) y f(a) signos != entonces p ∈ (a1,p1)

		
		#criterios de parada
		if abs(f(p[i])) < toler :
			return (p[i],i)
		elif (abs(f(p[i-1]-p[i])))/abs(p[i]) <= toler:
			return (p[i],i)

		x = a + ((b - a) / 2.0) #vuelve a hacer la biseccion
		i+=1
		p = np.append(p,x)
		pass

def iteracionPuntoFijo(g,p_0,tol):
	"""Metodo de Interación de punto fijo

	Parametros
	_______________
	g = Función continua a la que esta en forma de punto fijo para encontrar solución
	p_0 = Punto medio donde iniciara la iteracion (P₀)
	tol = tolerancia para la parada
	______________
	Salida
	0 = hubo un error y no encontro el punto fijo
	(el arreglo de p e i(contador))
	"""
	i = int(0)	#Inicializamos la variable contadora
	n = 30 #numero maximo de iteraciones
	p = np.zeros(30,dtype=float) #Arreglo donde se almacenaran los resultados de cada iteración para poder imprimir despues
	print("iteración:{} : p_{} = {}".format(0,0,p_0))

	while i <= n:
		pChange = g(p_0)
		critPar = abs(pChange - p_0)
		print("iteración:{} : p_{} = {:-7f}, eAbs = {:.7f}".format(i,i,pChange,critPar))
		if critPar < tol: 	#criterio de parada
			return (p,i)
		i += 1
		p = np.append(p,pChange)
		p_0 = pChange

	return (p,i)

