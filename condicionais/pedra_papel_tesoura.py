import random
maquina = ['','✂️','🪨','🧻']
escolha_maquina = random.choice(maquina)
id_maquina = maquina.index(escolha_maquina)
print(escolha_maquina)

minhas =['✂️','🪨','🧻']
print('escolha ✂️ - 1 ,''🪨 - 2,''🧻 - 3')
minha_escolha = int(input('escolha o objeto'))

if minha_escolha == id_maquina:
   print('empate')
   print('minha escolha - ' , minhas[minha_escolha])
   print( 'escolha da maquina ', escolha_maquina)
elif id_maquina == 1 and minha_escolha == 3:
   print('vitoria da maquina🤖🤖')
   print('minha escolha- ❌', minhas[minha_escolha])
   print('escolha da maquina',escolha_maquina)
elif id_maquina == 2 and minha_escolha == 1:
    print('Vitoria da maquina! 👽💀')    
    print('Minha escolha - ❌  ', minhas[minha_escolha])
    print('Escolha da maquina', escolha_maquina )
elif id_maquina == 3 and minha_escolha == 2:
    print('Vitoria da maquina! 👽💀')    
    print('Minha escolha - ❌ ', minhas[minha_escolha])
    print('Escolha da maquina', escolha_maquina )
elif id_maquina == 3 and minha_escolha == 1:
    print('SUA Vitoria!')    
    print('Minha escolha - 😍😘 ', minhas[minha_escolha])
    print('Escolha da maquina', escolha_maquina )
elif id_maquina == 1 and minha_escolha == 2:
    print('SUA Vitoria!')      
    print('Minha escolha - 😍😘 ', minhas[minha_escolha])
    print('Escolha da maquina', escolha_maquina )
elif id_maquina == 2 and minha_escolha == 3:
    print('SUA Vitoria!')      
    print('Minha escolha - 😍😘 ', minhas[minha_escolha])
    print('Escolha da maquina', escolha_maquina )