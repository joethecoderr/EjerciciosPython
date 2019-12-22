KEYS = {
    'a': 'w',
    'b': 'E',
    'c': 'x',
    'd': '1',
    'e': 'a',
    'f': 't',
    'g': '0',
    'h': 'C',
    'i': 'b',
    'j': '!',
    'k': 'z',
    'l': '8',
    'm': 'M',
    'n': 'I',
    'o': 'd',
    'p': '.',
    'q': 'U',
    'r': 'Y',
    's': 'i',
    't': '3',
    'u': ',',
    'v': 'J',
    'w': 'N',
    'x': 'f',
    'y': 'm',
    'z': 'W',
    'A': 'G',
    'B': 'S',
    'C': 'j',
    'D': 'n',
    'E': 's',
    'F': 'Q',
    'G': 'o',
    'H': 'e',
    'I': 'u',
    'J': 'g',
    'K': '2',
    'L': '9',
    'M': 'A',
    'N': '5',
    'O': '4',
    'P': '?',
    'Q': 'c',
    'R': 'r',
    'S': 'O',
    'T': 'P',
    'U': 'h',
    'V': '6',
    'W': 'q',
    'X': 'H',
    'Y': 'R',
    'Z': 'l',
    '0': 'k',
    '1': '7',
    '2': 'X',
    '3': 'L',
    '4': 'p',
    '5': 'v',
    '6': 'T',
    '7': 'V',
    '8': 'y',
    '9': 'K',
    '.': 'Z',
    ',': 'D',
    '?': 'F',
    '!': 'B',
}


def cifrar(message):
    words = message.split( )
    cypher_msg = []
    
    for word in words:
        cypher_word = ''
        for letter in word:
            cypher_word += KEYS[letter]

        cypher_msg.append(cypher_word)
    return ' '.join(cypher_msg)



def descifrar(message):
    words = message.split(' ')
    msg_descifrado = []
    

    for word in words:
        decypher_word = ''

        for letter in word:
            for key, value in KEYS.items():
                if value == letter:
                    decypher_word += key
        msg_descifrado.append(decypher_word)
    return ' '.join(msg_descifrado)

def run():

    while True:
        cmd = str(input('''Encriptar/Desenriptar mensajes. Elija una opcion:
        
        a) Cifrar mensaje
        b) Descrifrar mensaje
        c) Salir
        '''))

        if cmd == 'a':
            msg = str(input('Escribe tu mensaje: '))
            
            msg_cifrado = cifrar(msg)
            print(msg_cifrado)
        elif cmd == 'b':
            msg = str(input('Escribe tu mensaje cifrado: '))
            msg_descifrado = descifrar(msg)
            print(msg_descifrado)
        elif cmd == 'c':
            break
        else:
            print ('Opcion Invalida')

if __name__ == '__main__':
    run()