def run():
    total = 0
    avg = 0
    calif = {}
    calif['algoritmos'] = 9
    calif['matematicas'] = 10
    calif['web'] = 8
    calif['bases_datos'] = 10
    for key in calif:
        print(key)
    for value in calif.values():
        print(value)
    for key, value in calif.items():
        print(key, value)

    for value in calif.values():
        total += value
    avg = total /  calif.__len__()
    print('')
    print('El promedio es: {}'.format(avg))

if __name__ == '__main__':
    run()