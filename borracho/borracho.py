import random

class Borracho:
    def __init__(self, nombre):
        self.name = nombre

class BorrachoTradicional(Borracho):
    def __init__(self, nombre):
        super().__init__(nombre)
        self.moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    def camina(self):
        
        return random.choice(self.moves)

class BorrachoSinPie(Borracho):
    def __init__(self, nombre):
        super().__init__(nombre)
        
    def camina(self):
        moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        rand = random.choices(moves,  weights = [2,1,1,1], k=1)
        return rand[0]