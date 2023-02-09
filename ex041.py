from datetime import date
atual = date.today().year
nasc = int(input("Digite seu ano de nascimento: "))
idade = atual - nasc
print('Você nasceu em {} então tem {} anos.'.format(nasc, idade))
if idade <= 9:
    print('Você está na categoria: MIRIM!')
elif idade <= 14:
    print('Você está na categoria: INFANTIL!')
elif idade <= 19:
    print('Você está na categoria: JÚNIOR!')
elif idade <= 25:
    print('Você está na categoria: SÊNIOR!')
else:
    print("Você está na categoria: MASTER!")



