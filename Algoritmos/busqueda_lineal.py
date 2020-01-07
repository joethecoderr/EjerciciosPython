import random

def busqueda_lineal(lista, objetivo):
    match = False

    for i in lista:
        if i == objetivo:
            match = True
            break
    return match

if __name__ == '__main__':
    size_list = int(input('De que tamaño sera la lista?: '))
    objetivo = int(input('Que numero quieres encontrar?: '))

    lista = [random.randint(0,100) for i in range(size_list)]
    lista.sort()
    encontrado = busqueda_lineal(lista, objetivo)
    print(lista)
    if encontrado:
        print('El elemento {} está en la lista'.format(objetivo))
    else:
        print('El elemento {} no está en la lista'.format(objetivo))
