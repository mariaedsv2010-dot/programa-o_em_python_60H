#nome e valor dos quartos
quartos = ['simples', 'duplo', 'luxo']
valores = [100.,150.0,250.0]

escolhaas_usua = []
custo_usu = []

cliente_1 = int(input(' digite sua idade'))
cliente_2 = int(input(' digite sua idade'))
cliente_3 = int(input(', digite sua idade'))


n_cliente_1 = input('digite o nome:, digite sua idade')
n_cliente_2 = input('digite o nome:, digite sua idade')
n_cliente_3 = input('digite o nome:, digite sua idade')

print('escolha um quarto', quartos)
print('simples - 0', 'duplo - 1', 'luxo- 2')

q_cliente_1 = int(input('quarto:'))
q_cliente_2 = int(input('quarto:'))
q_cliente_3 = int(input('quarto:'))

d_cliente_1 = int(input('dias cliente 1'))
d_cliente_2 = int(input('dias cliente 2'))
d_cliente_3 = int(input('dias cliente 3'))

escolhaas_usua.extend([[quartos[q_cliente_1]],quartos[q_cliente_2], quartos[q_cliente_3]])
custo_usu.extend([valores[q_cliente_1], valores[q_cliente_2], valores[q_cliente_3]])

c1 = custo_usu[0] * d_cliente_1
c2 = custo_usu[1] * d_cliente_2
c3 = custo_usu [2] * d_cliente_3

soma = sum (custo_usu)
print(soma)