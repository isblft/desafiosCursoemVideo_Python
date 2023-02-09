peso = float(input('Digite seu peso (Kg): '))
altura = float(input("Digite sua altura: "))
imc = peso / altura ** 2
print("Seu IMC: {:.1f}".format(imc))
print("CLASSIFICAÇÃO: ")
if imc <= 18.5:
    print("Você está abaixo do Peso.")
elif 18.5 <= imc < 25:
    print("Você está no Peso Ideal.")
elif 25 <= imc < 30:
    print("Você está em Sobrepeso.")
elif imc <= 40:
    print("Você está com Obesidade.")
else:
    print("Você está com Obesidade Mórbida.")
    

