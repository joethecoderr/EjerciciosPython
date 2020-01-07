import random

contador_binario = 0

def busqueda_binaria(lista, comienzo, final, objetivo):
    global contador_binario
    contador_binario += 1

    if comienzo > final:
        return False
    medio  = (comienzo + final ) // 2

    if lista[medio] == objetivo:
        
        return True
    elif lista[medio] < objetivo:

        return busqueda_binaria(lista, medio + 1, final, objetivo)
    elif lista[medio] > objetivo:
        return busqueda_binaria(lista, comienzo, medio-1, objetivo)


def busqueda_lineal(lista, objetivo):
    match = False
    contador = 0
    for i in lista:
        contador+=1
        if i == objetivo:
            match = True
            break
    print('')
    print('')
    print('Busqueda Lineal cuenta: {}'.format(contador))
    return match


if __name__ == '__main__':
    size_list = int(input('De que tamaño sera la lista?: '))
    objetivo = int(input('Que numero quieres encontrar?: '))

    lista = sorted([random.randint(0,100) for i in range(size_list)])
    encontrado = busqueda_binaria(lista, 0, len(lista) -1, objetivo)
    print(lista)
    
    if encontrado:
        print('Busqueda Binaria cuenta: {} '.format(contador_binario))
        print('El elemento {} está en la lista'.format(objetivo))
    else:
        print('Busqueda Binaria cuenta: {} '.format(contador_binario))
        print('El elemento {} no está en la lista'.format(objetivo))

    encontrado_lineal = busqueda_lineal(lista, objetivo)
    if encontrado_lineal:
        print('El elemento {} está en la lista'.format(objetivo))
    else:
        print('El elemento {} no está en la lista'.format(objetivo))

