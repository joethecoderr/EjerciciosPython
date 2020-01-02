class Casilla:
    def __init__(self, identificador, pais):
        self.identificador = identificador
        self._pais = pais
        self._region = None
    @property
    def region(self):
        return self._region
    
    @region.setter
    def region(self, region):
        if region in self._pais:
            self._region = region
        else:
            print('La region {} no es valida en {}'.format(region, self._pais))
        
    

def run():
    casilla = Casilla(123, ['CDMX', 'Morelos'])
    print(casilla.region)
    print(casilla._pais)
    casilla.region = 'Moreloss'
    

if __name__ == '__main__':
    run()