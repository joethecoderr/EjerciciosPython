def func1(un_arg, una_func):
    print(f'Step 0, arg: {un_arg}')
    
    """define una funcion dentro de otra"""
    def func2(otro_arg):
        print(f'Step 1, arg: {otro_arg}')
        return otro_arg * 2

    """Aqui se llama a la funcion que se definio arriba"""
    valor = func2(un_arg)

    """ se retorna la funcion que llego como parametro,
        ademas se le envia el parametro que requiere esa funcion
        """
    return una_func(valor)

un_arg = 1


"""Esta funcion regresa el computo final del la variable 'un_arg'
    siendo este (1*2) + 5, ya que func2 retorna un_arg * 2
    y cualquier_func retorna ese un_arg + 5
    """
def cualquier_func(cualquier_arg):
    print(f'Step 2, arg: {cualquier_arg}')
    return cualquier_arg + 5

valor_final = func1(un_arg, cualquier_func)
print(valor_final)