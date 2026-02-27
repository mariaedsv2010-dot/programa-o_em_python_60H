
print('SISTEMA DE VERIFICAÇÃO DE MÉDIA')

nome = input('Digite o nome do aluno:')

print('digite as notas do aluno', nome)
n1 = float(input('Digite sua nota 1'))
n2 = float(input('Digite sua nota 2'))
n3 = float(input('Digite sua nota 3'))
print('***' * 15)
print('Média do aluno(a)', nome)
media = ( n1 + n2 + n3)/ 3
print('média do aluno(a)', nome)
print(round(media, 3))

aprovada = media >= 7
recuperacao = media >= 5 and media < 7
reprovada = media < 5

print(f'''
SITUAÇÃO DA ALUNA {nome}

APROVADA? - {aprovada}
REPROVADA? - {reprovada}
RECUPERAÇÃO? - {recuperacao}
      
''')

      