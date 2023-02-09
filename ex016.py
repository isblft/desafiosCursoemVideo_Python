#Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
import math
#ou from math import trunc, para importar apenas o trunc
n = float(input('Digite um valor qualquer: '))
print('O valor digitado foi {} e sua parte inteira é {}.'.format(n, math.trunc(n)))

#ou
n = float(input('Digite um número:'))
print('O número digitado foi {} e sua porção inteira {:.0f}.'.format(n, int(n)))

#ou
n = float(input('Digite um valor qualquer: '))
a = math.floor(n)
print('O número {} tem a parte inteira {}.'.format(n,a))

