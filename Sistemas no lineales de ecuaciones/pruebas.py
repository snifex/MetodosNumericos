import numpy as np
import math as math
import metodosSistemasNoLineales as metNol

def main():
    #Declaramos las ecuaciones    
    ec1Original = lambda x1,x2,x3: 3 * x1 - math.cos(x2*x3) - 0.5
    ec2Original = lambda x1,x2,x3: pow(x1,2) - 81 * pow((x2 + 0.1),2) + math.sin(x3) + 1.06
    ec3Original = lambda x1,x2,x3: math.exp(-x1*x2) + 20 * x3 + (3 - 10 * math.pi ) / 60

    ec1Despejada = lambda x1,x2,x3: (math.cos(x2 * x3) + 0.5) / 3
    ec2Despejada = lambda x1,x2,x3: math.sqrt(x1 ** 2 + math.sin(x3) + 1.06) / 9 - 0.1
    ec3Despejada = lambda x1,x2,x3: -(math.exp(-x1 * x2) / 20) + (3 - 10 * math.pi) / 60

    n = int(input("Introduce el numero de ecuaciones: "))
    vectorSolucion = np.zeros(3)
    ecuacionesParametros = []
    ecuacionesParametros.append(ec1Despejada)
    ecuacionesParametros.append(ec2Despejada)
    ecuacionesParametros.append(ec3Despejada)

    resultado = metNol.jacobiIterativo(vectorSolucion, ecuacionesParametros , 1e-5, 0, n)

    print("Resultado\n")
    #imprimimos los resultados
    print("Ecuación 1 = {}".format(ec1Original(resultado[0],resultado[1],resultado[2])))
    print("Ecuación 2 = {}".format(ec2Original(resultado[0],resultado[1],resultado[2])))
    print("Ecuación 3 = {}".format(ec3Original(resultado[0],resultado[1],resultado[2])))


if __name__ == '__main__':
    main()