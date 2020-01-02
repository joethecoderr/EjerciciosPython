class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saluda(self, otra_persona):
        print('Hola, {}, te saluda {}'.format(otra_persona.nombre, self.nombre))
