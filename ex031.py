distancia = float(input('Qual a distância da viagem em Km: '))
if distancia <= 200:
    vduzentos = distancia * 0.50
    print('O valor da passagem é de: {:.2f}'.format(vduzentos))
else:
    vmais = distancia * 0.45
    print("O valor da passagem é de {:.2f}".format(vmais))

#preco = distancia * 0.50 if distancia <= 200 else distancia * 0.45
