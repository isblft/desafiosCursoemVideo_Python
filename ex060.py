#usando a biblioteca do Python
from math import factorial
n = int(input("Digite um número para calcular o seu fatorial: "))
fatorial = factorial(n)
print("O fatorial de {} é {}.".format(n, fatorial))

#sem a biblioteca math
'''
n = int(input("Digite um número para calcularmos o seu fatorial: "))
c = n
f = 1
print("Calculando {}!\n".format(n), end='')
while c > 0:
    print("{}".format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f = f * c
    c -= 1
print("{}.". format(f))
'''
