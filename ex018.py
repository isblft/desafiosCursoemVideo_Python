# 18Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
import math

ang = float(input('Digite o ângulo que você deseja: '))

s = math.sin((math.radians(ang)))
c = math.cos((math.radians(ang)))
t = math.tan((math.radians(ang)))
print("O ângulo: {}\nSENO: {:.2f}\nCOSSENO: {:.2f}\nTANGENTE: {:.2f}".format(ang, s, c, t))

#antes de calcular apenas o math.sin, é necessario converter para radianos usando: math.radians
