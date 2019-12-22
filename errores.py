countries = {
'mexico': 122,
'colombia': 49,
'argentina': 43,
'chile': 18,
'peru': 31
}


def run():

    while True:
        country = input('Escribe el nombre de un país: ').lower()

        try:
            print('La poblaciónde {} es: {} millones'.format(country, countries[country]))
        except KeyError:
            respuesta = input('No tenemos el dato dela poblaciónde {}, ¿Desea agregarlo? SI(S), NO (N):'.format(country))
            if respuesta.upper() == 'S':
                poblacion = int(input('Ingresa la pobalcion de {}:'.format(country)))
                countries[country]= poblacion

if __name__ == '__main__':
   
    run()