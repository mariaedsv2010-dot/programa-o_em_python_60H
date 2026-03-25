#atividade1
try:
    n = int(input('adcione um numero inteiro:'))
except ValueError:
    print('esse numero não é inteiro')
  

#atividade 2
try:
 x = int(input('adcione um numero:'))
 y = int(input('adcione um numero:'))
 print(n/y)
except ZeroDivisionError:
   print('nao pode ser dividido por 0')

#atividade 3
try:
   l = [1,2,3]
   print(l[2])
except IndexError:
   print('esse indice nao existe')