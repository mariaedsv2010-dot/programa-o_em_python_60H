#1
list1 = range(1,1001)
c = 0
while c <= 1000:
    print(c)
    c= c+1




# 2


sistema = {

'senha': '123',
'aluno': []


}



for chances in range (3):
    print('bem vindo ao sistemas de notas')
    senha = input('digite sua senha:')
    if senha == sistema['senha']:
        print('ola')
        nome = input('digite um nome:')

        
    notas_alunos = []
    print('Cadastre as notas: ')

    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    n3 = float(input('Nota 3: '))

    notas_alunos.extend([n1,n2,n3])
    media = sum(notas_alunos)/len(notas_alunos)
    print('Notas: ', notas_alunos, 'Aluno: ', sistema['aluno'], 'media', media)
    break
    
else:
    print('incorreta digite novamente ...')    





   


