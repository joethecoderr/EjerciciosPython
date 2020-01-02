# -*- coding: utf-8 -*-

def run():
    with open('numeros.txt', 'w') as f:
        for i in range(10):
            f.write(str(i))


def run2():
    count = 0
    try:
        with open('aleph.txt') as f:
            for line in f:
                count += line.count('Beatriz')
    except UnicodeDecodeError:
        print('Ocurrio un error al leer el archivo')
    else:    
        print('Beatriz se encuentra {} en el texto'.format(count))


if __name__ == '__main__':
    run2()
