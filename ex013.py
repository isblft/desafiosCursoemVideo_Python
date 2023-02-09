#Faça um algoritmo que leia o salario de um funcionario e mostre seu novo salario, com 15% de aumento.
s = float(input('Qual valor do salário: R$'))
sa = s+(15/100*s)
print('Seu novo salário com aumento de 15% é: {:.1f}\n'.format(sa))
print('Essa foi fácil depois da primeira né, só trocar o sinal')


