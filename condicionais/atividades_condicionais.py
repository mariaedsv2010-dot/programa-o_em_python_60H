#atividade 1 
n = int(input('digite um numero:'))
if n > 0 :
    print('positivo')
elif n < 0 :
    print('negativo')
else:
    print('zero')
   

#atividade 2

idade = int(input('digite sua idade:'))
if idade >=16 :
    print('pode votar')
else:
    print('nao pode votar')

#atividade 3 
numero = int(input('digite um numero:'))
if numero % 2 == 0:
    print('numero par')
else:
    print('numero impar')

#atividade 4
a = int(input('digite um numero:'))
b = int(input('digite um numero:'))
c = int(input('digite um numero:'))
if a == b == c:
    print('equilatero')
elif a == b or a == c or b == c:
    print('isosceles')
else:
    print('escaleno')

#atividade 5 
d = int(input('digite um numero:'))
if d % 5 == 0 and d % 7 == 0:
    print('é multiplo')
else:
    print('nao é')

#atividade 6
n1 = int(input('digite um numero:'))
if n1 > 0 and n1 > 10:
    print('positivo e maior que 10')
else:
    print('nao é positivo e nao é maior que 10')