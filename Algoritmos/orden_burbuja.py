import random

def ordenar_burbuja(lista):
    n = len(lista)
    
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j] 
    return lista

if __name__ == '__main__':
    size_list = int(input('De que tamaño sera la lista?: '))
    

    lista = [random.randint(0,100) for i in range(size_list)]
    print(lista)
    lista_ordenada = ordenar_burbuja(lista)
    
    print(lista_ordenada)
