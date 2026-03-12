#atividade 1
n1 = int(input())
match n1 % 2:
   case 0:
      print('o numero é par')
   case _:
      print('o numero é impar')





#atividade 2
num = int(input())
match num:
 case 0:
    print('zero')
 case x if x > 0:
    print('positivo')
 case x if x < 0:
    print('negativo')

#atividade 3
minha_string = input()
match minha_string:
 case "":
      print('esta vazia')
 case _:
      print('tem algo')     

#atividade 4
n2 = int(input())
match n2:
   case 10:
      print('dez')
   case x if x > 10:
      print('maior que dez')
   case x if x < 10:
      print('menor que dez')


#atividade 5
n4 = int(input())
match n4:
   case x if x == 12:
      print('criança')
   case x if x == 17:
      print('adolescente')
   case x if x == 35:
      print('jovem')
   case x if x == 64:
      print('adulto')
   case x if x == 65:
      print('idoso')
