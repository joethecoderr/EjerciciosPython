class Persona:

    def __init__(self, nombre):
        self.nombre = nombre
    
    def avanza(self):
        print('Caminando ando')

class Ciclista(Persona):

    def __init__(self, nombre):
        super().__init__(nombre)

    def avanza(self):
        print('Pedaleando ando')

if __name__ == '__main__':
    persona = Persona('Joel')
    cicilista = Ciclista('Joel')
    persona.avanza()
    cicilista.avanza()