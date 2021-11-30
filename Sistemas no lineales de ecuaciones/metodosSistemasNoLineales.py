import numpy as np
import math as math



def jacobiIterativo(vector, ecs, toler, iter, n):
    var = [0,1,2]
    resultado = []
    iter += 1

    for i in range(n):
        #Sacamos el valor de Xᵢ 
        var.remove(i)
        resultado.append(ecs[i](vector[var[0]], vector[var[1]]))

    ER = errorRelativoNormaInfinita(resultado,vector)
    if ER < toler:
        return [resultado, iter]
    else:
        return jacobiIterativo(resultado,ecs,toler,iter,n)        


def errorRelativoNormaInfinita(xk,k0):
    numerador = []
    denominador = []
    for i in range(len(xk)):
        numerador.append(abs(xk[i] - k0[i]))    
        denominador.append(abs(xk[i]))

    #Sacamos el valor maximo del numerador y el denominador y lo dividimos para sacar el ER
    maxNumerador = max(numerador)
    maxDenominador = max(denominador)
    resultado = maxNumerador/maxDenominador

    return resultado


    