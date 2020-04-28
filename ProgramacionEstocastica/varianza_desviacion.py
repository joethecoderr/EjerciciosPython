import random
import math

def media(x):
    return sum(x)/len(x)

def varianza(X):
    mu = media(X)

    cum = 0

    for x in X:
        cum += (x - mu)**2

    return cum/len(X)

def desviacion_estandar(x):
    return math.sqrt(varianza(x))

if __name__ == '__main__':
    x = [random.randint(1,21) for i in range(20)]
    mu = media(x)
    Varianza = varianza(x)
    Desv_estandar = desviacion_estandar(x)

    print(f'Valores: {x}')
    print(f'Media: {mu}')
    print(f'Varianza: {Varianza}')
    print(f'Desviacion Estandar: {Desv_estandar}')