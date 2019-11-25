
def run():
    print('Programita para saber si un numero es primo o no')
    num = int(input('Introduce un numero: '))
    primo = determina(num)
    if primo:
        print('Es primo')
    else:
        print('No es primo')

def determina(num):
    
    if(num<2):
        return True
    elif(num == 2):
        return True
    
    else:
        for i in range(3, num):
            res = num%i
            if(res == 0):
                return False
            else:
                pass
        return True

    

         

if __name__ == '__main__':
    run()