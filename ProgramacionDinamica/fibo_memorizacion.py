import sys

def fibo_recursivo(n):
    if n == 0 or n == 1:
        return 1

    return fibo_recursivo(n - 1) + fibo_recursivo(n - 2)

def fibo_dinamico(n, memo = {}):
    if n == 0  or n == 1:
        return 1
    try:
        return memo[n]
    except KeyError:
        resultado = fibo_dinamico(n - 1) + fibo_dinamico(n  - 2)
        memo[n] = resultado

        return resultado


if __name__ == '__main__':
    sys.setrecursionlimit(10002)
    n = int(input('Escoge un numero: '))
    resultado = fibo_dinamico(n)
    print(resultado)
