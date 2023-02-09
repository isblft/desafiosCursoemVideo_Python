#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto.
p = float(input("Qual valor do produto: R$"))
pd = p-(5/100*p)
print("O valor com desconto de 5% fica: R${:.2f}\n".format(pd))
print('Agora tudo faz SeNtIdO!!')

# Correção Guanabara: porcentagem:  o valor de desconto/100*numeroDigitado
