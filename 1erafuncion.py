import turtle

def main():
    window = turtle.Screen()
    dave = turtle.Turtle()
    make_rec(dave)

def make_rec(dave):
    length = int(input('Tamaño de cuadrado: '))
    for i in range(4):
        make_line(dave, length)
    input()

def make_line(dave, length):
    dave.forward(length)
    dave.left(90)

if __name__ == '__main__':
    main()