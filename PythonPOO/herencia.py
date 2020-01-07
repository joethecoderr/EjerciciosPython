class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base *  self.altura

    def area(self, palabra):
        print(palabra)

class Cuadrado(Rectangulo):
    def __init__(self, lado):
        super().__init__(lado, lado)

if __name__ == '__main__':
    rectangulo = Rectangulo(3,4)
    print(rectangulo.area())
    rectangulo.area('Si funciona asi')
    cuadrado = Cuadrado(5)
    print(cuadrado.area())
    print(cuadrado.base)