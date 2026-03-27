import random


def atividade1():
    x  =  random.randint(5,10)
    return x




def atividade2():
    x  =  random.randint(1,10)
    y  =  random.randint(1,10)
    z  =  random.randint(1,10)
    return x, y, z


def atividade3():
    n = random.randrange(10,30)
    return n


def atividade4():
    for n in range(10,0,-1):
        print(n)
    print('fogo!')
atividade4()


def atividade5():
    n= int(input('digite um numero:'))
    soma = 0
    for i in range (2,n + 1,2):
        soma += n
        print(soma)
atividade5()

def atividade6():
    n = int(input('digite um numero:'))
    for x in range(1,11):
        print(x*n)
atividade6()

def atividade7():
    for x in range(99,1,-2):
        print(x)
atividade7()