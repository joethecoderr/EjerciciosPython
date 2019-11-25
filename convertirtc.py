
def run():
    print('C A L C U L A D O R A  D E  D I V I S A S')
    print('Convierte pesos mexicanos a pesos colombianos')
    print('')

    amount = float(input('Introduce la cantidad en pesos mexicanos: '))
    tc = convierteTC(amount)
    print('${}  pesos mexicanos equivalen a ${} pesos colombianos'.format(amount, tc))

def convierteTC(amount):
    tc_hoy = 145.97
    return tc_hoy * amount


if __name__ == '__main__':
    run()