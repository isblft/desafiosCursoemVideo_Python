# Faça um programa que leia o comprimento do cateto oposto
# e do cateto adjacente de um triângulo retângulo.
# Calcule e mostre o comprimento da hipotenusa.

import math

co = float(input('Digite o comprimento do cateto oposto: '))
ca = float(input('Digite o comprimento do cateto adjacente: '))
h = math.hypot(co, ca)
print('O valor do cateto oposto é {}\nO comprimento do cateto adjacente é {}\nEntão o comprimmento da hipotenusa é '
      'de: {:.2f}'.format(co, ca, h))

# isso nada mais é que somar a potencia dos catetos e fazer a raiz quadrada
# h = math.sqrt(co*co + ca*ca)
