import random

def tirar_dado(numero_tiros):
    secuencia_tiros = []

    for _ in range(numero_tiros):
        tiro = random.choice([1,2,3,4,5,6])
        secuencia_tiros.append(tiro)
    return secuencia_tiros


def main(numero_tiros, numero_intentos):
    tiros_dado1 = []
    tiros_dado2 = []
    for _ in range(numero_intentos):
        secuencia_tiros1 = tirar_dado(numero_tiros)
        secuencia_tiros2 = tirar_dado(numero_tiros)
        tiros_dado1.append(secuencia_tiros1)
        tiros_dado2.append(secuencia_tiros2)
            


    tiros_con_1 = 0
    for tiro in tiros_dado1:
        if 6 in tiro:
            tiros_con_1 += 1

    tiros_con_2 = 0
    for tiro in tiros_dado2:
        if 6 in tiro:
            tiros_con_2 += 1


    probab_tiros_con_1 = tiros_con_1/numero_intentos
    probab_tiros_con_2 = tiros_con_2/numero_intentos
    probab_total = probab_tiros_con_1 * probab_tiros_con_2
    print(f'La probabilidad de obtener por lo menos un 12 en {numero_tiros} tiros es igual a {probab_total}')
    


if __name__ == '__main__':
    numero_tiros = int(input('Cuantos tiros del dado?: '))
    numero_intentos = int(input('Cuantas veces correra la simulacion?: '))

    main(numero_tiros, numero_intentos)