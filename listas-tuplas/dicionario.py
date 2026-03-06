ecommerce = {                                                                                                           

'creme de pentear':30.,
'shampoo':50,
'condicionador':30 


}



prod1 =input('digite o seu produto 1:')

prod2 = input('digite o seu produtp 2:')

carrinho = []
valores = []


carrinho.append(prod1)
carrinho.append(prod2)

valores.append(ecommerce[prod1])
valores.append(ecommerce[prod2])

soma = sum(valores)

print(carrinho)
print('R$', soma)

# ecommerce = {

# 'creme de pentear:'['salonline,lola,wella'],



# 'shampoo:' ['eudora,pantene,elseve'],

# 'condicionador:' ['loreal,seda,dove']:



# }



