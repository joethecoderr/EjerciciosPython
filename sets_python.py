def run(numero):
    s = set([1,2,3])
    t = set([3,4,5])
    print('Union: {}'.format(s.union(t)))
    print('Interseccion: {}'.format(s.intersection(t)))
    print('Diferencia: {}'.format(s.difference(t)))
    if numero in s or numero in t:
        print('Si esta')
    else:
        print('No esta')

if __name__ == '__main__':
    numero = int(input('Ingresa un numero: '))
    run(numero)



