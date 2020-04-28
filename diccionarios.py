my_dict = {
    'Laura' : 27,
    'Idalia' : 50,
    'Juan' : 55,
    'Juan Jr.' : 18,
    'Ale Karam' : 27,
    
}

""" Se crea uno nuevo de la siguiente manera """

my_dict['Cleo'] = 6

""" Podes imprimir los nombres con el comando .keys() """

for nombres in my_dict.keys():
    print(nombres)

""" Podes imprimir las edades con el comando .values() """

for edad in my_dict.values():
    print(edad)

for nombres, edad in my_dict.items():
    print(nombres, edad)