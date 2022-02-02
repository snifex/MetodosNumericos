import numpy as np
import rungeKutta as rk
import math as math
import pandas as pd
import matplotlib as mlp

def main():
    #Datos iniciales
    Tinf = 7.2
    r0 = 1.0422
    Tincu = 3
    Tterap = 14
    Rinft = 0.2657
    Rsobre = .03
    Diasd = 5
    limite = 10

    
    #Ponemos el sistema de ecuaciones 
    S = lambda r,inf,n,x,i: -(r/(inf*n))*x*i
    E = lambda r,inf,n,x,inc,i: (r/inf*n)*x*i - (1/inc)*x
    I = lambda e,inc,x,inf: (1/inc)*e - (1/inf)*x
    H = lambda p,inf,i,th,x: (p/inf)*i - (1/th)*x
    R = lambda p,inf,i,q,th,h: ((1-p)/inf)*i - (q/th)*h
    F = lambda q,th,h: (1-q)/th*h

    #Leemos los datos del archivo csv
    datosCovid = leerDatos("datosCovid19Oaxaca.csv")
    
    #Creamos el array grande de 2 dimensiones
    X = np.zeros((6,datosCovid.__sizeof__),dtype=float)

    for datos in datosCovid:
        #iteramos en los datos obtenidos del CSV y lo añadiimos a un array
        Xs,Ys = rk.integrar(S(r0,rinft,diasd,datos[decesos],i),datos[dia],datos[decesos],limite,1)
        Xe,Ye = rk.integrar(E(r0,tinf,diasd,datos[decesos],Tincu,datos),datos[dia],limite,1)
        Xi,Yi = rk.integrar(I(Xe[datos],Tincu,datos[decesos],Tinf),datos[dia],datos[decesos],limite,1)
        Xh,Yh = rk.integrar(E(r0,tinf,diasd,datos[decesos],Tincu,datos),datos[dia],datos[decesos],limite,1)
        Xr,Yr = rk.integrar(R(Rsobre,Tinf,Xi,Diasd,Tterap,Xh),datos[dia],datos[decesos],limite,1)
        Xf,Yf = rk.integrar(F(Rinft,Rsobre,Tterap),1,8,20,1)

        #agregamos los resultados de los array en otro array
        X[0].append(Xs,Ys)
        X[1].append(Xe,Ye)
        X[2].append(Xi,Yi)
        X[3].append(Xh,Yh)
        X[4].append(Xr,Yr)
        X[5].append(Xf,Yf)
        
        
    

    
def leerDatos(archivoLeer):
    #con esta función obtenemos los datos del csv
    datosCovid = pd.read_csv(archivoLeer)
    return datosCovid

    
    

if __name__ == '__main__':
    main()
    