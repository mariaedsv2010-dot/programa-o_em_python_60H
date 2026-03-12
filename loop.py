import random
for chances in range (3):
 a = random.randint(1,10)
 chute = int(input('digite seu  chute:'))
 print('voce tem,',chances , 'chances')
 if a == chute:
  print('ganhou!! acertou em cheio!')
  break
 else:
  print('errou feio...')
  if chances == 0:
   print('nao acertou nenhum...')