#atividade 1
def comparar(x , y):
    if x % 2 == 0:
        print('numero par')
    else:
        print('numero impar')
    if y % 3 == 0:
        print('numero impar')
    else:
        print('numero par')
comparar(10, 3)

#atividade 2
def multiplicar(n1,n2,n3):
    print(n1*n2*n3)
multiplicar(10,5,4)

#atividade 3 
def valor_elevado(f):
    print(f**2)
valor_elevado(10)

# atividade 4
def mensagem(idade):
  idade = input('digite sua idade:')  
  if idade == 18:
    print('paçoca')
mensagem(18)

#atividade 5
def idade(ano):
    print(2026 - ano)
idade(2000)