from persona import Persona

def run():
    joel = Persona('Joel', 26)
    anahi = Persona('Anahi', 25)
    joel.saluda(anahi)

if __name__ == '__main__':
    run()