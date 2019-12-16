import random

IMAGES = ['''

    +---+
    |   |
        |
        |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
        |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
    |   |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|   |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
    |   |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
    |   |
   /    |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
    |   |
   / \  |
        =========''', '''
''']

WORDS = [
    'lavadora',
    'secadora',
    'sofa',
    'gobierno',
    'diputado',
    'democracia',
    'computadora',
    'teclado',
    'AMLO',

]

def random_word():
    idx = random.randint(0, len(WORDS) - 1)
    return WORDS[idx]

def display_board(hidden_word, tries):
    print(IMAGES[tries])
    print('')
    print(hidden_word)
    print('-------*-------------*-------------*-----------*')

def run():
    word = random_word()
    hidden_word =  ['-'] * len(word)
    tries = 0

    while True:
        display_board(hidden_word, tries)

        curr_letter = str(input('Escoge una letra: '))

        letter_idx = []
        for i in range(len(word)):
            if word[i] == curr_letter:
                letter_idx.append(i)
                
        if len(letter_idx) == 0:
            tries += 1
            if tries == 7:
                display_board(hidden_word, tries)
                print('')
                print('Perdiste! la palabra correcta era {0}'.format(word))
                break

        else:
            for i in letter_idx:
                hidden_word[i] = curr_letter
            letter_idx = []  
        try:
            hidden_word.index('-')
        except ValueError:
            
            print('')
            print('Ganaste')
            break

            



if __name__ == '__main__':
    print('BIENVENIDOS AL JUEGO DE AHORCADOS')
    run()