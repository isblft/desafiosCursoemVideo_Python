soma = 0 #acumulador, acumulando os valores
cont = 0 #contador, conta +1
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont = cont + 1
        soma = soma + c
print("A soma de todos os {} valores solicitados é {}.".format(cont, soma))








