#30: Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
num = int(input('Digite um número: '))
if num % 2 == 0:
    print(num, 'é um número par!')
else:
    print(num, 'é um número ímpar')