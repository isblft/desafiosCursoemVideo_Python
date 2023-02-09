#Escreva um programa que converta uma temperatura digitandoem graus Celsius e converta para graus e Fahrehheit.
t = int(input('Digita a temperatura em Cº: '))
f = (t*1.8) + 32
print('{}Cº equivalem a {}ºF'.format(t, f))