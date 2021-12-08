
import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

# funcion f(x) que se utilizara en el ejemplo


def f(x): return 1/x


def interpolacionLagrange(f):
    """
    Polinomio de Lagrange
    --------
    Parametros:
    f = función que se utlizara para rellenar 

    ------
    Resultado
    Grafica con el polinomio obtenido
    """

    import numpy as np
    import sympy as sym
    import matplotlib.pyplot as plt

    # xs son los valores que toma la funcion para X0 = 2 , X1= 2.5, X2=4
    xs = np.array([2, 2.5, 4])
    fs = np.array([f(xs[0]), f(xs[1]), f(xs[2])])
    polinomio = 0
    numerador = 1
    denominador = 1

    # Obtenemos el dato n de xs
    n = len(xs)
    x = sym.Symbol('x')
    divisorL = np.zeros(n, dtype=float)
    for i in range(0, n, 1):

        for j in range(0, n, 1):
            if (j != i):
                numerador = numerador*(x-xs[j])
                denominador = denominador*(xs[i]-xs[j])
        Li = numerador/denominador

        polinomio = polinomio + Li*fs[i]
        divisorL[i] = denominador

    # se simplifica el polinomio y se evalua
    polisimple = polinomio.expand()
    px = sym.lambdify(x, polisimple)

    # Puntos para la gráfica
    muestras = 50
    a = np.min(xs)
    b = np.max(xs)
    pxi = np.linspace(a, b, muestras)
    pfi = px(pxi)

    """
    Si se gusta visualizar el polinomio descomenten estas lineas
    print('Polinomio de Lagrange: ')
    print(polisimple)
    """

    # Gráfica
    plt.plot(xs, fs, 'o', label='Puntos')
    plt.plot(pxi, pfi, label='Polinomio')
    plt.legend()
    plt.xlabel('xi')
    plt.ylabel('fi')
    plt.title('Interpolación Lagrange')
    plt.show()

#Probamos la función
interpolacionLagrange(f)
