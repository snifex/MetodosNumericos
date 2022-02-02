import numpy as np
import rungeKutta as rk
import math as math

def main():
    #Datos iniciales
    Tinf = 7.2
    r0 = 1.0422
    Tincu = 3
    Tterap = 14
    Rinft = 0.2657
    Rsobre = .03
    Diasd = 5

    S = lambda r,inf,n,x,i: -(r/(inf*n))*x*i
    E = lambda r,inf,n,x,inc,i: (r/inf*n)*x*i - (1/inc)*x
    I = lambda e,inc,x,inf: (1/inc)*e - (1/inf)*x
    H = lambda p,inf,i,th,x: (p/inf)*i - (1/th)*x
    R = lambda p,inf,i,q,th,h: ((1-p)/inf)*i - (q/th)*h
    F = lambda q,th,h: (1-q)/th*h

    X,Y = rk.integrate(F(Rinft,Rsobre,Tterap),1,8,20,1)

    for i in X:
        print(i)

    
    

if __name__ == '__main__':
    main()
    