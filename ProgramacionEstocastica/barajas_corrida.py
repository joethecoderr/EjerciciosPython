import random
import collections

PALOS = ['espada', 'corazon', 'rombo', 'trebol']
VALORES = [1 , 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

def get_reales(valor_numerico):
    pass

def crear_baraja():
    barajas = []
    for palo in PALOS:
        for valor in VALORES:
            barajas.append((palo, valor))
    return barajas

def obtener_mano(barajas, tamano_mano):
    mano = random.sample(barajas, tamano_mano)
    return mano




def main(tamano_mano, intentos):
    barajas = crear_baraja()
    manos = []
    for _ in range(intentos):
        mano = obtener_mano(barajas, tamano_mano)
        manos.append(mano)

    print(mano)

    corridas = 0
    for mano in manos:
        valores = []
        valores_filtrados= []
        for carta in mano:
            valores.append(carta[1])
       # print(valores)

        for val in valores:
           # print(f'Val: {val}')
            if val not in valores_filtrados:
                valores_filtrados.append(val)
            else:
                pass


        #print(f'Valores filtrados: {valores_filtrados}')
        valores_filtrados_ordenados = sorted(valores_filtrados)
        
        #print(f'Valores Ordenados: {valores_filtrados_ordenados}')
        contador_consec = 0
        for i in range(0, len(valores_filtrados_ordenados)-1):
            
            #print(valores_filtrados_ordenados[i],valores_filtrados_ordenados[i+1])
            if len(valores_filtrados_ordenados) == 5:
                if valores_filtrados_ordenados[i] + 1 == valores_filtrados_ordenados[i+1]:
                    contador_consec += 1
                    if contador_consec == 4:
                        #print(f'{valores_filtrados_ordenados}')
                        
                        corridas += 1
                        print(f'Encontraste una corrida: {corridas}')
                        contador_consec = 0
                        break
                else:
                    break
            elif len(valores_filtrados_ordenados) > 5:
                if i < (len(valores_filtrados_ordenados) - 5):
                    print(f'{valores_filtrados_ordenados}')
                    i+=1
                    if valores_filtrados_ordenados[i] + 1 == valores_filtrados_ordenados[i+1]:
                        contador_consec += 1
                        if contador_consec == 4:
                            #print(f'{valores_filtrados_ordenados}')
                            
                            corridas += 1
                            print(f'Encontraste una corrida: {corridas}')
                            contador_consec = 0
                            break
                    else:
                        break
                else:
                    break
            elif len(valores_filtrados_ordenados) > 5  and i >= (len(valores_filtrados_ordenados) - 5):
                break





    

                



        """
        counter = dict(collections.Counter(valores_filtrados_ordenados))
        
        for val in counter.values():
            if val == 2:
                corridas +=1
                break
        """
    print(f'Corridas: {corridas}')
    probabilidad_par = corridas / intentos
    print(f'La probabilidad de obtener una corrida en una mano de {tamano_mano} es {probabilidad_par}')


if __name__ == '__main__':
    tamano_mano = int(input('De cuantas barajas sera la mano?: '))
    intentos = int(input('Cuantas simulaciones para calcular la probabilidad: '))
    main(tamano_mano, intentos)
    barajas = crear_baraja()
    mano = obtener_mano(barajas, 5)
