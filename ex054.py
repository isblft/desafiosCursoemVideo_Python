from datetime import date
atual = date.today().year
totalmaior = 0
totalmenor = 0
for pessoa in range(1, 8):
    ano = int(input("Digite seu ano de nascimento: "))
    idade = atual - ano
    if idade >= 21:
        totalmaior += 1
    else:
        totalmenor += 1
print("{}, são maiores de idade.".format(totalmaior))
print('{}, não são maiores de idade.'.format(totalmenor))










