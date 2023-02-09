#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar.
r = float(input("Quanto dinheiro você tem: R$"))
d = r/5.15
e = r/5.51
print('Você pode comprar US${:.2f} e {:.2f}€.'.format(d, e))

print("Agora você entendeu né, você precisa saber como resolver pra depois resolver!")