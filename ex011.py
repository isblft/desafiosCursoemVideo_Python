#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a
# quantidade de tinta  necessária para pinta- la, sabendo que cada litro de tinta, pinta uma área de 2m².
l = float(input("Digite a largura da parede: "))
a = float(input("Digite a altura da parede: "))
r = float(input('Digite o rendimento da tinta: '))
area = l * a
t = area / r
print("O cálculo da área é: {} m²,\nvocê irá precisar de {}l de tinta".format(area, t))