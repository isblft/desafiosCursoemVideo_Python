soma = 0
cont = 0
for c in range(1, 7):
    n = int(input("Digite o {} valor: ".format(c)))
    if n % 2 == 0:
        cont += 1
        soma += n
print('Você me informou {} números e o valor total foi {}.'.format(cont, soma))







