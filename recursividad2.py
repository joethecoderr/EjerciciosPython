"""
Calcula factorial
Recibe un numero del usuario
"""
def factorial(n):
    if n == 0:
        return 0
    if n == 1:
        return 1 

    return n * factorial(n-1)

if __name__ == '__main__':

    n = int(input('Ingresa el numero a calcular: '))
    r = factorial(n)
    print(f'El factorial de {n} es {r}')
