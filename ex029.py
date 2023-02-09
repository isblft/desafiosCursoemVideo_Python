# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 por cada Km acima do limite.

velocidade = int(input('Qual a velocidade atual do carro? '))
multa = (velocidade - 80) * 7
if velocidade > 80:
    print('Você ultrapassou o limite de 80Km/h, será multado no valor de R${:.2f}'.format(multa))
else:
    print('Você está dentro do padrão de velocidade permitido, que é de 80Km/h. Tenha uma Ótima Viagem!')
print('Dirija com segurança!')

# condição simples
# velocidade = float(input('Qual a velocidade atual do carro? ')
# if velocidade > 80:
#   print('Você ultrapassou o limite de velocidade!')
#   multa = (velocidade - 80)*7
#   print('Deverá pagar uma multa no valor de {:2.f}'.format(multa))
# print('Dirija com segurança')
