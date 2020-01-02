class Lavadora:
    def __init__(self):
        pass
    
    def Lavar(self, temp = 'Caliente'):
        self._llenar_tanque(temp)
        self._add_jabon()
        self._lavar()
        self._centrifugar()
    
    def _llenar_tanque(self, temperatura):
        print('Llenando el tanque con agua {}'.format(temperatura))
    
    def _add_jabon(self):
        print('Añadiendo jabon')

    def _lavar(self):
        print('Lavando....')

    def _centrifugar(self):
        print('Centrifugando...')

def run():
    lavadora = Lavadora()
    lavadora.Lavar()

if __name__ == '__main__':
    run()