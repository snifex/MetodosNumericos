import math
import numpy as np
import matplotlib.pyplot as plt

#Valores iniciales
r0 = float(1.6)
Tinf = float(7.2)
Tincubacion = int(3)
Tintensiva = int(14)
Rinfectados = float(0.2657)
Rsobrevivientes = float(0.3)
Dpositivos = int(5)

def runge_kutta(y, x, dx, f):
    """ y is the initial value for y
        x is the initial value for x
        dx is the time step in x
        f is derivative of function y(t)
    """
    k1 = dx * f(y, t)
    k2 = dx * f(y + 0.5 * k1, x + 0.5 * dx)
    k3 = dx * f(y + 0.5 * k2, x + 0.5 * dx)
    k4 = dx * f(y + k3, x + dx)
    return y + (k1 + 2 * k2 + 2 * k3 + k4) / 6.


if __name__=='__main__':
    t = float(0)
    y = float(1)
    dt = float(1)
    ys, ts = [], []

    
    while t <= 10:
        y = runge_kutta(y, t, dt, func)
        t += dt
        ys.append(y)
        ts.append(t)

    exact = [(t ** 2 + 4) ** 2 / 16. for t in ts]
    plt.plot(ts, ys, label='runge_kutta')
    plt.plot(ts, exact, label='exact')
    plt.legend()
    plt.show()
    error = np.array(exact) - np.array(ys)
    print("max error {:.5f}".format(max(error)))